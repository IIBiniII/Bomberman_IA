from random import randint
import Model.Element as Elem

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
        #self.CarteEvent = [ [None]*15 for i in range(13)]
        self.placerCaisse()
        #self.boxCarte = self.carteCaisse()          #Matrice utilisé pour les colision des joueurs
        self.convertNumberInObject() # les nombre de vienne des object (ex : box)


    
    def placerCaisse(self):
        for nul in range(len(self.Carte)):
            for nuc in range(len(self.Carte[nul])):
                if self.Carte[nul][nuc] == 1 and randint(0,100) <= 60:
                    if nul not in (1,2,10,11) or nuc not in (1,2,12,13):
                        self.Carte[nul][nuc] = 2
           
    """
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

    
    def convertNumberInObject(self):

        longeur = len(self.Carte)
        largeur = len(self.Carte[0])

        for l in range(longeur):
            for c in range(largeur):
                if self.Carte[l][c] == 0:
                    self.Carte[l][c] = Elem.BoxIncassable()
                elif self.Carte[l][c] == 1:
                    self.Carte[l][c] = Elem.Grass()
                elif self.Carte[l][c] == 2:
                    self.Carte[l][c] = Elem.Box()
