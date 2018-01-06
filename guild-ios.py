#import modules

import ui
import random
import character

view = ui.load_view('guild-ios')
view.present('sheet')

#Adventurer's Guild 0.1 by Wiley Wiggins

newCharacter = character.Character()
view['textview1'].text = str(newCharacter)

def nextButton():
    if seed == "":
        seed= random.randint(0,9999)
    newCharacter.generateCharacter(seed)
    view['textview1'].text = str(newCharacter)
    view.reloadData()

def saveButton():
    print("i saved")
    



