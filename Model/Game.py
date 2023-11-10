from Model import *

from Model import *
import Model.Element as Elem

class Game(): #Classe pour une Partie
    
    def __init__(self):
        
        self.players : list[Player]= [Player(0,"player 1")]
        self.nbPlayer = 1 ## pas sur
        self.map :Map = Map()
        self.map.placerCaisse()

        #placement des boite

                    
    def mouvePlayerTo(self, numplayer : int, direction :str):
        #print(direction)
        player = self.players[numplayer]
        newPosition = player.seePositionIfMoveTo(direction)
        if self.playerItBox(player,newPosition) == False:
            player.moveTo(direction)


    def playerItBox(self, player : Player,newPostion):
        for point in player.getItBox(newPostion):
            caseOfPoint = self.convertToCase(point)
            if type(self.map.Carte[caseOfPoint[1]][caseOfPoint[0]]) != Elem.Grass: # y puis x 
                return True
        
        return False
            
    
    def convertToCase(self,point)->(int,int) :
        x,y= (point[0]-17)//(465/15),(point[1]-17)//(465/15)##changer par des variable

        return (int(x),int(y))
    

    def placeBomb(self, numplayer : int):
        player = self.players[numplayer]
        if player.bomb > 0:

            playerCase = self.convertToCase((player.posX,player.posY))

            #convertire le direction en vecteur utilisable ex: TOP => (0,1) et BOTTOM => (0,-1)
            vecteurDicetion : (int,int)
            if player.discretionSee == "LEFT":
                vecteurDicetion = (-1,0)
            elif player.discretionSee == "RIGHT":
                vecteurDicetion = (1,0)
            elif player.discretionSee == "TOP":
                vecteurDicetion = (0,-1)
            elif player.discretionSee == "BOTTOM":
                vecteurDicetion = (0,1)
            
            #1er option : placer la bombe devant
            place = self.map.Carte[playerCase[1]+vecteurDicetion[1]][playerCase[0]+vecteurDicetion[0]]
            if type(place) == Elem.Grass:
                self.map.Carte[playerCase[1]+vecteurDicetion[1]][playerCase[0]+vecteurDicetion[0]] = Elem.Bombe(player, player.fire_range)

            player.bomb -= 1

    def explosion(self,Bombe : Elem.Bombe,possisionCase : (int,int)):

        directions = ("TOP","BOTTOM","LEFT","RIGHT")
        vecteurDirection = ((0,-1),(0,1),(-1,0),(1,0))

        for numDirection in range(4): #4 direction
            
            for distance in range(1,Bombe.Puissance):
                y = possisionCase[1]+distance*vecteurDirection[numDirection][1]
                x = possisionCase[0]+distance*vecteurDirection[numDirection][0]
                caseToucher = self.map.Carte[y][x]
                if type(caseToucher) == Elem.Box:
                    Bonnus = caseToucher.Breakit()
                    self.map.Carte[y][x] = Bonnus
                    break
                elif type(caseToucher) == Elem.BoxIncassable:
                    break
                else:
                    self.map.Carte[y][x] = Elem.Explosion(distance-Bombe.Puissance,directions[numDirection])
        
        self.map.Carte[possisionCase[1]][possisionCase[0]] = Elem.Explosion(0,"CENTER")

