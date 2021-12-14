import sqlite3
from SerWise.API.analyzer import contain_analyzer
from SerWise.setting import database_path, database_header, database_table_name
from SerWise.util.logger import get_core_logger

class userDatabase:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(database_path)
        self.executer = self.conn.cursor()
        header = ' '.join(list(map(lambda x : x+" string,", database_header)))[:-1]
        sql = 'create table if not exists ' + database_table_name + \
              '(' + header + ')'
        self.executer.execute(sql)

    def result_save(self, table_name : str, dict : dict):
        header = ' '.join(list(map(lambda x : x[1:]+" string,", dict.keys())))[:-1]
        sql = 'drop table if exists ' + table_name
        self.executer.execute(sql)

        sql = 'create table ' + table_name + \
              '(' + header + ')'
        self.executer.execute(sql)
        print(sql)

        self.conn.commit()
        sql = "insert into " + table_name  + ' values '
        values = '(' +  ",".join(list(map(lambda x: '"'+ str(x)+ '"',dict.values()))) + ')'
        sql += values
        self.executer.execute(sql)

        self.conn.commit()

    def insert_value(self, values) -> None:
        sql = "insert into " + database_table_name  + ' values '
        values = '(' +  ",".join(list(map(lambda x: '"'+ x+ '"',values))) + ')'
        sql += values
        self.executer.execute(sql)
        self.conn.commit()

    def select_with_id(self, id : str) -> dict:
        result = {}
        sql = "select " + ','.join(database_header) + ' from ' + database_table_name
        sql += ' where id = ' + id
        ans = self.conn.execute(sql)
        for row in ans:
            for i, content in enumerate(row):
                result['$' + database_header[i]] = content
        return result