class transaction:
    def __init__(self, amount, date, sender, receiver):
        self.amount = amount
        self.date = date
        self.sender = sender
        self.receiver = receiver
    def deposit_money(self):
        print("depositing money")
    def withdraw_money(self):
        print("withdrawing money")