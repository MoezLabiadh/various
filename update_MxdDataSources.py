import arcpy  

mxd = arcpy.mapping.MapDocument(r"\\bctsdata.bcgov\data\tko_root\Data_Library\MXDs\Resource and Terrain Maps\2019\Copy_of_Resource_Map_template_small_arc10.6_EastKootenay_jan2019.mxd")  

for lyr in arcpy.mapping.ListLayers(mxd):
  if lyr.supports("DATASOURCE"):
    OldPath = lyr.workspacePath
    NewPath = OldPath.replace("Layers_Library\SOURCE", "Data_Source")
    lyr.findAndReplaceWorkspacePath(OldPath, NewPath, False)

mxd.save()    
del mxd