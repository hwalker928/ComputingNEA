import sqlite3
from typing import Any
from utils import log

class Database:
    # Constructor
    def __init__(self, db_file: str):
        log.debug(f"Connecting to database {db_file}")
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        log.debug(f"Connected to database {db_file}")

    # Destructor
    def __del__(self) -> None:
        log.debug(f"Closing database {self.db_file}")
        self.conn.close()

    def get_cursor(self) -> sqlite3.Cursor:
        return self.cursor

    def query(self, query: str) -> list[Any]:
        log.debug(f"Executing query: {query}")
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def commit(self) -> None:
        log.debug("Committing changes to database")
        self.conn.commit()

    def close(self) -> None:
        log.debug(f"Closing database {self.db_file}")
        self.conn.close()
    
    