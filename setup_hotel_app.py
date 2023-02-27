import sqlite3
from sqlite3 import Error
 


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def make_db():  # create data and tables
    database = "hotel.db"

    create_hotels = """ CREATE TABLE IF NOT EXISTS Hotels (
                            hotel_id INTEGER PRIMARY KEY,
                            title TEXT,
                            king INTEGER,
                            queen INTEGER,
                            amount INTEGER,
                            worker INTEGER,
                            bnk NUMERIC
                        );"""
    print("hotel table made")
    create_employees = """ CREATE TABLE IF NOT EXISTS Workers (
                           id INT PRIMARY KEY,
                           name TEXT,
                           pos TEXT,
                           salary INT,
                           worker INT,
                           FOREIGN KEY(worker) REFERENCES Hotels(worker)
                       );"""
    print("emp table made")
    create_bank = """ CREATE TABLE IF NOT EXISTS Bank (
                            id INTEGER PRIMARY KEY,
                            balance NUMERIC,
                            hotel_id INTEGER,
                            FOREIGN KEY(hotel_id) REFERENCES Hotels(hotel_id)
                        );"""
    print("bank table made")

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        my_tables = [create_bank, create_hotels, create_employees]
        for table in my_tables:
            create_table(conn, table)
    else:
        print("Error! cannot create the database connection.")

    return conn
