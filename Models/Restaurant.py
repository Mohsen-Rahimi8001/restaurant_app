import json
import re
from Constants.RegExValidations import Patterns


class Restaurant():
    """Restaurant class"""
    
    def __init__(self, restaurantName:str, managerName:str,
     managerEmail:str, type:str, description:str, phone:str, region:str, address:str) -> None:
        self.restaurantName = restaurantName
        self.managerName = managerName
        self.managerEmail = managerEmail
        self.type = type
        self.description = description
        self.phone = phone
        self.region = region
        self.address = address

    @property
    def restaurantName(self):
        return self._restaurantName
    
    @restaurantName.setter
    def restaurantName(self, value:str):
        if not isinstance(value, str):
            raise TypeError("restaurantName must be a string")
        self._restaurantName = value

    @property
    def managerName(self) -> str:
        return self._managerName
    
    @managerName.setter
    def managerName(self, managerName) -> None:
        if not isinstance(managerName, str):
            raise TypeError("managerName must be a User")
        self._managerName = managerName

    @property
    def managerEmail(self):
        return self._managerEmail

    @managerEmail.setter
    def managerEmail(self, managerEmail):
        if not isinstance(managerEmail, str):
            raise TypeError("managerEmail must be a string")
        
        if not re.match(Patterns.EMAIL.value, managerEmail):
            raise ValueError("managerEmail must be a valid email address")
        
        self._managerEmail = managerEmail

    @property
    def type(self) -> str:
        return self._type
    
    @type.setter
    def type(self, type:str) -> None:
        if not isinstance(type, str):
            raise TypeError("type must be a string")
        self._type = type

    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, description:str) -> None:
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        self._description = description

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone:str) -> None:
        if re.match(Patterns.PHONE.value, phone):
            self._phone = phone
        else:
            raise ValueError("phone must be a valid phone number")

    @property
    def region(self) -> str:
        return self._region
    
    @region.setter
    def region(self, region:str) -> None:
        if not isinstance(region, str):
            raise TypeError("region must be a string")
        self._region = region

    @property
    def address(self) -> str:
        return self._address
    
    @address.setter
    def address(self, address:str) -> None:
        if not isinstance(address, str):
            raise TypeError("address must be a string")
        self._address = address

    @staticmethod
    def GetJsonAddress() -> str:
        """returns the path to the json file"""
        return r".\Constants\Restaurant.json"

    def SaveToJson(self) -> None:
        """save restaurant object to json file"""
        with open(Restaurant.GetJsonAddress(), "w") as file:
            json.dump(self.__dict__, file, indent=4)

    @classmethod
    def LoadFromJson(cls) -> 'Restaurant':
        """load restaurant from json file"""
        with open(Restaurant.GetJsonAddress(), "r") as file:
            # create a Restaurant object from json file
            return cls(*json.load(file).values())
