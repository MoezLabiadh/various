import os
import arcpy


fc = r'\\sfp.idir.bcgov\S164\S63087\Share\FrontCounterBC\Moez\WORKSPACE\20211125_aquaPlants_FN_consult\data.gdb\Harvest_areas_2022_all'

ha_list = [row[0] for row in arcpy.da.SearchCursor(fc, 'Harvest_Area_Number')]

counter = 1
for ha in ha_list:
    print ('converting {} of {}: {}').format(counter, len(ha_list), str(ha))
    where = """ Harvest_Area_Number = {} """.format(ha)
    fc_lyr = 'fc_lyr'
    arcpy.MakeFeatureLayer_management(fc, fc_lyr)
    arcpy.SelectLayerByAttribute_management (fc_lyr, "NEW_SELECTION", where)
    out_path = r'\\sfp.idir.bcgov\S164\S63087\Share\FrontCounterBC\Moez\WORKSPACE\20211125_aquaPlants_FN_consult\kmz_files'
    out_file = '{}.kmz'.format (str(ha))
    arcpy.LayerToKML_conversion(fc_lyr, os.path.join(out_path,out_file))

    arcpy.Delete_management(fc_lyr)
    counter +=1



