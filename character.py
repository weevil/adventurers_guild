import random
import markovify

class Character:
    def __init__(self):
        self.seed = 0
        self.name = "Wiley Wiggins"
        self.kind = "Human"
        self.description = "A middle-aged, pasty community college student"

    def generateCharacter(self, seed):
        self.seed = seed
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

    #substances and adjectives would probably be shared by multiple character types

    def getSubstance(self):
        random.seed(self.seed)
        substanceFO = open("substances.txt")
        substanceList = list(substanceFO)
        selection = random.randint(0, len(substanceList) - 1)
        substance = substanceList[selection]
        substance = substance.rstrip("\n")
        return substance

    def getAdjective(self):
        random.seed(self.seed)
        adjectiveFO = open("adjectives.txt")
        adjectiveList = list(adjectiveFO)
        selection = random.randint(0, len(adjectiveList) - 1)
        adjective = adjectiveList[selection]
        adjective = adjective.rstrip("\n")
        return adjective

    #here's the functions to make a human

    def generateHumanName(self):
        random.seed(self.seed)
        #pick a first name
        firstnameFO = open("firstnames.txt", encoding='utf-8')
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

    def getColor(self):
        random.seed(self.seed)
        colorsFO = open("colors.txt")
        colorsList = list(colorsFO)
        colorsSelection = random.randint(0, len(colorsList) - 1)
        color = colorsList[colorsSelection]
        color = color.rstrip("\n")
        colorsFO.close()
        return color

    def getClothing(self):
        random.seed(self.seed)
        clothesFO = open("clothes.txt")
        clothesList = list(clothesFO)
        color = self.getColor();
        clothesSelection = random.randint(0, len(clothesList) - 1)
        clothingItem = clothesList[clothesSelection]
        clothingItem = clothingItem.rstrip("\n")
        clothingItem = color + " " + clothingItem
        if clothingItem[-1] != "s" and clothingItem[0] == "a" or clothingItem[0] == "e" or clothingItem[0] == "i" or clothingItem[0] == "o" or clothingItem[0] == "u":
            clothingItem = "an " + clothingItem
        elif clothingItem[-1] != "s":
            clothingItem = "a " + clothingItem
        return clothingItem
        clothesFO.close()

    def getHair(self):
        random.seed(self.seed)
        hairFO = open("hair.txt")
        hairList = list(hairFO)
        selection = random.randint(0, len(hairList) - 1)
        hair = hairList[selection]
        hair = hair.rstrip("\n")
        hairFO.close()
        return hair

    def getCareer(self):
        random.seed(self.seed)
        careerFO = open("careers.txt")
        careerList = list(careerFO)
        selection = random.randint(0, len(careerList) - 1)
        career = careerList[selection]
        career = career.rstrip("\n")
        careerFO.close()
        return career


    def generateHuman(self):
        random.seed(self.seed)
        humanName = self.generateHumanName()
        clothingItem = self.getClothing()
        hairStyle = self.getHair()
        clothes = self.getClothing()
        adjective = self.getAdjective()
        career = self.getCareer()
        self.kind = "Human"
        self.name = humanName
        self.description = "A " +  adjective + " mammal with smooth skin and " + hairStyle + " hair on its head. It is wearing " + clothingItem + ". " + humanName + " spends their time working as a " + career + "."

    # here's the animal functions
    def getAnimalName(self):
        random.seed(self.seed)
        #pick a first name
        nameFO = open("firstnames.txt")
        nameList = list(nameFO)
        selection = random.randint(0, len(nameList) - 1)
        name = nameList[selection]
        name = name.rstrip("\n")
        nameFO.close()
        return name

    def generateAnimal(self):
        random.seed(self.seed)
        animalName = self.getAnimalName()
        animalTypeFO = open("animals.txt")
        animalList = list(animalTypeFO)
        selection = random.randint(0, len(animalList) - 1)
        animalType = animalList[selection]
        animalType = animalType.rstrip("\n")
        adjective = self.getAdjective()
        if adjective[0] == "a" or adjective[0] == "e" or adjective[0] == "i" or adjective[0] == "o" or adjective[0] == "u":
            animalType = "An " + adjective + " " + animalType
        else:
            animalType = "A " + adjective + " " + animalType
        self.kind = "Animal"
        self.name = animalName
        self.description =  animalType + "."
        animalTypeFO.close()

    #here's the bird functions

    def getBirdName(self):
        random.seed(self.seed)
        #pick a first name
        nameFO = open("birdName.txt")
        nameList = list(nameFO)
        selection = random.randint(0, len(nameList) - 1)
        name = nameList[selection]
        name = name.rstrip("\n")
        nameFO.close()
        return name

    def generateBirdDescription(self):
        random.seed(self.seed)
        birdDescription = ""
        birdCorpusFO = open("bird_corpus.txt")
        text = birdCorpusFO.read()
        text_model = markovify.Text(text)
        for i in range(4):
            birdDescription += text_model.make_sentence() + " "
        return birdDescription


    def generateBird(self):
        random.seed(self.seed)
        name = self.getBirdName()
        enemyname = self.getAnimalName()
        enemyType = self.generateAnimal()
        adjective = self.getAdjective
        description = self.generateBirdDescription()
        description += name + " the bird is hunted through life by its enemy, " + enemyname +", a " + adjective + " " + enemyType +"."
        self.kind = "Bird"
        self.name = name
        self.description = description


    #veggies

    def generateVegetable(self):
        random.seed(self.seed)
        veggieType = random.randint(1,2)
        color = self.getColor()
        if veggieType == 1:
            pumpkinsFO = open("pumpkins.txt")
            pumpkinsList = list(pumpkinsFO)
            selection = random.randint(0, len(pumpkinsList) -1)
            veggieType = pumpkinsList[selection]
            veggieType = veggieType.rstrip("\n")
            pumpkinsFO.close()
        else:
            vegetablesFO = open("vegetables.txt")
            vegetablesList = list(vegetablesFO)
            selection = random.randint(0, len(vegetablesList))
            veggieType = vegetablesList[selection]
            veggieType = veggieType.rstrip("\n")
            vegetablesFO.close()

        self.name = "nameless"
        self.kind = "Vegetable"
        if color[0] == "a" or color[0] == "e" or color[0] == "i" or color[0] == "o" or color[0] == "u":
            color = "An " + color
        else:
            color = "A " + color
        self.description = color + " " + veggieType + "."

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
        self.description = "A hard working robot."

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
        nameFO = open("fungiType.txt")
        nameList = list(nameFO)
        selection = random.randint(0, len(nameList) - 1)
        fungiType = nameList[selection]
        fungiType = fungiType.rstrip("\n")
        adjective = self.getAdjective()
        color = self.getColor()
        self.kind = "Fungus"
        self.name = fungiName
        self.description = "A colony of " + adjective + color + fungiType + "."



    #obelisk functions

    def generateObelisk(self):
        someNumber = random.randint(0, 10000)
        substance = self.getSubstance()
        self.kind = "Obelisk"
        self.name = "nameless"
        self.description = "A " + str(someNumber) + " foot high obelisk made of " + substance + "."

    def __str__(self):
        return 'Name: ' + str(self.name) + '\nKind: ' + str(self.kind) + '\nDescription: ' + str(self.description)
