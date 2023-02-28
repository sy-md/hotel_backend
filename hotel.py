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
        king = self.king
        queen = self.queen
        genders = ["sir","ma'ma"]
        room = ["King", "Queen"]
        rm = random.choice(room)
        print("Welcome {} which room would you like. one {} size room".format(random.choice(genders), rm))
        if rm == "King":
            return hotel.avaiable(self, rm, king)
        else:
            return hotel.avaiable(self, rm, queen)

    def pay(self, rm, booked=None):
        if self.king <= 1:
            print("sorry no more avaiable")
            profit = 0
            return (profit)
        if self.queen == 1:
            print("sorry no more avaiable")
            profit = 0
            return (profit)


        if booked == "King":
            amount_of_room = (self.king - (self.king - 1))
            profit = (170 * amount_of_room)
            return profit
        if booked == "Queen":
            amount_of_room = (self.queen - (self.queen - 1))
            profit = (150 * amount_of_room)
            return profit


    def avaiable(self, typ, opt=None):
        res = opt - 1
        if res == 0:
            return hotel.pay(self, res, booked=None)
            
        print("{} {} size rooms left".format(res, typ))
        if typ == "King":
            self.king -= 1
        else:
            self.queen -= 1
        return hotel.pay(self, res, booked=typ)

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
