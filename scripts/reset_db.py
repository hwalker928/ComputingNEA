import sqlite3, os


def reset():
    os.remove("data/database.db")

    connection = sqlite3.connect("data/database.db")

    with open("schema.sql") as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()


if __name__ == "__main__":
    print("Running database reset")
    reset()
    print("Database reset complete")
