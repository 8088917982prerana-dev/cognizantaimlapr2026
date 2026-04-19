from models.customer import customer
class corporate(customer):
    def __init__(self, name, address, phone_number, email, account_number, password, company_type):
        super().__init__(name, address, phone_number, email, account_number, password)
        self.company_type = company_type