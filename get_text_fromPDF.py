# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:56:35 2020

@author: MLABIADH
"""

import os
import pandas as pd
import PyPDF2 as pdf2

search_dir = r'\\...\PID Title Search'

file_list = []  
val_dict = {}
val_dict['PID'] = []
val_dict['Ownership'] = []

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                file_list.append (file_path)
        
for file in file_list:
    with open (file, "rb") as f:
        pdf = pdf2.PdfFileReader(f)
        num = pdf.numPages
        page = pdf.getPage(22)
        text = page.extractText()
        
        #list = text.split('Address:')
        if 'HER MAJESTY THE QUEEN' in text:
            owner = 'CROWN'
        else:
            owner = 'PRIVATE'
            
        list_2 = text.split('Identifier:')
        pid = list_2[1][:11]
        print ('The owner of PID {} is {}'.format(pid, owner))
        
        val_dict['PID'].append(pid)
        val_dict['Ownership'].append(owner)
        
df = pd.DataFrame.from_dict(val_dict)
df.index = df.index + 1
df.index.name = '#'

out_excel = r'\\...\PID Title Search\status_check.xlsx'
df.to_excel(out_excel)
