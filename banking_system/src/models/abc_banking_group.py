class ABCBankingGroup:
    def __init__(self):
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)