#import modules

import ui
import random
import clipboard
import character

#Adventurer's Guild 0.1 by Wiley Wiggins

def nextButton(sender):
    #print("next button pressed")
    global seed
    seed= random.randint(0,9999)
    newCharacter.generateCharacter(seed)
    view['textview1'].text = str(newCharacter)
    view['label1'].text = str("An adventurer appears!")

def saveButton(sender):
    print("i saved")
    clipboard.set(view['textview1'].text)
    view['label1'].text = str("copied to clipboard")


view = ui.load_view('guild-ios')
view.present('sheet')

newCharacter = character.Character()
view['textview1'].text = str(newCharacter)
