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
        characterType = random.randint(0, 9)
        if characterType <= 2:
            self.generateHuman()
        elif characterType == 3:
            self.generateFungus()
        elif characterType == 4:
            self.generateVegetable()
        elif characterType == 5:
            self.generateAnimal()
        elif characterType == 6:
            self.generateBird()
        elif characterType == 7:
            self.generateObelisk()
        elif characterType == 8:
            self.generateGhost()
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
        clothingItem = self.addAorAn(clothingItem)
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
        obeliskSubstance = self.getSubstance()
        self.kind = "Human"
        self.name = humanName
        self.description = "A bipedal mammal with smooth skin and " + hairStyle + " hair on its head. It is wearing " + clothingItem + ". " + humanName + " worked as a " + career + " before emarking on their " + adjective + " quest to find the legendary " + obeliskSubstance + " obelisk"

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

    def generateAnimalDescription(self):
        animalDescription = " "
        random.seed(self.seed)
        animalCorpusFO = open("animal_corpus.txt")
        text = animalCorpusFO.read()
        text_model = markovify.NewlineText(text)
        for i in range(4):
            try:
                animalDescription += text_model.make_sentence(tries=100) + " "
            except TypeError:
                animalDescription += "It hunts daily for food. "
        animalCorpusFO.close()
        return animalDescription

    def getAnimalType(self):
        animalTypeFO = open("animals.txt")
        animalList = list(animalTypeFO)
        selection = random.randint(0, len(animalList) - 1)
        animalType = animalList[selection]
        animalType = animalType.rstrip("\n")
        return animalType
        animalTypeFO.close()

    def generateAnimal(self):
        random.seed(self.seed)
        animalName = self.getAnimalName()
        animalType = self.getAnimalType()
        adjective = self.getAdjective()
        description = self.generateAnimalDescription()
        animalType = adjective + " " + animalType
        animalType = self.addAorAn(animalType)
        self.kind = "Animal"
        self.name = animalName
        self.description =  animalType + ". " + description

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
        birdDescription = " "
        birdCorpusFO = open("bird_corpus.txt")
        text = birdCorpusFO.read()
        text_model = markovify.NewlineText(text)
        for i in range(3):
            try:
                birdDescription += text_model.make_sentence() + " "
            except TypeError:
                birdDescription += "It enjoys flying. "
        birdCorpusFO.close()
        return birdDescription

    def generateBird(self):
        random.seed(self.seed)
        name = self.getBirdName()
        enemyname = self.getAnimalName()
        enemyType = self.getAnimalType()
        adjective = self.getAdjective()
        adjective = self.addAorAn(adjective)
        description = self.generateBirdDescription()
        description = description + " " + name + " the bird is hunted through life by its enemy, " + enemyname +", " + adjective + " " + enemyType +"."
        self.kind = "Bird"
        self.name = name
        self.description = description


    #veggies
    def generateVegetableDescription(self):
        random.seed(self.seed)
        vegetableDescription = " "
        veggieCorpusFO = open("veggie_corpus.txt")
        text = veggieCorpusFO.read()
        text_model = markovify.NewlineText(text)
        for i in range(2):
            vegetableDescription += text_model.make_sentence(tries=100) + " "
        veggieCorpusFO.close()
        return vegetableDescription

    def generateVegetable(self):
        random.seed(self.seed)
        veggieType = random.randint(1,2)
        color = self.getColor()
        vegetableDescription = self.generateVegetableDescription()
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
        color = self.addAorAn(color)
        self.description = color + " " + veggieType + ". " + vegetableDescription

    #robot functions

    def getRobotName(self):
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

    def generateRobotDescription(self):
        random.seed(self.seed)
        robotDescription = " "
        robotCorpusFO = open("robot_corpus.txt")
        text = robotCorpusFO.read()
        text_model = markovify.Text(text)
        for i in range(4):
            robotDescription += text_model.make_sentence(tries=100) + " "
        robotCorpusFO.close()
        return robotDescription


    def generateRobot(self):
        name = self.getRobotName()
        description = self.generateRobotDescription()
        self.kind = "Robot"
        self.name = name
        self.description = "A hard working robot." + " " + description

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
        self.description = "A colony of " + adjective + ", " + color + " " + fungiType + "."

    #ghost functions

    def getGhostName(self):
        random.seed(self.seed)
        #pick a first name
        nameFO = open("ghostType.txt")
        nameList = list(nameFO)
        selection = random.randint(0, len(nameList) - 1)
        name = nameList[selection]
        name = name.rstrip("\n")
        nameFO.close()
        return name

    def generateGhostDescription(self):
        random.seed(self.seed)
        adjective = self.getAdjective()
        adjective = self.addAorAn(adjective)
        ghostDescription = " "
        ghostCorpusFO = open("ghost_corpus.txt")
        text = ghostCorpusFO.read()
        text_model = markovify.Text(text)
        for i in range(3):
            ghostDescription += text_model.make_sentence(tries=100) + " "
        ghostCorpusFO.close()
        ghostDescription = adjective + " spirit. " + ghostDescription
        return ghostDescription

    def generateGhost(self):
        random.seed(self.seed)
        someNumber = random.randint(0, 10000)
        substance = self.getSubstance()
        kind = self.getGhostName()
        description = self.generateGhostDescription()
        self.kind = "Ghost"
        self.name = kind
        self.description = description

    #obelisk functions

    def generateObelisk(self):
        random.seed(self.seed)
        someNumber = random.randint(0, 10000)
        substance = self.getSubstance()
        self.kind = "Obelisk"
        self.name = "nameless"
        self.description = "A " + str(someNumber) + " foot high obelisk made of " + substance + "."

    def __str__(self):
        return 'Name: ' + str(self.name) + '\n \nKind: ' + str(self.kind) + '\n \nDescription: ' + str(self.description)

    #puts either an 'a' or 'an' before a word depending on if the word starts with a vowel or not and not at all if it's plural

    def addAorAn(self, word):
        if word[-1] != "s" and word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
            word = "an " + word
        elif word[-1] != "s":
            word = "a " + word
        return word
