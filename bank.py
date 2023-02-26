from insert import hotel


class bank:

    def __init__(self, balance, hotel_id, operation = None):
        self.money = balance
        self.id = hotel_id

    def earn_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(self.balance())

    def data_connection(self):
        pass
