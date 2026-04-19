from models.customer import customer
class individual(customer):
    def __init__(self, name, address, phone_number, email, account_number, password, date_of_birth, surname, gender):
        super().__init__(name, address, phone_number, email, account_number, password)
        self.date_of_birth = date_of_birth
        self.surname = surname
        self.gender = gender
    def work_out_age(self):
        print("calculated age")
