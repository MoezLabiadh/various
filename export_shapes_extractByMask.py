import arcpy
from arcpy import env
from arcpy.sa import *
import sys
import os

if arcpy.CheckExtension("Spatial") == "Available":
  arcpy.CheckOutExtension("Spatial")

arcpy.env.overwriteOutput = True


OA_shp = r"\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\AAAcomp-20200128-THLB_analysis_George\data\data.gdb\BCTS_Bdry_op_areas"
out_path = r"\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\ong-20200130-slope_analysis_boundary-George\shps"

oid_fieldname = arcpy.Describe(OA_shp).OIDFieldName
name_field = 'OPAREA_NAM'

with arcpy.da.SearchCursor(OA_shp, [oid_fieldname, name_field]) as cursor:
  for row in cursor:
    theID = row[0]
    theName = row[1]
    print ('working on', row)
    selectClause = str(oid_fieldname)  + ' = ' + str(theID)
    arcpy.MakeFeatureLayer_management(OA_shp,"OA_Layer")
    arcpy.SelectLayerByAttribute_management("OA_Layer", "NEW_SELECTION", selectClause)
    out_name = str(theName) + ".shp"
    print out_name
    arcpy.FeatureClassToFeatureClass_conversion("OA_Layer", out_path, out_name)

raster = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\ong-20200130-slope_analysis_boundary-George\data_slope_analysis.gdb\slope_bounday_OAs_reclass'
gdbPath = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\ong-20200130-slope_analysis_boundary-George\data_slope_analysis.gdb'
arcpy.env.workspace = out_path
FCs = arcpy.ListFeatureClasses()

for FC in FCs:
    name,ext = os.path.splitext(FC)
    temp = ExtractByMask(raster, FC)
    temp.save(gdbPath + "\\slopeClass_" + name)
