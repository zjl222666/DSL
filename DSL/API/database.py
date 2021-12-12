import sqlite3
from DSL.setting import database_path

class userDatabase:
    def __init__(self) -> None:
        self.path = database_path
        