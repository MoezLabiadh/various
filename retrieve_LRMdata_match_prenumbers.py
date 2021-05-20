from itertools import combinations
import pandas as pd
import arcpy


mxd_path = r'\\BCTSdata.bcgov\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\harold_tool\consultation_tracker.mxd'
mxd = arcpy.mapping.MapDocument(mxd_path)

'''
xls_file = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\harold_tool\prenumbers.xlsx'

df = pd.read_excel(xls_file)

list_initial = df['blk_nbr'].tolist()
print('The excel has {} rows' .format(len(list_initial)))

list_string = ','.join("'" + str(x) + "'" for x in list_initial)

print (list_string)

'''

new_list = [160350311, 160354315, 160354314, 160354326, 160350317, 160350313, 160350316, 160350312, 160353472, 160353475, 160370424, 160354322, 160350315, 160354316, 160354193, 160353476, 160354324, 160354325, 160350314, 160353911, 160354191]
list_IDs = []
list_NBRs = []



for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name == "FORESTVIEW.SV_BLOCK_2":
        block_lyr = lyr
        fields = ['CUTB_SEQ_NBR']
        cursor = arcpy.da.SearchCursor(block_lyr,fields)
        for row in cursor:
            list_IDs.append(int(row[0]))

for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name == "FORESTVIEW.SV_BLOCK":
        block_lyr = lyr
        fields = ['CUTB_SEQ_NBR']
        cursor = arcpy.da.SearchCursor(block_lyr,fields)
        for row in cursor:
            list_NBRs.append(int(row[0]))

list_all = list_IDs + list_NBRs

comb = combinations(list_all, 2)
for x, y in comb:
        if x == y:
            list_all.remove(x)

print(len(list_all))

list_string = ','.join("'" + str(x) + "'" for x in list_all)

print(list_string)

lic_list = []
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name == "FORESTVIEW.SV_BLOCK":
        block_lyr = lyr
        fields = ['LICN_SEQ_NBR']
        cursor = arcpy.da.SearchCursor(block_lyr,fields)
        for row in cursor:
            lic_list.append(int(row[0]))


print(len(lic_list))

list_string = ','.join("'" + str(x) + "'" for x in lic_list)
print(list_string)
'''
