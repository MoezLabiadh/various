import pandas as pd

file = r'F:\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\ong-20200916-KMZ file for 2021 EK planting STACEY\list_verify.xlsx'

df = pd.read_excel(file)

list(set(df.UBI) - set(df.UBI_arc))




