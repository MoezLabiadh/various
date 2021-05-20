# -*- coding: utf-8 -*-
"""
This script takes a raster (slope) as input and perform the following manipulations:
    - Clip the raster using a polygon shapefile.
    - Reclassify the slope raster to predefined ranges.
    - Vectorize the final raster output.
    - Calculate Areas for each slope class.
"""
import os
import rasterio
import rasterio.mask
import geopandas as gpd
import numpy as np
import fiona
from osgeo import gdal, ogr

workspace = 'H:/Profile/Desktop/ARCHIVE/2019/LIDAR_works/tests'
AOI = os. path.join (workspace, "test_shp.shp") 
input_raster = os.path.join (workspace, "CanopyCover_NoData.tif")

# Clip the raster using a polygon shp
print ("Clipping raster...in progress")  
with fiona.open(AOI, "r") as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]
    
with rasterio.open(input_raster) as src:
    out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
    out_meta = src.meta

out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})

masked_raster = os.path.join (workspace, "masked_raster.tif")
with rasterio.open(masked_raster, "w", **out_meta) as dst:
    dst.write(out_image)
    
print ("raster clipped")    

# Reclassify the raster   
print ("Reclassifying raster...in progress")  
with rasterio.open(masked_raster) as src:    
    # Read as numpy array
    array_in = src.read()
    profile = src.profile
    # Reclassify
    array_out= array_in.copy()
    array_out[np.where((0 <= array_in) & (array_in <= 0.2)) ] = 1
    array_out[np.where((0.2 < array_in) & (array_in <= 0.5)) ] = 2
    array_out[np.where((0.5 < array_in) & (array_in <= 0.7)) ] = 3
    array_out[np.where((0.7 < array_in) & (array_in <= 1)) ] = 4

reclass_raster = os.path.join (workspace, "CanopyCover_reclass.tif")  
with rasterio.open(reclass_raster, 'w', **profile) as dst:
    dst.write(array_out)
    crs = src.crs
os.remove(masked_raster)
print ("raster reclassified")

# Vectorize the raster
print ("Vectorizing raster...in progress") 
dst_layername = os.path.join (workspace, "raster_to_vector")
src_ds = gdal.Open(reclass_raster)
srcband = src_ds.GetRasterBand(1)
drv = ogr.GetDriverByName("ESRI Shapefile")
dst_ds = drv.CreateDataSource( dst_layername + ".shp" )
dst_layer = dst_ds.CreateLayer(dst_layername, srs = None )
newField = ogr.FieldDefn('gridcode', ogr.OFTInteger)
dst_layer.CreateField(newField)
gdal.Polygonize(srcband, None, dst_layer, 0, [], callback=None)
del src_ds, srcband, drv, dst_ds, dst_layer

print ("raster vectorized")

# add an Area (ha) field, dissolve and aggregate areas
slope_class_vector = gpd.read_file(dst_layername + ".shp")
print ("Calculating area_ha field...in progress") 
slope_class_vector["area_ha"] = slope_class_vector['geometry'].area/ 10000
slope_class_vector = slope_class_vector[['gridcode', 'geometry' , 'area_ha']]
print ("Dissolving and agregating areas...in progress") 
slope_class_vector_dissolve = slope_class_vector.dissolve(by='gridcode' , aggfunc = 'sum')
slope_class_vector_dissolve.to_file(os.path.join (workspace, "Slope_area_stats.shp"))
os.remove(dst_layername + ".shp")

print ("Process Completed")