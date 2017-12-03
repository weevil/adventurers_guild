#Adventurer's Guild 0.1 by Wiley Wiggins

#import modules
import random
import character
import pyglet
from pyglet.window import key

newCharacter = character.Character()
window = pyglet.window.Window(500, 800, caption='Adventurer\'s Guild')
document = pyglet.text.document.FormattedDocument()
layout = pyglet.text.layout.TextLayout(document, 500, 800)
title = pyglet.text.Label('Press ENTER to summon an entity',
                          font_name='Fredoka One',
                          font_size=16,
                          color=(249,104,107,255),
                          x=window.width//2, y=window.height-16,
                          anchor_x='center', anchor_y='center')

characterText = pyglet.text.Label( str(newCharacter),
                                    font_name='ProFontIIx',
                                    font_size=10,
                                    color=(15,10,10,255),
                                    x=10,y=window.height - 40,
                                    anchor_x='left', anchor_y='top')

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')
    if symbol == key.ENTER:
        seed= random.randint(0,9999)
        newCharacter.generateCharacter(seed)
        print('Enter was pressed')
        characterText.draw()
        print(newCharacter)
    return newCharacter
    window.push_handlers(on_key_press)

@window.event
def on_draw():
    pyglet.gl.glClearColor(240,240,240,255)
    window.clear()
    title.draw()
    characterText.draw()




pyglet.app.run()
