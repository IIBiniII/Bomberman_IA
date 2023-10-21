from random import randint
from Model.Box import Box

class Map:

    def __init__(self) -> None:
        # 0 = mur (incassable) :: 1 = sol :: 2 = Caisse
        self.Carte = [                                  #Matrice utilisé par l'ia 
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                     [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                     [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                     [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                     [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                     [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    ]
        self.boxCarte = self.carteCaisse()              #Matrice utilisé pour les colision des joueurs
    
    def placerCaisse(self):
        for nul in range(len(self.Carte)):
            for nuc in range(len(self.Carte[nul])):
                if self.Carte[nul][nuc] == 1 and randint(0,100) <= 60:
                    if nul not in (1,2,10,11) or nuc not in (1,2,12,13):
                        self.Carte[nul][nuc] = 2
        self.boxCarte = self.carteCaisse() #Mettre à jour la matrice de box
                    

    def carteCaisse(self):
        carteBox = []
        for numLigne in range(len(self.Carte)):
            ligneBox = []
            for numCol in  range(len(self.Carte[numLigne])): 
                valCase = self.Carte[numLigne][numCol] #Récupère la valeur de la case associé de la mattrice self.Carte
                if valCase == 0:
                    ligneBox.append(Box(numCol,numLigne,False))
                elif valCase == 2 :
                    ligneBox.append(Box(numCol,numLigne,True))
                else:
                    ligneBox.append(0) 
            carteBox.append(ligneBox)
        return carteBox

    def is_box_at(self,x,y):
        if type(self.boxCarte[y][x])==Box:
            return True
        return False



    def afficher(self):
        
        text = ""

        for l in self.Carte:
            for v in l:
                if v == 0:
                    text+="▓▓▓"
                elif v == 1:
                    text+="░░░"
                elif v == 2:
                    text+="▒▒▒"

            text+="\n"
        
        print(text)

"""
m = Map()
m.placerCaisse()
m.afficher()
"""