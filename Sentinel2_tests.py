# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:49:43 2020

@author: MLABIADH
"""
import os
import rasterio
from rasterio.enums import Resampling

Workspace = 'H:/Profile/Desktop/TRAINING/RS/SnowCoverProject'
S2_path = os.path.join (Workspace, 'raw_data/S2B_MSIL2A_20191208T184749_N0213_R070_T11UNQ_20191208T205518.SAFE')

#Browse through the S2 product folder and retrieve the following bands: Green, Red, SWIR and Cloud probability
for root, dirs, files in os.walk(S2_path):
    for name in files:
        if name.endswith("B03_10m.jp2"):
            Gpath = os.path.join (root, name)
        else:
            pass
        
#Read the bands as arrays. Resample (upscale) SWIR and Cloud bands to 10m.
upscale_factor = 2


with rasterio.open(Gpath) as dataset:

    # resample data to target shape
    data = dataset.read(
        out_shape=(
            dataset.count,
            int(dataset.width * upscale_factor),
            int(dataset.height * upscale_factor)
        ),
        resampling=Resampling.bilinear
    )