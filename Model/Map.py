from random import randint

class Map:

    def __init__(self) -> None:
        # 0 = mure (incasable) :: 1 = sol :: 2 Caise
        self.Carte = [
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
    
    def placerCaisse(self):
        for nul in range(len(self.Carte)):
            for nuc in range(len(self.Carte[nul])):
                if self.Carte[nul][nuc] == 1 and randint(0,100) <= 60:
                    if nul not in (1,2,10,11) or nuc not in (1,2,12,13):
                        self.Carte[nul][nuc] = 2
                    



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


m = Map()
m.placerCaisse()
m.afficher()