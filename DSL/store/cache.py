import sqlite3
from DSL.setting import database_path


class varibleTable:
    def __init__(self) -> None:
        self.conn = sqlite3(database_path)
        self.conn.execute(" CREATE TABLE IF NOT EXISTS USER\
                            (NAME TEXT,  \
                            AGE INT,\
                            SALARY REAL)")