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

        player = self.players[numplayer]
        newPosition = player.seePositionIfMoveTo(direction)
        if self.playerItBox(player,newPosition) == False:
            player.moveTo(direction)

    ##idée de modification : avoir un if avec CanGo(p,p) qui utilise playerItBox()
    
    def playerItBox(self, player : Player,newPostion):
        for point in player.getItBox(newPostion):
            caseOfPoint = self.convertToCase(point)
            typeCase = type(self.map.Carte[caseOfPoint[1]][caseOfPoint[0]])# y puis x 
            if typeCase == Elem.Bombe:
                ## si il était déja dedans alors il peux bouger
                for pointplayerActuel in player.getItBox((player.posX,player.posY)):
                    caseOfPointPlayer = self.convertToCase(pointplayerActuel)
                    if type(self.map.Carte[caseOfPointPlayer[1]][caseOfPointPlayer[0]]) == Elem.Bombe:
                        return False
                
                return True

            elif typeCase != Elem.Grass: 
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
                self.map.Carte[playerCase[1]+vecteurDicetion[1]][playerCase[0]+vecteurDicetion[0]] = Elem.Bombe(player)
            #2ème potion : on la place ou il est
            else:
                self.map.Carte[playerCase[1]][playerCase[0]] = Elem.Bombe(player)


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
                    self.map.Carte[y][x] = Elem.Explosion(Bombe.Puissance-distance,directions[numDirection],Bombe.Puissance)
        
        self.map.Carte[possisionCase[1]][possisionCase[0]] = Elem.Explosion(Bombe.Puissance,"CENTER",Bombe.Puissance)

