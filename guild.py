#Adventurer's Guild 0.1 by Wiley Wiggins

#import modules
import random
import character

def main():
    print("Adventurer's Guild")
    seed= random.randint(0,9999)
    newCharacter = character.Character()
    newCharacter.generateCharacter(seed)
    print(newCharacter)
    
main()
