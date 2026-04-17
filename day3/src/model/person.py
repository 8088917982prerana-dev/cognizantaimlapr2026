"""
person model
"""
import re
class person:
    """
    a class to represent a person with a name and age
    """
    def __init__(self, aadhar_number: int, mobile_no: int):
        self.__aadhar_number = aadhar_number
        self.__mobile_no = mobile_no

    @property
    def aadhar_number(self):
        return self.__aadhar_number

    @property
    def mobile_no(self):
        return self.__mobile_no

    @mobile_no.setter
    def mobile_no(self, new_mobile_no):
        if not re.match(r'\d{10}', str(new_mobile_no)):
            raise ValueError("Mobile number must be a 10-digit number")
        self.__mobile_no = new_mobile_no

    def update_mobile_no(self, new_mobile_no):
        """
        update mobile number
        """
        self.mobile_no = new_mobile_no