#!/usr/bin/python3

import random
import time
import datetime
import sqlite3

conn = sqlite3.connect('movies.db')

c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS movies(unix REAL, title TEXT, description TEXT, image BLOB, totallikes REAL)")

def data_entry():
    unix = int(time.time())
    title = "Star Wars"
    description = "Den är najzzz"
    totallikes = random.randrange(0,10)

    c.execute("INSERT INTO movies (unix, title, description, totallikes) VALUES(?,?,?,?)",
        (unix, title, description, totallikes))

    conn.commit()
    time.sleep(1)

def read_from_db():
    c.execute("SELECT * FROM movies")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

def readall():
    c.execute("SELECT title FROM movies")
    return c.fetchall()

def add_movie(title,description,likes):
    unix = int(time.time())
    c.execute("INSERT INTO movies (unix, title, description, totallikes) VALUES(?,?,?,?)", (unix,title,description,likes))


if __name__ == "__main__":
    # create_table()
    # for i in range(10):
    #     data_entry()
    read_from_db()

