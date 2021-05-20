import os
import cx_Oracle
import pandas as pd
from my_logins import get_credentials

def connect_to_DB (db_name):
    """ returns a connection to LRM or BCGW database"""
    username = get_credentials(db_name)[0]
    userpwd = get_credentials(db_name)[1]
    instance = get_credentials(db_name)[2]

    try:
        connection = cx_Oracle.connect(username, userpwd, instance, encoding="UTF-8")
        print ("Successuffuly connected to {} database" .format (db_name))
    except:
        raise Exception('Connection to {}  failed! Please verifiy your login parameters'.format (db_name))

    return connection



def run_query (DB_connection, SQLquery, out_excel):
    """Runs SQL queries"""
    df = pd.read_sql(SQLquery, con=DB_connection)
    del df['SHAPE']
    print (df.head())


    #writer = pd.ExcelWriter(out_excel, engine='openpyxl')
    #df.to_excel(writer,sheet_name='result', encoding='utf-8')
    #writer.save()
    DB_connection.close()


def main ():
    db_name = 'LRM' # takes LRM or BCGW
    workspace = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\tempo'
    out_excel = os.path.join(workspace, 'query_result.xlsx')

    # Your SQL query goes here
    SQLquery ="""
            SELECT*
            FROM FORESTVIEW.SV_BLOCK
            WHERE TSO_CODE = 'TKO'
                  AND FIELD_TEAM = 'East Kootenay'
                  AND (HVS_STATUS_DATE BETWEEN  TO_DATE ('2015-01-01', 'yyyy-mm-dd') AND
                                                TO_DATE ('2019-12-31', 'yyyy-mm-dd'))

                  AND HVS_STATUS = 'D'
                  AND TENURE = 'B20'
          """
    DB_connection = connect_to_DB (db_name)
    run_query (DB_connection, SQLquery, out_excel)

main ()
