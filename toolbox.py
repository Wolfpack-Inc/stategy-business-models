import pandas as pd
import peewee as pw

class ToolBox:
    def __init__(self):
        self.connect_db()

    def connect_db(self):
        """
        Connect to the mysql database
        """
        self.db = pw.MySQLDatabase('video-games', **{
            'charset': 'utf8',
            'use_unicode': True,
            'user': 'remote',
            'password': 'EtrPCEc0jt',
            'host': '165.22.199.122'
        })

        self.db.connect()

    def load_data_raw_sql(self, query):
        """
        Transform a string into a sql query
        """

        # Transform the string into an actual sql query
        query = pd.read_sql_query(query, self.db.connection())

        return pd.DataFrame(query)

    def load_data_sql(self, select='*', table='', where='', limit=None):
        """
        Function to select data from the database with certain parameters
        """

        limit = 'LIMIT {}'.format(limit) if limit else ''

        query = 'SELECT {} FROM {} WHERE {} {}'.format(select, table, where, limit)

        return self.load_data_raw_sql(query)
