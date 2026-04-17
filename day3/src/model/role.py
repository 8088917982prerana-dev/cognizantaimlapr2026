"""
role model
"""
class role:
    """
    a class to represent a role with a name and description
    """
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description
    # setter for description
    @description.setter
    def update_description(self, new_description):
        """update description
        """
        self.__description = new_description    
