#!/usr/bin/env python3
import argparse, sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")




def dbmake(tname, key1, key2, key3, key4):
    conn.execute(f'''CREATE TABLE IF NOT EXISTS {.upper(tname)}
     (ID INT PRIMARY KEY     NOT NULL,
    {.upper(key1)}           TEXT    NOT NULL,
    {.upper(key2)}            INT     NOT NULL,
    {.upper(key3)}         CHAR(50),
    {.upper(key4)}         REAL);''')
    print("Table created successfully")
    conn.close()


def newdb():
    # if user sent a POST
    if request.method == "POST":
        tname = request.form["tname"]
        key1 = request.form["key1"]
        key2 = request.form["key2"]
        key3 = request.form["key3"]
        key4 = request.form["key4"]


