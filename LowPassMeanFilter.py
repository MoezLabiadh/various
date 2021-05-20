# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:03:09 2020

@author: MLABIADH
"""

import rasterio
import numpy as np
import scipy
import scipy.ndimage

input1 = r'H:\Profile\Desktop\TRAINING\RS\SnowCoverProject\Script_Outputs\S2A_T11UNQ_20191208_Snow_cover_extent.tif'

raster = rasterio.open (input1)

array = raster.read()

profile = raster.profile

kernel = np.ones((3,3))
kernel_3d = kernel[None,:,:] # Add singleton dimension

print (kernel_3d.shape)
print (array.shape)
result = scipy.ndimage.convolve(array, weights=kernel_3d) / kernel_3d.size
finalOutput = result.squeeze() # Remove singleton dimension