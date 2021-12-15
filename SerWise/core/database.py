import sqlite3
from SerWise.setting import database_path, database_header, database_table_name
from SerWise.util.logger import get_core_logger

class userDatabase:
    '''
    Overview:
        Used to manage user database, read and write, modify the information in it
    Note:
        Many settings of the database can be set in setting.py
    '''
    def __init__(self) -> None:
        self.conn = sqlite3.connect(database_path)
        self.executer = self.conn.cursor()
        header = ' '.join(list(map(lambda x : x+" string,", database_header)))[:-1]
        sql = 'create table if not exists ' + database_table_name + \
              '(' + header + ')'
        self.executer.execute(sql)

    def result_save(self, table_name : str, dict : dict):
        '''
        overview:
            According to the input table name and dictionary key, construct a new table, and store the dictionary value correspondingly in the database
        Paramters:
            - table_name<str>: table name
            - dict<dict>: the dict need to be parsed and store into database
        '''
        header = ' '.join(list(map(lambda x : x[1:]+" string,", dict.keys())))[:-1]
        sql = 'drop table if exists ' + table_name
        self.executer.execute(sql)

        sql = 'create table ' + table_name + \
              '(' + header + ')'
        self.executer.execute(sql)

        self.conn.commit()
        sql = "insert into " + table_name  + ' values '
        values = '(' +  ",".join(list(map(lambda x: '"'+ str(x)+ '"',dict.values()))) + ')'
        sql += values
        self.executer.execute(sql)

        self.conn.commit()


    def insert_value(self, values) -> None:
        '''
        Overview:
            Insert data into the user table
        Parameters:
            values: The data to be inserted requires the same format with header
        '''
        sql = "insert into " + database_table_name  + ' values '
        values = '(' +  ",".join(list(map(lambda x: '"'+ x+ '"',values))) + ')'
        sql += values
        self.executer.execute(sql)
        self.conn.commit()

    def select_with_id(self, id : str) -> dict:
        '''
        Overview:
            Read user information by user id
        Parameters:
            id <str>: user id
        Return:
            Formatted dict
        '''
        result = {}
        sql = "select " + ','.join(database_header) + ' from ' + database_table_name
        sql += ' where id = ' + id
        ans = self.conn.execute(sql)
        for row in ans:
            for i, content in enumerate(row):
                result['$' + database_header[i]] = content
        return result

    def get_num(self) -> int:
        '''
        Overview:
            Get the number of users in the table
        '''
        sql = "select count(id) from " + database_table_name
        ans = self.conn.execute(sql)
        for row in ans:
            return int(row[0])
    