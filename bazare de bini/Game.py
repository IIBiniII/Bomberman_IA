from Model import *


class Game: #Classe pour une Partie
    
    def __init__(self):
        
        self.players = [Player("player 1")]
        self.map :Map = Map()
        self.map.placerCaisse()

        #placement des boite
        self.boxes = []
        for y in range(len(self.map.Carte)):
            for x in range(len(self.map.Carte[y])) :
                if self.map.Carte[y][x] == 2:
                    self.boxes.append(Box(x,y,True))
                if self.map.Carte[y][x] == 0:
                    self.boxes.append(Box(x,y,False))

        self.bombPlace = []
        
                    

    def add_player(self,ply:Player): 
         self.players.append(ply)



