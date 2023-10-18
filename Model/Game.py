from View import Player




class Game(): #Classe pour une Partie
    
    def __init__(self):
        
        self.players = [Player("player 1")]

    def add_player(self,ply:Player): 
         self.players.append(ply)



