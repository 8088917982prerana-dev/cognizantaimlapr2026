class menu:
    def __init__(self):
        self.transaction_list = []
        self.customer_account_list = []
        self.customer_list = []
    def initiate_transaction(self):
        print("initiating transaction")
    def add_customer(self, customer):
        self.customer_list.append(customer)
    def delete_customer(self, customer):
        self.customer_list.remove(customer)
    def login(self):
        print("logging in")
    def logout(self):
        print("logging out")

