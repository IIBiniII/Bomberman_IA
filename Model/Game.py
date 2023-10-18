from View import Player
from Model.Map import Map
from View.Box import Box




class Game: #Classe pour une Partie
    
    def __init__(self):
        
        self.players = [Player("player 1")]
        self.map :Map = Map()

        self.boxes = []
        for y in range(len(self.map.Carte)):
            for x in range(len(self.map.Carte[y])) :
                if self.map.Carte[y][x]:
                    print(x,y)
                    self.boxes.append(Box(x,y))
                    

    def add_player(self,ply:Player): 
         self.players.append(ply)



