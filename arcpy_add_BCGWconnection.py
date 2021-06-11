def create_bcgw_connection(path, bcgw_user_name,bcgw_password):
    """Creates a BCGW connnection file"""

    name = 'Temp_BCGW'
    database_platform = 'ORACLE'
    account_authorization  = 'DATABASE_AUTH'
    instance = 'bcgw.bcgov/idwprod1.bcgov'
    username = bcgw_user_name
    password = bcgw_password

    if arcpy.Exists(os.path.join(path,'Temp_BCGW.sde')):
        try:
            arcpy.Delete_management(os.path.join(path,'Temp_BCGW.sde'))
        except:
            pass

    arcpy.CreateDatabaseConnection_management (path,name, database_platform,instance,account_authorization,
                                               username ,password, 'DO_NOT_SAVE_USERNAME')
