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

        my_hotel = hotel(title="jumper", king=10, queen=10, amount=(20), title=hotel_title, operation=tables[0])
        b = bank(operation=tables[2])
        """
        setting the database for the first hotel and bank
            * this can be a function 
         
        hotel_data = my_hotel.get_report() #getting the first report
        avaiable = hotel.avaiable(my_hotel) #checking for rooms
        bank_data = b.get_statement() # getting the statment from the bank
        
        data = tuple((hotel_data, bank_data)) # i think i should add avaiable
        """
        
        """def setupdatabe(conn, data, tables )""" #send data to get processed
        insert_table(conn, data, tables) # get rid of this line of code and relpace with setupdatabase()
        
        # exit()  #uncomment to just test database connection 
        while True: # life
            """
            1.) have guess check in the hotel
            2.) do we have any room avaiable
                
            
            def func():
                x = "king"
                if x == "queen":
                    print("here u go")
                else:
                    print("no queen sorry")
                    return test(x)
            
            def test(x):
                print(x)
                return x

            while True:
                for x in range(1):
                    profit = func()
                    print("back in while loop")
                    print(profit)
                break

            > no queen sorry
            > back in while loop
            
            
    
                
    
            """
            for _ in range(5): # 20 days for :eon month 
                monthly_profit = 0
                time.sleep(0.8) 
                re = hotel.booking(my_hotel)
                monthly_profit += re
                ava = hotel.avaiable(my_hotel)
                print(ava)
                if ava <= 0:
                    break
                time.sleep(0.5)
                print("profit of the month - ", re)

                bank_data = (bank_data + monthly_profit)
                update_table(conn, bank_data, updates)
                mnthly = hotel.paycheck(my_hotel)
                print("monthly pay $", mnthly)
                bank.withdraw_money(b, mnthly)
            
    else:
        print("Error! cannot create the database connection.")

    print("all done")


if __name__ == "__main__":
    main()
