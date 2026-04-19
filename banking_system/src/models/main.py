from saving_account import saving_account
from current_account import current_account
from abc_banking_group import ABCBankingGroup
from corporate import corporate
from individual import individual
from menu import menu
sa = Saving_account(running_total = 1000, opening_date = "01/01/2020", interest_rate = 0.05)
ca = Current_account(running_total = 2000, opening_date = "01/02/2020", overdraft_limit = 500)
ind = individual(name = "John", address = "123 Main St", phone_number = "555-1234", email = "john@example.com", account_number = "12345678", password = "password", date_of_birth = "01/01/1990", surname = "Smith", gender = "Male")
corp = corporate(name = "ABC Corp", address = "456 Corporate Blvd", phone_number = "555-5678", email = "corp@example.com", account_number = "87654321", password = "password", company_type = "LLC")
#aggregation
menu = menu()
menu.add_customer(ind)
menu.add_customer(corp)
#association
bank= ABCBankingGroup()
bank.add_account(sa)
bank.add_account(ca)
print("project executed successfully")