from models.menu import menu
from models.individual import individual
def test_add_customer():
    m = menu()
    ind = individual(name = "John", address = "123 Main St", phone_number = "555-1234", email = "john@example.com", account_number = "12345678", password = "password", date_of_birth = "01/01/1990", surname = "Smith", gender = "Male")
    m.add_customer(ind)
    assert len(m.customer_list) == 1