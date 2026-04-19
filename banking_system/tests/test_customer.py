from models.individual import individual
from models.corporate import corporate
def test_individual():
    ind = individual(name = "John", address = "123 Main St", phone_number = "555-1234", email = "john@example.com", account_number = "12345678", password = "password", date_of_birth = "01/01/1990", surname = "Smith", gender = "Male")
    assert ind.name == "John"
    assert ind.gender == "Male"
def test_corporate():
    corp = corporate(name = "ABC Corp", address = "456 Corporate Blvd", phone_number = "555-5678", email = "corp@example.com", account_number = "87654321", password = "password", company_type = "LLC")
    assert corp.name == "ABC Corp"
    assert corp.company_type == "LLC"