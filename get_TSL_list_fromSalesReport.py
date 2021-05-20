# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:45:23 2020

@author: MLABIADH
"""
import tabula as tb
import pandas as pd

def get_tsl_list(pdf_file):
    """returns a TSL list from a PDF Sales Schedule report"""
    
    dfs = tb.read_pdf(file, pages = "all", multiple_tables = True)
    df = pd.concat(dfs)
    col_list = df[0].tolist()
    filtered = [file[0:6] for file in col_list if str(file).startswith("A") or  str(file).startswith("TA")]
    filtered_dup = list(set(filtered))
    print ('the PDF has {} TSLs' .format(len(filtered_dup)))
    TSL_list_string = ','.join("'" + x + "'"  for x in filtered_dup )
    
    return TSL_list_string

file = r'F:\tko_root\GIS_WORKSPACE\MLABIADH\SalesSchedule\20210317_2021_2022\TKO Sales Schedule 2021_2022.pdf'

print (get_tsl_list(file))