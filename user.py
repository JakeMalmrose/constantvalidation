# this class is used to create a user object
# it will be used to store user data
# A user will have the following fields:
# First Name, Last Name, Email, Address, City, State, Zipcode, Phone Number and Password

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
    
    