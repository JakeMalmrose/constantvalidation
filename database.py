import user
import json
import os
import validator

people = []

def __init__():
    loadDatabase()

def __del__():
    saveDatabase()

def loadDatabase():
    global highestIndex
    dir = os.listdir("database")
    for file in dir:
        if file.endswith(".json"):
            with open("database/" + file, "r") as f:
                people.append(json.load(f))
                

def saveDatabase():
    for person in people:
        with open("database/" + person.id + ".json", "w") as f:
            json.dump(person, f)


def createUser(attributes):
    for key in attributes:
        if not validator.validateInput(attributes[key], validator.regexes[key]):
            attributes["invalidInput"] = key
            return False
    user_id = len(people)+1
    people.append(user.createUser(attributes, user_id))
    return True



def findUser(attributes):
    for person in people:
        if person.firstName == attributes["firstName"] and person.lastName == attributes["lastName"]:
            return True
    return False

def updateUser(attributes):
    for person in people:
        if person.firstName == attributes["firstName"] and person.lastName == attributes["lastName"]:
            for key in attributes:
                person.key = attributes[key]
            return True
    return False

def deleteUser(attributes):
    for person in people:
        if person.firstName == attributes["firstName"] and person.lastName == attributes["lastName"]:
            people.remove(person)
            return True
    return False