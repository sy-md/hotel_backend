from sqlite3 import Error
from bank import bank
import setup_hotel_app
from hotel import hotel
import sqlite3
import time


def insert_table(conn, data, tables):
    try:
        c = conn.cursor()
        (hotel_data, bank_data) = data

        c.execute(tables[0], hotel_data)
        last_id = c.lastrowid
        c.execute(tables[2], (bank_data, last_id))
        conn.commit()
    except Error as e:
        print("eror", e)


def update_table(conn, data, updates):
    try:
        c = conn.cursor()
        c.execute(updates[0], (data, 1))
        conn.commit()
    except Error as e:
        print("eror", e)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def main():  # create data and tables
    # create a database connection
    conn = setup_hotel_app.make_db()
    conn.execute("PRAGMA foreign_keys = ON;")

    create_emp = """
                   INSERT INTO Workers(f_name, l_name, pos)
                       VALUES("martell","dorsett","cleark")
               """

    create_hotel = """
                   INSERT INTO Hotels ("title","king","queen","amount","worker")
                       VALUES (?,?,?,?,?)
               """

    create_bank = """  INSERT INTO Bank(balance,hotel_id) VALUES(?,?) """

    update_bank = """ UPDATE Bank SET balance = ? WHERE id = ? """
    # create tables
    if conn is not None:

        tables = [create_hotel, create_emp, create_bank]

        updates = [update_bank]

        hotel_title = "jumper"  # user title hotel

        my_hotel = hotel(title=hotel_title, operation=tables[0])
        b = bank(operation=tables[2])
        hotel_data = my_hotel.get_report()
        avaiable = hotel.avaiable(my_hotel)
        bank_data = b.get_statement()
        data = tuple((hotel_data, bank_data))
        insert_table(conn, data, tables)
        # exit()
        while avaiable != 0:
            tmp = 0
            for _ in range(5):
                time.sleep(2)
                re = hotel.booking(my_hotel)
                tmp += re
            time.sleep(5)
            print("profit of the day - ", tmp)

            bank_data = (bank_data + tmp)
            update_table(conn, bank_data, updates)

            
    else:
        print("Error! cannot create the database connection.")

    print("all done")


if __name__ == "__main__":
    main()
