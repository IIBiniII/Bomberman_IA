from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from View import *

game = MainView()
game.play()