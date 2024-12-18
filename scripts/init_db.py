import sqlite3


def init():
    connection = sqlite3.connect("data/database.db")

    with open("schema.sql") as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()


if __name__ == "__main__":
    print("Running database initialization")
    init()
    print("Database initialization complete")
