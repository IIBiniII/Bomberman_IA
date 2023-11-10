from Model import *

class Player() : #Essayer de le mettre dans Personnage.py
    def __init__(self,number,name:str)->None:
        self.number = number
        self.speed = 0.1
        self.posX = (465//15)*1 + 30#25
        self.posY = (465//15)*1 + 30#25
        self.name = name
        #Init of bonuses
        self.fire_range = 3
        self.fire_bonus = 0
        #self.bomb_bonus = 0
        self.angel_bonus_time = 0
        self.boot_bonus = 0 
        
        #self.bomb_place = 0
        self.bomb = 1
        

        self.last_move = [0,0]

        #ajout
        
        self.coter = 20
        self.discretionSee : str = "TOP" 


    """
    def moveTo(self,x,y):
        self.posX += x
        self.posY += y
        self.last_move = [x,y]
    
        
    def player_case(self)->(int,int) :
        x,y= (self.posX-17)//(465/15),(self.posY-17)//(465/15)
        return int(x),int(y)
    """
    
    def moveTo(self,direction : str):
        
        newposition = self.seePositionIfMoveTo(direction)

        self.posX, self.posY = newposition[0],newposition[1]
        self.discretionSee = direction
        
            
    def seePositionIfMoveTo(self,direction : str) -> (float,float):
        if direction == "LEFT":
            x,y = self.posX - self.speed ,self.posY
        elif direction == "RIGHT":
            x,y = self.posX + self.speed ,self.posY
        elif direction == "TOP":
            x,y = self.posX, self.posY - self.speed
        elif direction == "BOTTOM":
            x,y = self.posX, self.posY + self.speed
        else: 
            raise ValueError("cette direction n'existe pas")
        
        return (round(x,1),round(y,1))
        

    
    def getItBox(self,postions: (float,float)) -> (float,float,float,float):

        listePoints = [None,None,None,None]
        tableauCoef = (1,-1)

        moitierCoter = (self.coter)/2

        for i in range(2):
            for j in range(2):
                pointx = tableauCoef[i]*moitierCoter+postions[0]
                pointy = round(tableauCoef[j]*moitierCoter+postions[1],1)
                listePoints[i*2+j] = (pointx,pointy)
        #print("---------------")
        #print(f"postion actuel, {self.posX},{self.posY}")
        #print(f"Postion Future, {postions}")
        #print(f"listepoints , {listePoints}")
        return listePoints