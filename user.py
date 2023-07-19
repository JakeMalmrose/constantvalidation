# this class is used to create a user object
# it will be used to store and validate user data
import validator

class User:
    def __init__(self, firstName, lastName, email, address, city, state, zipcode, phoneNumber, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phoneNumber = phoneNumber
        self.password = password


    
    
    
    