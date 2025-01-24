import sqlite3
from typing import Any

from utils import log
from scripts import reset_db, init_db


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
        self.close()

    def is_database_setup(self) -> bool:
        log.debug("Checking if database is setup")

        # Check if the user_details table exists
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='user_details'"

        # Execute the SQL query
        result = self.query(query)

        # Return True if the table exists, else return False
        return True if result else False

    def setup_database(self) -> None:
        log.debug("Setting up database")

        # Close the database connection
        self.close()

        # Reset the database
        reset_db.reset()

        # Initialize the database
        init_db.init()

        # Reconnect to the new database
        self.connect()

        log.debug("Database setup complete")

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

        log.debug(f"Closed database {self.db_file}")

    def connect(self) -> None:
        log.debug(f"Connecting to database {self.db_file}")

        # Close the database connection
        self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

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
