import user
import json
import os

people = []

def __init__():
    loadDatabase()

def makeDatabase():
    pass

def loadDatabase():
    dir = os.listdir("database")
    for file in dir:
        if file.endswith(".json"):
            with open("database/" + file, "r") as f:
                people.append = json.load(f)

def createUser(attributes):
    # using attributes, dump json into a file
    # find the highest id in directory, files are named by ID
    dir = os.listdir("database")
    highestID = 0
    for file in dir:



    for key in attributes:
        pass

def findUser(attributes):
    pass