# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:49:53 2020

@author: MLABIADH
"""

import os
import rasterio
import numpy as np


workspace = 'H:/Profile/Desktop/ARCHIVE/2019/LIDAR_works/tests'
A = os.path.join (workspace, "CanopyCover_NoData.tif")
B = os.path.join (workspace, "CanopyCover_raster2.tif")

with rasterio.open(A) as srcA:
    #Read raster as array
     array_inA = srcA.read()
    #Copy metadata. will be passed to the output
     profile = srcA.profile

with rasterio.open(B) as srcB:     
   array_inB = srcB.read()
   profileB = srcB.profile
        

#Fill array_out using condition: IF pixel value of A < 0.5 THEN use pixel value of B ELSE use pixel value of A
array_out = np.where((array_inA > 0.5), array_inB, array_inA)

#write the new raster to the disk
result2 = os.path.join (workspace, "result2.tif")  
with rasterio.open(result2, 'w', **profile) as dst:
    dst.write(array_out)
    crs = srcA.crs
    
print ("Process completed")