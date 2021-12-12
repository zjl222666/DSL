import sqlite3
from DSL.API.analyzer import contain_analyzer
from DSL.setting import database_path, database_header, database_table_name
from DSL.util.logger import get_core_logger

class userDatabase:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(database_path)
        self.executer = self.conn.cursor()
        header = ' '.join(list(map(lambda x : x+" string,", database_header)))[:-1]
        sql = 'create table if not exists ' + database_table_name + \
              '(' + header + ')'
        self.executer.execute(sql)

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
                result[database_header[i]] = content
        return result