from models.account import account
class current_account(account):
    def __init__(self, running_total, open_date, overdraft_limit):
        super().__init__(running_total, open_date)
        self.overdraft_limit = overdraft_limit