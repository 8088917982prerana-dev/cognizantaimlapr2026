from models.account import account
class savings_account(account):
    def __init__(self, running_total, open_date, interest_rate):
        super().__init__(running_total, open_date)
        self.interest_rate = interest_rate 