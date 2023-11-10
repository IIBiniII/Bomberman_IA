from random import randint
from Model.Element import *

class Box:

    BONNUS = [BonnusBombe(),BonnusVitesse(),BonnusFeu()]
    

    def Breakit(self):
        randNumber = randint(1,100)

        if randNumber < 5:
            res = __class__.BONNUS[0]
        elif randNumber < 10:
            res = __class__.BONNUS[1]
        elif randNumber < 20:
            res = __class__.BONNUS[2]
        else:
            res = Grass()
        
        return res