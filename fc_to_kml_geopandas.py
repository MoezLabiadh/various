import os
import fiona
import geopandas as gpd



def esri_to_gdf (aoi):
    """Returns a Geopandas file (gdf) based on 
       an ESRI format vector (shp or featureclass/gdb)"""
    
    if '.shp' in aoi: 
        gdf = gpd.read_file(aoi)
    
    elif '.gdb' in aoi:
        l = aoi.split ('.gdb')
        gdb = l[0] + '.gdb'
        fc = os.path.basename(aoi)
        gdf = gpd.read_file(filename= gdb, layer= fc)
        
    else:
        raise Exception ('Format not recognized. Please provide a shp or featureclass (gdb)!')
    
    return gdf


fc = r'\\spatialfiles.bcgov\Work\lwbc\visr\Workarea\moez_labiadh\WORKSPACE\20221124_aquaWildPlants_2023_newApps\data.gdb\new_harvest_areas_2023_v2'

gdf = esri_to_gdf (fc)

gdf = gdf.loc[gdf['harvest_area'] == '5623']


fiona.supported_drivers['KML'] = 'rw'
out= r'\\spatialfiles.bcgov\Work\lwbc\visr\Workarea\moez_labiadh\WORKSPACE\20221124_aquaWildPlants_2023_newApps\maps\harvest_area_5623.kml'
gdf.to_file(out, driver='KML')
