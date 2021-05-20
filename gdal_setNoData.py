# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 07:44:37 2020

@author: MLABIADH
"""

from osgeo import gdal

file = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\pyDemo\DEM\dem.tif'
out = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\pyDemo\DEM\dem_utm.tif'

src = gdal.Open (file)

gdal.Warp(out,file,dstSRS='EPSG:32611')

out_utm = gdal.Open(out)

out_utm.GetRasterBand(0).SetNoDataValue(-32768)