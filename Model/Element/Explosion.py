import datetime

from Model.Element import Grass

class Explosion:
    
    def __init__(self,Puissance : int,Direction : str) -> None:
        self.DateDeMort = datetime.datetime.now() + datetime.timedelta(seconds=1)
        
        self.Puissance = Puissance
        self.Direction = Direction

        self.Status = 1

    def checkStatus(self):

        tempAvantMort = self.DateDeMort - datetime.datetime.now()

        if   tempAvantMort < datetime.timedelta(seconds=0):
            self.Status = 0
        else:
            self.Status = 1
    
    def die(self):
        self = Grass()
    