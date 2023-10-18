class Player : #Essayer de le mettre dans Personnage.py
    def __init__(self,name:str)->None:
        self.speed = 0.015
        self.posX = 5
        self.posY = 5
        self.name = name
        #Init of bonuses
        self.fire_range = 3
        self.fire_bonus = 0
        self.bomb_bonus = 0
        self.angel_bonus_time = 0
        self.boot_bonus = 0 

    def moveTo(self,x,y):
        self.posX += x
        self.posY += y