# creating entry point for the application
import faker
from store.customerstore import CustomerStore
from view.customerview import CustomerView
"""
creating entry point for the application
"""


def check():
    """
    this function creates an instance of the faker class and prints random names
    """
    customer_store = CustomerStore(100)
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()


if __name__ == "__main__":
    check()
