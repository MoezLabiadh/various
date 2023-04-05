'''
This script fixes shapes for ILRR:
    - Reprojects to BC Albers
    - Dissolves multi-geometries
'''

import os
import fiona
import geopandas as gpd

fiona.drvsupport.supported_drivers['KML'] = 'rw' # enable KML support which is disabled by default

wks = r'\\spatialfiles.bcgov\Work\lwbc\visr\Workarea\moez_labiadh\WORKSPACE\tempo\20230404_tanya'
kml_n = '2023-03-28 KML Site 7 to 8 1415214.kml'

in_kml = os.path.join(wks, kml_n)

gdf = gpd.read_file(in_kml, driver='KML')

gdf['dissolve'] = 1
gdf = gdf.dissolve(by='dissolve')

if not gdf.crs.to_epsg() == 3005:
    gdf = gdf.to_crs(3005)
    
gdf.to_file(os.path.join(wks,'fixed_'+kml_n[:-4]+'.shp'))
