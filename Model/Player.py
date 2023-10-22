class Player : #Essayer de le mettre dans Personnage.py
    def __init__(self,name:str)->None:
        self.speed = 0.1
        self.posX = (465//15)*1 + 25
        self.posY = (465//15)*1 + 25
        self.name = name
        #Init of bonuses
        self.fire_range = 3
        self.fire_bonus = 0
        self.bomb_bonus = 0
        self.angel_bonus_time = 0
        self.boot_bonus = 0 
        
        self.bomb_place = 0

        self.last_move = [0,0]

    def moveTo(self,x,y):
        self.posX += x
        self.posY += y
        self.last_move = [x,y]
    
    def player_case(self)->(int,int) :
        x,y= (self.posX-17)//(465/15),(self.posY-17)//(465/15)
        return int(x),int(y)