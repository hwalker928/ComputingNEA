import sqlite3
from typing import Any

from utils import log
from scripts import reset_db, init_db


class Database:
    # Constructor
    def __init__(self, db_file: str):
        log.debug(f"Connecting to database {db_file}")

        # Set the class attributes based on the parameters
        self.__db_file = db_file
        # Connect to the database using sqlite3
        self.__conn = sqlite3.connect(db_file, check_same_thread=False)
        # Creating a cursor using the database connection
        self.__cursor = self.__conn.cursor()

        log.debug(f"Connected to database {db_file}")

    # Destructor
    def __del__(self) -> None:
        self.close()

    def is_database_setup(self) -> bool:
        log.debug("Checking if database is setup")

        # Check if the user_details table exists
        query = (
            "SELECT name FROM sqlite_master WHERE type='table' AND name='user_details'"
        )

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
        return self.__cursor

    def query(self, query: str, params: tuple = ()) -> list[Any]:
        log.debug(f"Executing query: {query}")

        # Check if params are being used
        if params != ():
            log.debug(f"Included parameters: {params}")

        # Execute the SQL query
        self.__cursor.execute(query, params)

        self.commit()

        # Return all results from the query
        return self.__cursor.fetchall()

    def commit(self) -> None:
        log.debug("Committing changes to database")

        # Commit the changes to the database
        self.__conn.commit()

    def close(self) -> None:
        log.debug(f"Closing database {self.__db_file}")

        # Close the database connection
        self.__conn.close()

        log.debug(f"Closed database {self.__db_file}")

    def connect(self) -> None:
        log.debug(f"Connecting to database {self.__db_file}")

        # Close the database connection
        self.__conn = sqlite3.connect(self.__db_file, check_same_thread=False)
        self.__cursor = self.__conn.cursor()

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

    def get_all_credentials(self):
        log.debug("Getting all credentials")

        # Query to obtain all credentials
        query = "SELECT * FROM credentials"

        # Execute SQL query
        return self.query(query)

    def update_last_used_at(self, credential_id: int):
        log.debug(f"Updating last_used_at for credential ID {credential_id}")

        # Update the last_used_at column to be the current datetime for the specified credential by ID
        self.query(
            f"UPDATE credentials SET last_used_at = strftime('%Y-%m-%d %H:%M:%S', 'now') WHERE id = '{credential_id}'"
        )
