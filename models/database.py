import sqlite3
from sqlite3 import Error

class DB:
    def __init__(self):
        """ create a database connection to a SQLite database """

        self.init_tables()

        self.conn = sqlite3.connect(r"C:\Users\spilk\Documents\ScrimsBot\user.db")
        self.conn.row_factory = self.dict_factory
        self.cursor = self.conn.cursor()
        print(sqlite3.version)
    
    def __del__(self):
        self.conn.close()

    def get_conn(self):
        return self.conn
    
    def get_cursor(self):
        return self.cursor

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def init_tables(self):
        conn = sqlite3.connect(r"C:\Users\spilk\Documents\ScrimsBot\user.db")
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scrims
            (scrim_id INTEGER PRIMARY KEY, scrim_name TEXT UNIQUE, host_id INTEGER)
            ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players
            (player_id INTEGER PRIMARY KEY, scrim_id INTEGER, player_name TEXT,FOREIGN KEY(scrim_id) REFERENCES scrims(scrim_id) ON DELETE CASCADE)
            ''')
        # BS cause it doesn't work
        cursor.execute("PRAGMA foreign_keys=ON");
        conn.commit()
        cursor.close()
        conn.close()

    
