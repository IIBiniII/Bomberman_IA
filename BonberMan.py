import View
import Controler
import Model

"""
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from View import *

game = MainView()
player1 = Player("Bertrand")
game.add_player(player1)
game.play()
"""

fenêtre = View.MainView()
while 1:
    fenêtre.update()
#fenêtre.mainloop()