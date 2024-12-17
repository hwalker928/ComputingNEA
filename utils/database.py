import sqlite3
from typing import Any
from utils import log


class Database:
    # Constructor
    def __init__(self, db_file: str):
        log.debug(f"Connecting to database {db_file}")

        # Set the class attributes based on the parameters
        self.db_file = db_file
        # Connect to the database using sqlite3
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        # Creating a cursor using the database connection
        self.cursor = self.conn.cursor()

        log.debug(f"Connected to database {db_file}")

    # Destructor
    def __del__(self) -> None:
        log.debug(f"Closing database {self.db_file}")
        # Close the database connection
        self.conn.close()

    def get_cursor(self) -> sqlite3.Cursor:
        return self.cursor

    def query(self, query: str) -> list[Any]:
        log.debug(f"Executing query: {query}")

        # Execute the SQL query
        self.cursor.execute(query)

        # Return all results from the query
        return self.cursor.fetchall()

    def commit(self) -> None:
        log.debug("Committing changes to database")

        # Commit the changes to the database
        self.conn.commit()

    def close(self) -> None:
        log.debug(f"Closing database {self.db_file}")

        # Close the database connection
        self.conn.close()

    def get_user_detail(self, key: str) -> Any:
        log.debug(f"Getting user details for {key}")

        # Query to obtain value from key
        query = f"SELECT value FROM user_details WHERE key = '{key}'"

        # Execute SQL query
        result = self.query(query)
        
        # Return value if found, else return None
        return result[0][0] if result else None

    def set_user_detail(self, key: str, value: Any) -> None:
        log.debug(f"Setting user details for {key}")

        # Query to insert or update the key-value pair
        query = f"INSERT OR REPLACE INTO user_details (key, value) VALUES ('{key}', '{value}')"

        # Execute SQL query
        self.query(query)

        # Commit the changes to the database
        self.commit()
