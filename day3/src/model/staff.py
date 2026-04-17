"""
create class staff  
"""
from src.model.person import person
class staff(Person):# we are doing inheritance
    """
    staff class inherits from person class and associated to role
    """
    def __init__(self, aadhar_number, mobile_no, role):
        super().__init__(aadhar_number, mobile_no)
        self.__role = role # we are doing association
    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, new_role):
        self.__role = new_role
