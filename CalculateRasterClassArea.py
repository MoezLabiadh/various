# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:57:02 2020

@author: MLABIADH
"""

import rasterio
import numpy as np

data = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\PyMe\slope_analysis\data\Reclass\AOI_slope_reclass.tif'
raster =  rasterio.open (data)
array_raster = raster.read()

# Retrieve the pixel size and caluclate the Pixel Area
pixelSizeX, pixelSizeY  = raster.res
pixelArea = pixelSizeX * pixelSizeY 


# Calculate the area in hectares for each Class 
Area_class_1 = (np.count_nonzero(array_raster == 1)*pixelArea)/10000
Area_class_2 = (np.count_nonzero(array_raster == 2)*pixelArea)/10000
Area_class_3 = (np.count_nonzero(array_raster == 3)*pixelArea)/10000
Area_class_4 = (np.count_nonzero(array_raster == 4)*pixelArea)/10000
Area_class_5 = (np.count_nonzero(array_raster == 5)*pixelArea)/10000

print (Area_class_1)
print (Area_class_2)
print (Area_class_3)
print (Area_class_4)
print (Area_class_5)