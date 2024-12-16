import sqlite3, os


def reset():
    if os.path.exists("data/database.db"):
        os.remove("data/database.db")
    if os.path.exists("keys/private.key"):
        os.remove("keys/private.key")
    if os.path.exists("keys/public.key"):
        os.remove("keys/public.key")

    connection = sqlite3.connect("data/database.db")

    with open("schema.sql") as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()


if __name__ == "__main__":
    print("Running database reset")
    reset()
    print("Database reset complete")
