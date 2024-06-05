import os
import fiona
from shapely import wkt

import geopandas as gpd
gpd.io.file.fiona.drvsupport.supported_drivers['KML']

# Set the folder path where the KMZ files are located
folder_path = r'W:\lwbc\visr\Workarea\moez_labiadh\WORKSPACE_2024\20240605_aquaPlants_new_2024_harvestAreas\New 2024 harvest areas\New Area a'

# Create an empty GeoDataFrame to store the combined data
combined_gdf = gpd.GeoDataFrame()

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a KMZ file
    if filename.endswith('.kml'):
        file_path = os.path.join(folder_path, filename)
        
        # Read the KMZ file into a GeoDataFrame
        gdf = gpd.read_file(file_path, driver='KML')
        
        # Flatten the geometries to 2D
        gdf['geometry'] = gdf['geometry'].apply(lambda geom: wkt.loads(wkt.dumps(geom, output_dimension=2)))
        
        # Append the GeoDataFrame to the combined GeoDataFrame
        combined_gdf = combined_gdf.append(gdf)

# Reset the index of the combined GeoDataFrame
combined_gdf = combined_gdf.reset_index(drop=True)
combined_gdf = combined_gdf.to_crs(epsg=3005)

# Export the combined GeoDataFrame as a shapefile
output_path = os.path.join(folder_path, 'new_area_5628.shp')
combined_gdf.to_file(output_path)