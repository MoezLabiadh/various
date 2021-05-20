import arcpy
shp = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\comp-20200206-update Drilldown ANNA\BEC_tko_dissolve.shp'
list = []

with arcpy.da.SearchCursor(shp, 'MAP_LABEL') as cursor:
  for row in cursor:
    if (row[0].find('IDF')  != -1) or (row[0].find('MS')  != -1) :
        list. append (str(row[0]))

print (list)


ICHdm,ICHdw1,ICHmk1,ICHmk4,ICHmk5,ICHmw1,ICHmw2,ICHmw3,ICHmw4,ICHmw5,ICHvk1,ICHwk1,ICHxw,ICHxwa,MSdk,MSdm1,MSdw

IDFdk5,IDFdm1,IDFdm2,IDFxh4,IDFxk,IDFxx2,MSdk,MSdm1,MSdw
