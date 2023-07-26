# Jake Malmrose
# This needs a full rewrite. I apologize.
# Needs to manage users, using basic CRUD operations
# Input will be validated via regex
# If any input is bad, simply inform user which fields are invalid, and don't do the operation
# User data will be persisted to json file

import input
import validator
import user as user
import database as database

def run():
    database.__init__()
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
    print("Making a new user!")
    personAttributes = input.getCreateUserMenu()
    if not database.createUser(personAttributes):
        print("Invalid input for " + personAttributes["invalidInput"] + ". Please try again.")
    else:
        print(personAttributes["firstName"] + " created successfully!")
        

def readUser():
    tempInput = input.getSearchUser()
    if database.findUser(tempInput):
        print("User found!")
        user = database.findUser(tempInput)
        print("First Name: " + user["firstName"])
        print("Last Name: " + user["lastName"])
        print("Email: " + user["email"])
        print("Address: " + user["address"])
        print("City: " + user["city"])
        print("State: " + user["state"])
        print("Zipcode: " + user["zipcode"])
        print("Phone Number: " + user["phoneNumber"])
        print("Password :O : " + user["password"])
    else:
        print("User not found.")

def updateUser():
    userToUpdate = database.findUser(input.getSearchUser())
    if userToUpdate:
        print("User found, updating!")
        print("Enter new user information:")
        database.updateUser(userToUpdate, input.getCreateUserMenu())
    else:
        print("User not found. Nothing to update.")

def deleteUser():
    if database.deleteUser(input.getSearchUser()):
        print("User found, deleting!")
    else:
        print("User not found. Nothing to delete.")

def saveDatabase():
    database.saveDatabase()
    print("Database saved successfully!")



if __name__ == "__main__":
    run()