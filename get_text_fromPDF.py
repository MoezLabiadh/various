# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:56:35 2020

@author: MLABIADH
"""

import os
#import re
import pandas as pd
import PyPDF2 as pdf2

search_dir = r'\\...\title_docs'

file_list = []  
val_dict = {}
val_dict['PID'] = []
val_dict['Owner Info'] = []
val_dict['Owner Type'] = []

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                file_list.append (file_path)
        
for file in file_list:
    with open (file, "rb") as f:
        pdf = pdf2.PdfFileReader(f)
        num = pdf.numPages
        page = pdf.getPage(0)
        text = page.extractText()

        startStr = text.split('Registered Owner/Mailing Address:')[1]
        ownerInfo = startStr.split('Taxation Authority')[0]

        
        if 'HER MAJESTY THE QUEEN' in ownerInfo:
            ownerType = 'CROWN'
        else:
            ownerType = 'PRIVATE'
            
        list_2 = text.split('Identifier:')
        pid = list_2[1][:12]

        val_dict['PID'].append(pid)
        val_dict['Owner Info'].append(ownerInfo)
        val_dict['Owner Type'].append(ownerType)
        
df = pd.DataFrame.from_dict(val_dict)
df.index = df.index + 1
df.index.name = '#'

out_excel = os.path.join(search_dir, 'status_check.xlsx')
df.to_excel(out_excel)
