# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:56:35 2020

@author: MLABIADH
"""

import os
import pandas as pd
import PyPDF2 as pdf2



search_dir = r'\\Sfp.idir.bcgov\u164\MLABIADH$\Profile\Desktop\ARCHIVE\2020\GIS-REQUESTS\comp-20200213-FTEK Op 21 PID Title Search Darren\serach'

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
        
print (text)       
'''
        #list = text.split('Address:')
        if 'HER MAJESTY THE QUEEN IN RIGHT OF THE PROVINCE OFBRITISH COLUMBIA' in text:
            owner = 'HER MAJESTY THE QUEEN IN RIGHT OF THE PROVINCE OF BRITISH COLUMBIA'
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

out_excel = r'F:\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\ong-20210204-private_land_owners_Olivia\title_docs\status_check.csv'
df.to_csv(out_excel)

'''
        
        
