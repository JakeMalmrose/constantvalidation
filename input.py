# This will function as a module that can get all input from the user

# Imports
import re
import json
import os

# Global Variables

# Functions
def getMenuNumber(max):
    while True:
        try:
            choice = int(input("Enter a number: "))
            if choice > 0 and choice <= max:
                return choice
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def getRegexInput(prompt, regex):
    userInput = input(prompt)
    if re.match(regex, userInput):
        return userInput
    else:
        return False

def getUserInput(prompt):
    return input(prompt)

def getMainMenu():
    print("Welcome to the user manager!")
    print("1. Create a user")
    print("2. Read a user")
    print("3. Update a user")
    print("4. Delete a user")
    print("5. Exit")
    return getMenuNumber(5)

def getCreateUserMenu():
    print("Making a new user!")
    firstName = input("Enter user's first name: ")
    lastName = input("Enter user's last name: ")
    email = input("Enter user's email: ")
    address = input("Enter user's address: ")
    city = input("Enter user's city: ")
    state = input("Enter user's state: ")
    zipcode = input("Enter user's zipcode: ")
    phoneNumber = input("Enter user's phone number: ")
    password = input("Enter user's password: ")
    return {
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "address": address,
        "city": city,
        "state": state,
        "zipcode": zipcode,
        "phoneNumber": phoneNumber,
        "password": password
    }


