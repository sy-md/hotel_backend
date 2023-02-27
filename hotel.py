class hotel:

    def __init__(self, title, king=5, queen=5, amount=None, worker=0, bnk=1_000_000, operation=None):
        self.title = title
        self.king = king
        self.queen = queen
        self.amount = (self.king + self.queen)
        self.workers = worker
        self.bank = bnk
        self.operation = operation

    def booking(self):
        """
        take away from quue or king
        every couple of mins

        run pay
        """
    def pay(self):
        """
        from the the booking they will have to pay
        """

    def account(self):
        return self.bank
        """
        sunbtract money to sim asalry of such
        """
    def get_report(self) -> tuple: 
        return (
                self.title,
                self.king,
                self.queen,
                self.amount,
                self.workers,
                self.bank
            )
