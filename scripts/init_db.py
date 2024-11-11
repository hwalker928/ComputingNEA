import sqlite3

connection = sqlite3.connect("data/database.db")

def init():
    with open("schema.sql") as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()

if __name__ == "__main__":
    print("Running database initialization")
    init()
    print("Database initialization complete")