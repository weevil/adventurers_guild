#Adventurer's Guild 0.1 by Wiley Wiggins

#import modules
import random

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

def getSubstance(characterSeed):
    random.seed(characterSeed)
    substanceSO = open("substances.txt")
    substanceList = list(substanceSO)
    selection = random.randint(0, len(substanceList) - 1)
    substance = substanceList[selection]
    substance = substance.rstrip("\n")
    return substance

def main():
    print("Adventurer's Guild")
    characterSeed = input("press enter to meet a candidate \n") #you will eventually be able to secretly enter a seed number to get a particular character
    if characterSeed == "":
        characterSeed = random.randint(0, 999)
    random.seed(characterSeed)
    clothes = getClothing(characterSeed)
    characterType = random.randint(0, 6)
    if characterType == 1:
        humanName = generateHumanName(characterSeed)
        clothingItem = getClothing(characterSeed)
        print("Type: Human")
        print("Name:", humanName)
        print("A bilaterally symmetrical mammal with smooth skin and black-colored hair on its head. It is wearing", clothingItem + "." )
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
        birdName = generateBirdName(characterSeed)
        print("Type: Bird")
        print("Name:", birdName)
    elif characterType == 6:
        someNumber = random.randint(0, 10000)
        substance = getSubstance(characterSeed)
        print("Type: Obelisk")
        print("Name: nameless")
        print("A", str(someNumber), "foot high obelisk made of " + substance + ".")
    else:
        robotName = generateRobotName(characterSeed)
        print("Type: Robot")
        print("Name:", robotName)
main()
