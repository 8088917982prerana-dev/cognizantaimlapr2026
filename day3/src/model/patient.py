import typing
from datetime import date
class patient:
    def __init__(self, name, id, dob, ailment):
        self.name = name
        self.id = id
        self.dob = dob
        self.ailment = ailment
    def __str__(self):
        return f"Patient {self.id}: {self.name}, DOB: {self.dob}, Ailment: {self.ailment}"