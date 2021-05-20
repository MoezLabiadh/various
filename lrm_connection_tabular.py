import os
import cx_Oracle
import pandas as pd

def extract_from_OracleDB (instance, username, userpwd, SQLquery, outputExcel):

    try:
        connection = cx_Oracle.connect(username, userpwd, instance, encoding="UTF-8")
    except:
        print ('Connection failed! Please verifiy your login parameters')

    df = pd.read_sql(SQLquery, con=connection)
    print (df.head())
    #writer = pd.ExcelWriter(outputExcel, engine='xlsxwriter')
    df.to_csv(outputExcel)
    connection.close()


def run():
    instance = 'lrmbctsp.nrs.bcgov/DBP06.nrs.bcgov'
    username = 'map_view_15' #replace with your map_view account
    userpwd = 'sharing' #replace with your password
    workspace = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS' #specify a folder where the script will run
    outputExcel = os.path.join (workspace, 'query_result.csv') # change the output excel file name

    # Your SQL query goes here
    SQLquery ="""
            SELECT*
            FROM FORESTVIEW.V_BLOCK
            WHERE TSO_CODE = 'TKO'
                  AND NAV_NAME = 'Kootenay Lake'
                  AND (HVC_STATUS_DATE BETWEEN  TO_DATE ('2016-01-01', 'yyyy-mm-dd') AND
                                                TO_DATE ('2020-12-31', 'yyyy-mm-dd'))



          """
    extract_from_OracleDB (instance, username, userpwd, SQLquery,outputExcel)


run()