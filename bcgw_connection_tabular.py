import cx_Oracle
import pandas as pd

username = 'MLABIADH'
userpwd = 'MoezLab8812'
instance = 'bcgw.bcgov/idwprod1.bcgov'

connection = cx_Oracle.connect(username, userpwd, instance, encoding="UTF-8")



query = """
           SELECT fire.FIRE_NUMBER

           FROM WHSE_LAND_AND_NATURAL_RESOURCE.PROT_HISTORICAL_INCIDENTS_SP fire,
                WHSE_FOREST_VEGETATION.RSLT_OPENING_SVW opening

           WHERE SDO_WITHIN_DISTANCE(opening.GEOMETRY, fire.SHAPE, 'distance=1000') = 'TRUE'
               AND opening.OPENING_ID = 1310614
        """



df = pd.read_sql(query, con=connection)

print (df.head())
#output = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\PyMe\database_connection\tests\output.csv'
#df.to_csv(output)