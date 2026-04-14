#define customer model
import datetime
class Customer:
    def __init__(self, name: str, dob: datetime.date, email: str):
        self.name = name
        self.dob = dob
        self.email = email

    def __str__(self):
        return f"Customer(name={self.name}, dob={self.dob}, email={self.email})"