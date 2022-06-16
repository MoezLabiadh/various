import pandas as pd
import cx_Oracle

file = r'//bctsdata.bcgov\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\tempo\deac_list.xlsx'
df = pd.read_excel(file)

instance = 'lrmbctsp.nrs.bcgov/DBP06.nrs.bcgov'
username = ''
userpwd = ''

df_bdry  = df.loc[df['Field Team'] == 'Boundary']
df_bdry2 = df_bdry.rename(columns={"\nName": "Name"})
name_list = df_bdry2.Name.unique().tolist()
name_set = ','.join("'" + item + "'" for item in name_list)

connection = cx_Oracle.connect(username, userpwd, instance, encoding="UTF-8")


SQLquery ="""
            SELECT*

            FROM FORESTVIEW.V_ROAD_DEACTIVATION rd

            WHERE rd.ROAD_ROAD_NAME IN (""" + name_set +""")
      """


df = pd.read_sql(SQLquery, con=connection)

out = r'//bctsdata.bcgov\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\tempo\out.xlsx'
df.to_excel(out)
