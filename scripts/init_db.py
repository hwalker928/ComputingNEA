import sqlite3
import os

os.chdir('..')

# Connect to the database
connection = sqlite3.connect("data/database.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

connection.commit()
connection.close()
