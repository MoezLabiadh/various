# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 07:54:58 2020

@author: MLABIADH
"""

import os
import sys
import rasterio
from osgeo import gdal, gdal_array, ogr

Workspace = 'H:/Profile/Desktop/TRAINING/RS/SnowCoverProject'
S2_path = os.path.join (Workspace, 'raw_data/S2B_MSIL2A_20191208T184749_N0213_R070_T11UNQ_20191208T205518.SAFE')

#Browse through the S2 product folder and retrieve the following bands: Green, NIR, SWIR and Cloud probability
for root, dirs, files in os.walk(S2_path):
    for name in files:
        if name.endswith("B03_10m.jp2"):
            Gpath = os.path.join (root, name)
        elif name.endswith("B04_10m.jp2"):
            Rpath = os.path.join (root, name)
        elif name.endswith("B08_10m.jp2"):
            NIRpath = os.path.join (root, name)
        elif name.endswith("B11_20m.jp2"):
            SWIRpath = os.path.join (root, name)
        elif name.endswith("CLDPRB_20m.jp2"):
            CLDprobpath = os.path.join (root, name)
        else:
            pass
print (Gpath)

#Read the bands as arrays.
with rasterio.open(Gpath) as green:
    GREEN = green.read()
with rasterio.open(Rpath) as red:
    RED = red.read()
with rasterio.open(NIRpath) as nir:
    NIR = nir.read()
with rasterio.open(SWIRpath) as swir:
    SWIR = swir.read()
with rasterio.open(CLDprobpath) as cloud:
    CLOUDprob = cloud.read()
    
ndsi= (GREEN.astype(float) - SWIR.astype(float)) / (GREEN+SWIR)

profile = GREEN.meta
profile.update(driver='GTiff')
profile.update(dtype=rasterio.float32)

NDSI = os.path.join (Workspace, 'NDSI.tif')
with rasterio.open(NDSI, 'w', **profile) as dst:
    dst.write(NDSI.astype(rasterio.float32))
