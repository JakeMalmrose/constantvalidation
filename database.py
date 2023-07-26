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
    if not os.path.exists("database"):
        os.makedirs("database")
    dir = os.listdir("database")
    for file in dir:
        if file.endswith(".json"):
            with open("database/" + file, "r") as f:
                people.append(json.load(f))
                

def saveDatabase():
    if not os.path.exists("database"):
        os.makedirs("database")
    for file in os.listdir("database"):
        os.remove("database/" + file)
    for person in people:
        savePerson(person)

def savePerson(person):
    with open("database/" + str(person["id"]) + ".json", "w") as f:
        # check if person is dictionary
        if isinstance(person, dict):
            json.dump(person, f)
        else:
            json.dump(person.getUserJson(), f)


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
        if person["firstName"] == attributes["firstName"] and person["lastName"] == attributes["lastName"]:
            return person
    return False

def updateUser(attributesSearch, attributesUpdate):
    for person in people:
        if person["firstName"] == attributesSearch["firstName"] and person["lastName"] == attributesSearch["lastName"]:
            for key in attributesUpdate:
                person[key] = attributesUpdate[key]
            return True
    return False

def deleteUser(attributes):
    for person in people:
        if person["firstName"] == attributes["firstName"] and person["lastName"] == attributes["lastName"]:
            people.remove(person)
            return True
    return False