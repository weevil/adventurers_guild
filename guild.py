#Adventurer's Guild 0.1 by Wiley Wiggins

#import modules
import random
from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
    CheckBox, RadioButtons, Button, PopUpDialog
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication, \
    InvalidFields

#initial data for the form
form_data = {
"name": "Wiley Wiggins",
"type": "human",
"description": "A middle-aged, pasty community college student",
}


def generateHumanName(characterSeed):
    random.seed(characterSeed)
    #pick a first name
    firstnameFO = open("firstnames.txt")
    firstnameList = list(firstnameFO)
    selection = random.randint(0, len(firstnameList) - 1)
    firstname = firstnameList[selection]
    firstname = firstname.rstrip("\n")
    firstnameFO.close()

    #pick a last name
    lastnameFO = open("lastnameBeginnings.txt")
    lastnameEndingsFO = open("lastnameEndings.txt")
    lastnameList = list(lastnameFO)
    lastnameEndingsList = list(lastnameEndingsFO)
    selection = random.randint(0, len(lastnameList) - 1)
    lastname = lastnameList[selection]
    lastname = lastname.rstrip("\n")
    selection = random.randint(0, len(lastnameEndingsList) - 1)
    lastnameEnding = lastnameEndingsList[selection]
    lastnameEnding = lastnameEnding.rstrip("\n")
    lastname = lastname + lastnameEnding
    name = firstname + " " + lastname
    return name
    lastnameFO.close()

def getClothing(characterSeed):
    random.seed(characterSeed)
    clothesFO = open("clothes.txt")
    clothesList = list(clothesFO)
    selection = random.randint(0, len(clothesList) - 1)
    clothingItem = clothesList[selection]
    clothingItem = clothingItem.rstrip("\n")
    if clothingItem[-1] != "s" and clothingItem[0] == "a" or clothingItem[0] == "e" or clothingItem[0] == "i" or clothingItem[0] == "o" or clothingItem[0] == "u":
        clothingItem = "an " + clothingItem
    elif clothingItem[-1] != "s":
        clothingItem = "a " + clothingItem
    return clothingItem
    clothesFO.close()

def getHair(characterSeed):
    random.seed(characterSeed)
    hairSO = open("hair.txt")
    hairList = list(hairSO)
    selection = random.randint(0, len(hairList) - 1)
    hair = hairList[selection]
    hair = hair.rstrip("\n")
    return hair

def generateHuman(characterSeed):
    humanName = generateHumanName(characterSeed)
    clothingItem = getClothing(characterSeed)
    hairStyle = getHair(characterSeed)
    clothes = getClothing(characterSeed)
    print("Type: Human")
    print("Name:", humanName)
    print("A bilaterally symmetrical mammal with smooth skin and " + hairStyle + " hair on its head. It is wearing", clothingItem + "." )

def generateBirdName(characterSeed):
    random.seed(characterSeed)
    #pick a first name
    nameFO = open("birdName.txt")
    nameList = list(nameFO)
    selection = random.randint(0, len(nameList) - 1)
    name = nameList[selection]
    name = name.rstrip("\n")
    nameFO.close()
    return name

def generateBird(characterSeed):
    birdName = generateBirdName(characterSeed)
    print("Type: Bird")
    print("Name:", birdName)

def generateRobotName(characterSeed):
    random.seed(characterSeed)
    #pick a first name
    nameFO = open("robotName.txt")
    nameList = list(nameFO)
    selection = random.randint(0, len(nameList) - 1)
    name = nameList[selection]
    name = name.rstrip("\n")
    name = name + "-" + str(random.randint(100, 1000))
    nameFO.close()
    return name

def getSubstance(characterSeed):
    random.seed(characterSeed)
    substanceSO = open("substances.txt")
    substanceList = list(substanceSO)
    selection = random.randint(0, len(substanceList) - 1)
    substance = substanceList[selection]
    substance = substance.rstrip("\n")
    return substance

def generateObelisk(characterSeed):
    someNumber = random.randint(0, 10000)
    substance = getSubstance(characterSeed)
    print("Type: Obelisk")
    print("Name: nameless")
    print("A", str(someNumber), "foot high obelisk made of " + substance + ".")

def main():
    print("Adventurer's Guild")
    characterSeed = input("press enter to meet a candidate \n") #you can secretly enter a seed number to get a specific character
    if characterSeed == "":
        characterSeed = random.randint(0, 999)
    random.seed(characterSeed)
    characterType = random.randint(0, 6)
    if characterType == 1:
        generateHuman(characterSeed)
    elif characterType == 2:
        print("Type: Animal")
        print("Name:", "Fuzzy Wuzzy")
    elif characterType == 3:
        print("Type: Vegetable")
        print("Name:", "Urm")
    elif characterType == 4:
        print("Type: Fungus")
        print("Name:", "glush")
    elif characterType == 5:
        generateBird(characterSeed)
    elif characterType == 6:
        generateObelisk(characterSeed)
    else:
        robotName = generateRobotName(characterSeed)
        print("Type: Robot")
        print("Name:", robotName)
main()
