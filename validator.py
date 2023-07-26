# This stores all of our regex validation strings and has methods
# to validate input. This will be imported by user.py

import re

regexes = {
    "firstName": "^[a-zA-Z]{2,50}$",
    "lastName": "^[a-zA-Z]{2,50}$",
    "email": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    "address": "^[a-zA-Z0-9 ]{2,50}$",
    "city": "^[a-zA-Z]{2,50}$",
    "state": "^[a-zA-Z]{2}$",
    "zipcode": "^[0-9]{5}$",
    "phoneNumber": "^1?\\(?\\d{3}\\)?[- ]?\\d{3}[- ]?\\d{4}$",
    "password": "^(?=.*[A-Z])(?=.*\\d)(?=.*[!@#$%^&*()\\[\\]{};:'\"<>,./?]).{8,}$"
}

def validateInput(input, regex):
    if re.match(regex, input, re.IGNORECASE):
        return True
    else:
        return False

def findInvalidInput(personAttributes):
    for key in personAttributes:
        if not validateInput(personAttributes[key], regexes[key]):
            return key
    return True
    
# PersonAttributes have been validated all together due to assignment
# requirements. It would probably be preferable to check as it's inputted
def validatePersonAttributes(personAttributes): 
    for key in personAttributes:
        if not validateInput(personAttributes[key], regexes[key]):
            return False, regexes[key]
    return True

def validatePassword(password):
    return validateInput(password, regexes["password"])