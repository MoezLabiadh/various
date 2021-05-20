import arcpy
import os

def create_bcgw_connection(bcgw_user_name,bcgw_password):

    output_path = workspace
    name = 'Temp_BCGW'
    database_platform = 'ORACLE'
    account_authorization  = 'DATABASE_AUTH'
    instance = 'bcgw.bcgov/idwprod1.bcgov'
    username = bcgw_user_name
    password = bcgw_password

    if arcpy.Exists(os.path.join(output_path,'Temp_BCGW.sde')):
        try:
            arcpy.Delete_management(os.path.join(output_path,'Temp_BCGW.sde'))
        except:
            pass

    arcpy.CreateDatabaseConnection_management (output_path,name,
                                               database_platform, instance,
                                               account_authorization,username,
                                               password, 'DO_NOT_SAVE_USERNAME')
    print ("BCGW connection created!")


workspace = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\PyMe\database_connection'
bcgw_user_name = ''
bcgw_password = ''

create_bcgw_connection (bcgw_user_name,bcgw_password)


VQO = os.path.join (workspace, 'Temp_BCGW.sde' , 'WHSE_FOREST_VEGETATION.REC_VISUAL_LANDSCAPE_INVENTORY')


print ('Clipping...')
clip_features = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\TimberAvailability\slope_analysis\workspace\inputs\data.gdb\BA_outline_buffer_50m'
out_feature_class = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\TimberAvailability\slope_analysis\workspace\inputs\data.gdb\tko_VQO'
arcpy.Clip_analysis(VQO, clip_features, out_feature_class)