# this class is used to create a user object
# it will be used to store and validate user data
import validator

class User:
    def __init__(self, firstName, lastName, email, address, city, state, zipcode, phoneNumber, password):
        self.firstName = None
        self.lastName = None
        self.email = None
        self.address = None
        self.city = None
        self.state = None
        self.zipcode = None
        self.phoneNumber = None
        self.password = None
        self.setFirstName(firstName)
        self.setLastName(lastName)
        self.setEmail(email)
        self.setAddress(address)
        self.setCity(city)
        self.setState(state)
        self.setZipcode(zipcode)
        self.setPhoneNumber(phoneNumber)
        self.setPassword(password)
    
    def setFirstName(self, firstName):
        if validator.validateFirstName(firstName):
            self.firstName = firstName
            return True
        return False
    
    def setLastName(self, lastName):
        if validator.validateLastName(lastName):
            self.lastName = lastName
            return True
        return False
    
    def setEmail(self, email):
        if validator.validateEmail(email):
            self.email = email
            return True
        return False
    
    def setAddress(self, address):
        if validator.validateAddress(address):
            self.address = address
            return True
        return False
    
    def setCity(self, city):
        if validator.validateCity(city):
            self.city = city
            return True
        return False
    
    def setState(self, state):
        if validator.validateState(state):
            self.state = state
            return True
        return False
    
    def setZipcode(self, zipcode):
        if validator.validateZipcode(zipcode):
            self.zipcode = zipcode
            return True
        return False
    
    def setPhoneNumber(self, phoneNumber):
        if validator.validatePhoneNumber(phoneNumber):
            self.phoneNumber = phoneNumber
            return True
        return False
    
    def setPassword(self, password):
        if validator.validatePassword(password):
            self.password = password
            return True
        return False
    
    
    
    