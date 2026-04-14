import faker
import typing
from models.customer import Customer

class CustomerStore:
    def __init__(self, num_customers: int):
        self.customers = []
        self.generate_customers(num_customers)

    def generate_customers(self, num_customers: int):
        fake = faker.Faker()
        for _ in range(num_customers):
            name = fake.name()
            dob = fake.date_of_birth()
            email = fake.email()
            customer = Customer(name, dob, email)
            self.customers.append(customer)

    def get_all_customers(self) -> typing.List[Customer]:
        return self.customers