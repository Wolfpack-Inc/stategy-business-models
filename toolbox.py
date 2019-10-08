import pandas as pd
import peewee as pw
import os
import re

class ToolBox:
    def __init__(self, cache_folder='./.db_cache/'):
        self.connect_db()
        self.cache_folder = cache_folder

        # Check if the cache folder exists
        if not os.path.exists(self.cache_folder):
            os.mkdir(self.cache_folder)

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

    def create_cache_file_name(self, query):
        return re.sub(r'[,!@#$=\ \']', '', query)

    def cache_file(self, df, file_name):
        cache_file = self.cache_folder + file_name + '.pkl'

        df.to_pickle(cache_file)

    def load_data_raw_sql(self, query):
        """
        Transform a string into a sql query
        """

        # Transform the string into an actual sql query
        query = pd.read_sql_query(query, self.db.connection())

        return pd.DataFrame(query)

    def load_data_sql(self, select='*', table='', where='', limit=None, use_cache=True):
        """
        Function to select data from the database with certain parameters
        """

        limit = 'LIMIT {}'.format(limit) if limit else ''

        where = 'WHERE {}'.format(where) if where else ''

        query = 'SELECT {} FROM {} {} {}'.format(select, table, where, limit)

        # Cached file name
        file_name = self.create_cache_file_name(query)
        cache_file = self.cache_folder + file_name + '.pkl'

        # Check if the cached file exists
        if os.path.exists(cache_file) and use_cache:
            print('Loaded from cache')
            df = pd.read_pickle(cache_file)

        # Otherwise load the data from the database
        else:
            print('Loading from database')
            # Create the dataframe
            df = self.load_data_raw_sql(query)

            # Cache the file
            self.cache_file(df, file_name)

        return df
