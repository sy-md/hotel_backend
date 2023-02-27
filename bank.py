import hotel 

class bank():

    def __init__(self, balance=10000, hotel_id=None, operation=None):
        self.balance = balance
        self.hotel_id = hotel_id

    def earn_money(self, amount):
        return self.balance + amount

    def withdraw_money(self, amount):
        self.balance -= amount

    def show_balance(self):
        return self.balance

    def get_statement(self) -> tuple:
        return (self.balance)
