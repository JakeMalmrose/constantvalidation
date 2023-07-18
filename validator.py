# This stores all of our regex validation strings and has methods
# to validate input. This will be imported by main.py

import re

regexes = {
    
}

def validateInput(input, regex):
    if re.match(regex, input):
        return True
    else:
        return False

def validateFirstName(firstName):
    return validateInput(firstName, regexes["firstName"])

def validateLastName(lastName):
    return validateInput(lastName, regexes["lastName"])

def validateEmail(email):
    return validateInput(email, regexes["email"])

def validateAddress(address):
    return validateInput(address, regexes["address"])

def validateCity(city):
    return validateInput(city, regexes["city"])

def validateState(state):
    return validateInput(state, regexes["state"])

def validateZipcode(zipcode):
    return validateInput(zipcode, regexes["zipcode"])

def validatePhoneNumber(phoneNumber):
    return validateInput(phoneNumber, regexes["phoneNumber"])

def validatePassword(password):
    return validateInput(password, regexes["password"])