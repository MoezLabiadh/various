import arcpy
shp = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\ong-20200206-update Drilldown ANNA\BEC_tko.shp'

listFields = arcpy.ListFields(shp)

if "MATURE" not in listFields:
    arcpy.AddField_management(shp, "MATURE", "TEXT", "", "", 10, "", "NULLABLE", "")

Fields = ['Zone', 'Variant', 'MATURE']

with arcpy.da.UpdateCursor(shp, Fields) as cursor:
  for row in cursor:
    if row[0] == "ICH" and row[1] > 3 :
        row[2] = "Y"
    else:
        row[2] = "N"
        cursor.updateRow(row)

arcpy.MakeFeatureLayer_management(shp,"shp_lyr")
lyr = arcpy.mapping.Layer("shp_lyr")
lyr.definitionQuery = " [MATURE] = 'Y' "
