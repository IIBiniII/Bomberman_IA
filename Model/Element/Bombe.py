import datetime

class Bombe():
    
    def __init__(self,player,Puissance) -> None:
        self.DateDeMort = datetime.datetime.now() + datetime.timedelta(seconds=3)
        self.Status = 3
        self.player = player
        self.Puissance = Puissance

    
    def checkStatus(self):

        tempAvantMort = self.DateDeMort - datetime.datetime.now()

        if   tempAvantMort < datetime.timedelta(seconds=0):
            self.Status = 0
        elif tempAvantMort < datetime.timedelta(seconds=1):
            self.Status = 1
        elif tempAvantMort < datetime.timedelta(seconds=2):
            self.Status = 2
        elif tempAvantMort <=datetime.timedelta(seconds=3):
            self.Status = 3
    

    def retourAuPlayer(self):
        self.player.bomb += 1
        
    
    
        