import arcpy

fc = r'\\sfp.idir.bcgov\S164\S63087\Share\FrontCounterBC\Moez\20210607_proximity_analysis\gis\data.gdb\test_dataset'


field = 'CROWN_LANDS_FILE'
cursor = arcpy.da.SearchCursor(fc,field)

val_dict = {}

for row in cursor:
  value = row[0]
  if value not in val_dict.keys():
    val_dict[value] = 0
  else:
    val_dict[value] += 1

print (val_dict)
