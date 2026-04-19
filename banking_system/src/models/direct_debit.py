from models.transaction import transaction
class direct_debit(transaction):
    def __init__(self, amount, date, sender, receiver, payment_date):
        self.amount = amount
        self.date = date
        self.sender = sender
        self.receiver = receiver
        self.payment_date = payment_date