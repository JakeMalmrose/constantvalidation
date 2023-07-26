# this class is used to create a user object
# it will be used to store and validate user data
from typing import Any
import validator

class User:
    def __init__(self, firstName, lastName, email, address, city, state, zipcode, phoneNumber, password, id):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phoneNumber = phoneNumber
        self.password = password
        self.id = id
    
    def getUserJson(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "phoneNumber": self.phoneNumber,
            "password": self.password,
            "id": self.id
        }
    
    def __getitem__(self, __name):
        return self.getUserJson()[__name]
    
    def __setitem__(self, name, value):
        self.__name = value

def createUser(attributes, id):
        if validator.validatePersonAttributes(attributes):
            return User(attributes["firstName"], attributes["lastName"], attributes["email"], attributes["address"], attributes["city"], attributes["state"], attributes["zipcode"], attributes["phoneNumber"], attributes["password"], id)
        else:
            return validator.findInvalidInput(attributes)
        
    
            


    
    
    
    