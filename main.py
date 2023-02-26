from insert import hotel
from sqlite3 import Error
from simulation import bank
import sqlite3

# main.py

def insert_table(conn, tables):
    """
    return hotel update list[tuples]
    return employee list[tuples]

    try to for loop through and send to database

    commit

    """
    ht1 = [("jumper", 5, 5, 10, 0, 50)]
    bank = [(ht1[0][5])]
    try:
        c = conn.cursor()

        for x, ht in enumerate(ht1):
            c.execute(tables[0], ht)
            last_id = c.lastrowid
            c.execute(tables[1], (bank[x],last_id))
            conn.commit()
        print(f"last id is {last_id}")
    except Error as e:
        print(e)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def main():  # create data and tables
    database = "hotel.db"

    create_emp = """
                   INSERT INTO Workers(f_name, l_name, pos)
                       VALUES("martell","dorsett","cleark")
               """

    create_hotel = """
                   INSERT INTO Hotels ("title","king","queen","amount","worker","bnk")
                       VALUES (?,?,?,?,?,?)
               """

    create_bank = """
                   INSERT INTO Bank(balance,hotel_id)
                       VALUES(?,?)
               """

    # create a database connection
    conn = create_connection(database)
    conn.execute("PRAGMA foreign_keys = ON;")

    # create tables
    if conn is not None:
        tables = [create_hotel, create_emp, create_bank]
        insert_table(conn, tables)
    else:
        print("Error! cannot create the database connection.")

    print("all done")


if __name__ == "__main__":

    main()
