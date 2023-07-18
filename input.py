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
