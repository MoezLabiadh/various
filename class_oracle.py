
import cx_Oracle

class Oracle:

    def __init__(self,db_name, instance,username,password):
        self.db_name = db_name
        self.instance= instance
        self.username= username
        self.password= password


    def get_credentials():
        if db_name == 'LRM_mapview':
            instance = 'lrmbctsp.nrs.bcgov/DBP06.nrs.bcgov'
            username = 'map_view_15'
            password= 'sharing'

        elif self.db_name == 'BCGW':
            self.instance = 'bcgw.bcgov/idwprod1.bcgov'
            self.username = 'MLABIADH'
            self.password= password = 'MoezLab8810'


    def connect ():
        try:
            connection = cx_Oracle.connect(username, userpwd, instance, encoding="UTF-8")
            print ("Successffuly connected to {} database" .format (db_name))

        except cx_Oracle.DatabaseError as e:
            raise

    def disconnect():
         connection.close()

LRM = Oracle('LRM_mapview', instance, username, username)


LRM.connect()


