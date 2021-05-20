import arcpy

inputFolder = r'\\BCTSdata.bcgov\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\AAAcomp-20200128-THLB_analysis_George\data\data.gdb\tests'

arcpy.env.workspace = inputFolder

FCs = arcpy.ListFeatureClasses()

for FC in FCs:
    if "OGMA" in FC:
        arcpy.AddField_management(FC, "OGMA", "TEXT", 5, "", "", "", "NULLABLE", "")
        with arcpy.da.UpdateCursor(FC, "OGMA") as cursor:
          for row in cursor:
            row[0] = "Y"
            cursor.updateRow(row)


