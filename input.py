# This will function as a module that can get all input and output

# Imports
import re
import json
import os

# Global Variables

# Functions
def getMenuNumber(range):
    while True:
        try:
            choice = int(input("Enter a number: "))
            if choice in range:
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
