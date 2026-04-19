from models.transaction import transaction
class externaltransaction(transaction):
    def __init__(self, amount, date, sender, receiver, branch_name, branch_address, branch_post_code, branch_code):
        super().__init__(amount, date, sender, receiver)
        self.branch_name = branch_name
        self.branch_address = branch_address
        self.branch_post_code = branch_post_code
        self.branch_code = branch_code