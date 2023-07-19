# Jake Malmrose
# This will be a command line interface program
# Needs to manage users, using basic CRUD operations
# Input will be validated via regex
# If any input is bad, simply inform user which fields are invalid, and don't do the operation
# User data will be persisted to json file

import input
import validator

def run():
    while True:
        choice = input.getMainMenu()
        if choice == 1:
            createUser()
        elif choice == 2:
            readUser()
        elif choice == 3:
            updateUser()
        elif choice == 4:
            deleteUser()
        elif choice == 5:
            exit()
        else:
            print("Please enter a valid number.")

def createUser():
    personAttributes = input.getCreateUserMenu()
    

def readUser():
    pass

def updateUser():
    pass

def deleteUser():
    pass



if __name__ == "__main__":
    run()