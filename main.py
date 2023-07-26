# Jake Malmrose
# This will be a command line interface program
# Needs to manage users, using basic CRUD operations
# Input will be validated via regex
# If any input is bad, simply inform user which fields are invalid, and don't do the operation
# User data will be persisted to json file

import input
import validator
import user as user
import database as database

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
            saveDatabase()
            exit()
        else:
            print("Please enter a valid number.")

def createUser():
    personAttributes = input.getCreateUserMenu()
    if not database.createUser(personAttributes):
        print("Invalid input for " + personAttributes["invalidInput"] + ". Please try again.")
    else:
        print(personAttributes["firstName"] + " created successfully!")
        

def readUser():
    if database.findUser(input.getSearchUser()):
        print("User found!")
    else:
        print("User not found.")

def updateUser():
    if database.findUser(input.getSearchUser()):
        print("User found, updating!")
        database.updateUser(input.getSearchUser())
    else:
        print("User not found. Nothing to update.")

def deleteUser():
    if database.deleteUser(input.getSearchUser()):
        print("User found, deleting!")
    else:
        print("User not found. Nothing to delete.")

def saveDatabase():
    database.saveDatabase()



if __name__ == "__main__":
    run()