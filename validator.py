# This stores all of our regex validation strings and has methods
# to validate input. This will be imported by user.py

import re

regexes = {
    "firstName": "^[a-zA-Z]+{2}$",
    "lastName": "^[a-zA-Z]{2,50}$"
}

def validateInput(input, regex):
    if re.match(regex, input):
        return True
    else:
        return False
    
def validatePersonAttributes(personAttributes):
    for key in personAttributes:
        if not validateInput(personAttributes[key], regexes[key]):
            return False
    return True

def validatePassword(password):
    return validateInput(password, regexes["password"])