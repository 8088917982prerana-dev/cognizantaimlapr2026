class customer:
    def __init__(self, name, address, phone_number, email, account_number, password):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.account_number = account_number
        self.password = password
    def total_number_of_transactions(self):
        print("total customer counted")