# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:45:10 2020

@author: MLABIADH
"""

import os
import rasterio
import rasterio.mask
import numpy as np
import geopandas as gpd
from osgeo import gdal, ogr, osr

# Create script variables
Workspace = 'F:/tko_root/GIS_WORKSPACE/MLABIADH/PyMe/slope_analysis/data'
slope_raster = os.path.join (Workspace, 'Slope' , 'sheep_creek_slopePercent.tif') 
AOI =  os.path.join (Workspace, 'AOI' , 'AOI.shp') 

#Clip the slope raster to the AOI extent
 ##Make a new folder for the clipped raster
Masked_dir = os.path.join (Workspace, 'Masked')
if not os.path.exists(Masked_dir):
    os.makedirs (Masked_dir)
else:
    pass

 ##Clip the raster and save in the new folder     
print('Clipping in progress...')

'''
wrap_options = gdal.WarpOptions(cutlineDSName=AOI,cropToCutline=True)
out_raster = gdal.Warp(srcDSOrSrcDSTab= slope_raster,
                    destNameOrDestDS= os.path.join (Masked_dir , os.path.basename (AOI)[:-4]+'_slope.tif'),
                    options=wrap_options)