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


def insert_data(conn, tables):
    ht1 = ("jumper", 5, 5, 10, 0, 50)
    bank = (ht1[5])
    try:
        c = conn.cursor()

        c.execute(tables[0], ht1)
        last_id = c.lastrowid
        c.execute(tables[1], (bank, last_id))
        conn.commit()
        print(f"last id is {last_id}")
    except Error as e:
        print(e)
    """
    loop over the data ex: hotel(...)
    get the last id
    for the bank - hotel id and balance
    """


def main():  # create data and tables
    database = "hotel.db"

#   create_emp = """
#                   INSERT INTO Workers(f_name, l_name, pos)
#                       VALUES("martell","dorsett","cleark")
#               """

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
        tables = [create_hotel, create_bank]
        insert_data(conn, tables)
    else:
        print("Error! cannot create the database connection.")

    print("all done")


if __name__ == '__main__':
    main()
