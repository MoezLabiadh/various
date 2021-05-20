# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:27:19 2020

@author: MLABIADH
"""
import os

path = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\ong-20200617-more PFR maps KARLI\maps'

for filename in os.listdir(path):
    firstPart = filename [0:8]
    secondPart = filename [14:-4]
    thirdPart = filename [7:13]  
    src = os.path.join(path, filename)
    dst = os.path.join (path, firstPart + secondPart + thirdPart + ".pdf")

    os.rename(src, dst)
    
    print (dst)
    