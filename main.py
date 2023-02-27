from sqlite3 import Error
from bank import bank
import setup_hotel_app
from hotel import hotel
import sqlite3


def insert_table(conn, data, tables):
    try:
        c = conn.cursor()
        (hotel_data, bank_data ) = data

        c.execute(tables[0], hotel_data)
        last_id = c.lastrowid
        c.execute(tables[2], (bank_data, last_id))
        conn.commit()
       #print(f"last id is {last_id}")
    except Error as e:
        print("eror",e)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def main():  # create data and tables
    conn = setup_hotel_app.make_db()

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
    #conn = create_connection(database)
    conn.execute("PRAGMA foreign_keys = ON;")

    # create tables
    if conn is not None:
        tables = [create_hotel, create_emp, create_bank]

        hotel_title = "jumper"

        my_hotel = hotel(title=hotel_title, operation=tables[0])
        b = bank(balance=my_hotel.account(), operation=tables[2])

        hotel_data = my_hotel.get_report()
        bank_data = b.get_statement()

        data = tuple((hotel_data,bank_data))

        insert_table(conn, data, tables)
    else:
        print("Error! cannot create the database connection.")

    print("all done")


if __name__ == "__main__":
    main()
