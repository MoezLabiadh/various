"""
Last updated on: 2020-09-17

Author: MLABIADH, BCTS-TKO

Purpose: This script compares FOREST VIEW EVs to their original V tables. Differences are reported in a CSV output file.
         the "is_only_in" field indicates if the record is only in "EV or "V" tables.

"""
import os
import cx_Oracle
import pandas as pd
import numpy as np

def connect_to_OracleDB (username, userpwd, instance):
    """ Returns a connection to Oracle DB"""
    try:
        connection = cx_Oracle.connect(username, userpwd, instance, encoding="UTF-8")
        print ("Successfully connected to the database.")
    except cx_Oracle.DatabaseError as e:
        print (e)
        raise

    return connection

def get_tables_fromDB (connection):
    """ Returns a list of tables based on specified critera"""
    # Create a cursor
    cur = connection.cursor()

    # Get all tables in the DB
    cur.execute("""SELECT DISTINCT (table_name)
                   FROM all_tab_columns
                   WHERE owner = 'FORESTVIEW'
                """)

    # Make a list of tables to be tested
    table_list =["FORESTVIEW." + row[0] for row in cur if str(row).find('EV_') != -1]

    return table_list

def test_tables (table_list, connection, out_loc):
    """ compares tables based on specified conditions"""
    # Loop through EVs
    for EV in table_list:
        # get table names
        V = EV.split('.')[0] + '.' + EV.split('.')[1][1:]

        EV_name = EV.split('.')[1]
        V_name = V.split('.')[1]

        # queries
        SQLquery_EV ="""
                         SELECT*
                         FROM """ + EV + """
                     """

        SQLquery_V ="""
                        SELECT*
                        FROM """ + V + """
                    """

        # read queries in pandas dataframe
        df_EV = pd.read_sql(SQLquery_EV, con=connection)
        df_V = pd.read_sql(SQLquery_V, con=connection)

        # get the row count
        EV_row_count = df_EV.shape[0]
        V_row_count = df_V.shape[0]

        nbr_miss = V_row_count - EV_row_count

        # print results
        print ('The {EV_t} table has {row_nbr} rows' .format (EV_t = EV_name, row_nbr = EV_row_count))
        print ('The {V_t} table has {row_nbr} rows' .format (V_t = V_name, row_nbr = V_row_count))
        print ('Nbr of rows missing: {nbr}\n' .format(nbr = nbr_miss))

'''        # Export missing rows to table
        if nbr_miss > 1:
            df_merge = pd.merge(df_EV, df_V, how='outer', indicator=True)
            df_merge = df_merge.rename(columns={"_merge": "is_only_in"})
            #df_merge.loc[df_merge.is_only_in == "left_only", "is_only_in"] = "EV"
            #df_merge.loc[df_merge.is_only_in == "right_only", "is_only_in"] = "V"
            df_merge['is_only_in'] = np.where((df_merge.is_only_in == 'left_only'),'EV',df_merge.is_only_in)
            df_merge['is_only_in'] = np.where((df_merge.is_only_in == 'right_only'),'V',df_merge.is_only_in)

            df_miss  = df_merge.loc[(df_merge['is_only_in'] == 'EV') | (df_merge['is_only_in'] == 'V')]

            out_file = os.path.join(out_loc, 'diff_'+ EV_name + ".csv")
            df_miss.to_csv(out_file)
'''
def main():
    instance = 'lrmbctsp.nrs.bcgov/DBP06.nrs.bcgov'
    username = 'map_view_15' # use your LRM connection parameters
    userpwd = 'sharing' # use your LRM connection parameters
    connection = connect_to_OracleDB (username, userpwd, instance)
    table_list = get_tables_fromDB (connection)
    out_loc = r'\\bctsdata.bcgov\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\tempo' # change this to your output location
    test_tables (table_list, connection, out_loc)
    print ("Process Completed. Check your Output Folder for results")

if __name__ == "__main__":
    main()