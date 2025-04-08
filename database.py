import sqlite3
from contextlib import contextmanager
from config import Config

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(Config.DB_PATH, check_same_thread=False)
        self._create_tables()
    
    def _create_tables(self):
        with self.connection() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS users
                         (user_id INTEGER PRIMARY KEY, 
                          username TEXT,
                          full_name TEXT,
                          balance REAL DEFAULT 0,
                          lang TEXT DEFAULT 'en',
                          referred_by INTEGER,
                          created_at TIMESTAMP)''')
            
            # Create other tables similarly...
    
    @contextmanager
    def connection(self):
        try:
            yield self.conn
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

db = Database()
