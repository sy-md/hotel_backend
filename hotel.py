import random


class hotel:

    def __init__(self, title, king=10, queen=10, amount=None, worker=0, operation=None):
        self.title = title
        self.king = king
        self.queen = queen
        self.amount = (self.king + self.queen)
        self.workers = worker
        self.operation = operation

    def booking(self):
        genders = ["sir","ma'ma"]
        room = ["King", "Queen"]
        rm = random.choice(room)
        print("Welcome {} which room would you like. one {} size room".format(random.choice(genders), rm))

        if rm == "King":
            res = self.king - 1
            print("{} king size room left".format(self.king))
            return hotel.pay(self, res, booked="King")
        else:
            res = self.queen - 1
            print("{} queen size room left".format(self.queen))
            return hotel.pay(self, res, booked="Queen")

    def pay(self, rm, booked=None):

        if booked == "King":
            price = (170 * (self.king - rm))
            profit = price
        if booked == "Queen":
            amount_of_room = (self.queen - rm)
            price = (150 * amount_of_room)
            profit = price

        return (profit)

    def avaiable(self):
        return self.amount

    def paycheck(self):
        monthly = 8500
        return monthly

    def get_report(self) -> tuple:
        return (
                self.title,
                self.king,
                self.queen,
                self.amount,
                self.workers
            )
