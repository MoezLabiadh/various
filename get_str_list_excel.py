# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 09:48:03 2021

@author: MLABIADH
"""

import pandas as pd

excel = r'F:\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\comp-20210323-5year_plan_arrowSouth\data_north.xlsx'
df = pd.read_excel(excel)

list_tsl = list(set(df['TSL'].tolist()))

tsl_string = ','.join("'" + str(x) + "'" for x in list_tsl )

print (len(list_tsl))
print (tsl_string)