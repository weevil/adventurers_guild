#Adventurer's Guild 0.1 by Wiley Wiggins

#import modules
import random
#not using the asciimatics stuff yet, but here's the bits we'd need for text-UI
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication

#initial data for the form we will eventually build with asciimatics


#everything is currently in functions because I haven't written any classes yet, that's next.

class Character:
    def __init__(self):
        self.seed = "0"
        self.name = "Wiley Wiggins"
        self.kind = "Human"
        self.description = "A middle-aged, pasty community college student"

    def generateSeed(self):
        characterSeed = input("Press enter to summon an entity: ")
        if characterSeed == "":
            characterSeed = random.randint(0, 999)
        else:
            characterSeed = int(characterSeed)
        self.seed = characterSeed

    def generateCharacter(self):
        characterType = random.randint(0, 7)
        if characterType == 1:
            self.generateHuman()
        elif characterType == 2:
            self.generateFungus()
        elif characterType == 3:
            self.generateVegetable()
        elif characterType == 4:
            self.generateAnimal()
        elif characterType == 5:
            self.generateBird()
        elif characterType == 6:
            self.generateObelisk()
        else:
            self.generateRobot()

    def generateHumanName(self):
        random.seed(self.seed)
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

    def getClothing(self):
        random.seed(self.seed)
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

    def getHair(self):
        random.seed(self.seed)
        hairSO = open("hair.txt")
        hairList = list(hairSO)
        selection = random.randint(0, len(hairList) - 1)
        hair = hairList[selection]
        hair = hair.rstrip("\n")
        return hair

    def generateHuman(self):
        humanName = self.generateHumanName()
        clothingItem = self.getClothing()
        hairStyle = self.getHair()
        clothes = self.getClothing()
        self.kind = "Human"
        self.name = humanName
        self.description = "A bilaterally symmetrical mammal with smooth skin and " + hairStyle + " hair on its head. It is wearing", clothingItem + "."

    #here's the bird functions

    def generateBirdName(self):
        random.seed(self.seed)
        #pick a first name
        nameFO = open("birdName.txt")
        nameList = list(nameFO)
        selection = random.randint(0, len(nameList) - 1)
        name = nameList[selection]
        name = name.rstrip("\n")
        nameFO.close()
        return name

    def generateBird(self):
        birdName = self.generateBirdName()
        self.kind = "Bird"
        self.name = birdName

    #robot functions

    def generateRobotName(self):
        random.seed(self.seed)
        #pick a first name
        nameFO = open("robotName.txt")
        nameList = list(nameFO)
        selection = random.randint(0, len(nameList) - 1)
        name = nameList[selection]
        name = name.rstrip("\n")
        name = name + "-" + str(random.randint(100, 1000))
        nameFO.close()
        return name

    def generateRobot(self):
        robotName = self.generateRobotName()
        self.kind = "Robot"
        self.name = robotName

    #fungus functions

    def generateFungiName(self):
        random.seed(self.seed)
        #pick a first name
        nameFO = open("fungiName.txt")
        nameList = list(nameFO)
        selection = random.randint(0, len(nameList) - 1)
        name = nameList[selection]
        name = name.rstrip("\n")
        nameFO.close()
        return name

    def generateFungus(self):
        fungiName = self.generateFungiName()
        self.kind = "Fungus"
        self.name = fungiName

    #substances would probably be shared by multiple character types

    def getSubstance(self):
        random.seed(self.seed)
        substanceSO = open("substances.txt")
        substanceList = list(substanceSO)
        selection = random.randint(0, len(substanceList) - 1)
        substance = substanceList[selection]
        substance = substance.rstrip("\n")
        return substance

    #obelisk functions

    def generateObelisk(self):
        someNumber = random.randint(0, 10000)
        substance = self.getSubstance()
        self.kind = "Obelisk"
        self.name = "nameless"
        self.description = "A", str(someNumber), "foot high obelisk made of " + substance + "."

#here's the functions to make a human


def main():
    print("Adventurer's Guild")
    newCharacter = Character()
    newCharacter.generateSeed()
    newCharacter.generateCharacter()
    print("Name:", newCharacter.name)
    print("Kind:", newCharacter.kind)
    print("Description:", newCharacter.description)
main()
