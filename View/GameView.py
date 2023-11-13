from Model import *


import pygame

from Model.Game import Game

import Model.Element as Elem

class GameView(): #Classe pour une Partie

    def __init__(self):
        pygame.init()
        self.window_height = 500
        self.window_width = 500
        self.window = pygame.display.set_mode((self.window_width,self.window_height))
        self.background = pygame.image.load("Assets/background.jpg")
        self.background = pygame.transform.scale(self.background, (self.window_width,self.window_height))

        pygame.display.set_caption("Ma Fenêtre Pygame")

        dimension = (465//15,465//15)

        self.imageBoxIncassable = pygame.transform.scale(pygame.image.load('Assets/BoxIncassable.png'), dimension)
        self.imageBox = pygame.transform.scale(pygame.image.load('Assets/Box.png'), dimension)
        self.imageBombe = [
            pygame.transform.scale(pygame.image.load('Assets/bombes/BombeRouge3.png'), dimension),
            pygame.transform.scale(pygame.image.load('Assets/bombes/BombeRouge2.png'), dimension),
            pygame.transform.scale(pygame.image.load('Assets/bombes/BombeRouge1.png'), dimension),
        ]
        self.imageGrass = pygame.transform.scale(pygame.image.load('Assets/Grass.png'), dimension)
        
        #Explosion
        imageCenter = pygame.transform.scale(pygame.image.load('Assets/bombes/ExplosionCenter.png'), dimension)
        imageInter = pygame.transform.scale(pygame.image.load('Assets/bombes/ExplosionInterBottom.png'), dimension)
        imageEnd = pygame.transform.scale(pygame.image.load('Assets/bombes/ExplosionEndBottom.png'), dimension)
        self.imageExplosion = [
            imageCenter,
            {"TOP" : pygame.transform.rotate(imageInter,180),"BOTTOM" : imageInter,"LEFT" : pygame.transform.rotate(imageInter,90),"RIGHT" : pygame.transform.rotate(imageInter,-90)},
            {"TOP" : pygame.transform.rotate(imageEnd,180),"BOTTOM" : imageInter,"LEFT" : pygame.transform.rotate(imageEnd,90),"RIGHT" : pygame.transform.rotate(imageEnd,-90)}
        ]

        self.imageBonnus = [
            pygame.transform.scale(pygame.image.load('Assets/Bonnus/BonnusBombe.png'), (465//15,465//15)),
            pygame.transform.scale(pygame.image.load('Assets/Bonnus/BonnusFeu.png'), (465//15,465//15)),
            pygame.transform.scale(pygame.image.load('Assets/Bonnus/BonnusVitesse.png'), (465//15,465//15))
        ]

        self.game : Game = Game() #Permettera de changer la partie affiché
    

    def update(self): 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        self.clear()
        self.update_boxes() # drawbox
        self.update_game() # drawplayer
        pygame.display.update()
        return True
    
    def clear(self):
        self.window.blit(self.background, (0, 0))

    def stop(self):
        pygame.quit()

    # Déplacement/action du joueur
    def update_game(self):
        for player in self.game.players:
            police = pygame.font.SysFont("Arial", 10)
            text = police.render(player.name, True, "black")
            self.window.blit(text, (player.posX - 10, player.posY - 20))
            pygame.draw.rect(self.window, (0, 200, 50), pygame.Rect(player.posX-player.coter/2, player.posY-player.coter/2, player.coter, player.coter))
            #pygame.draw.circle(self.window, pygame.color.Color(0, 200, 50), (player.posX, player.posY), 5, 3)

            ##point de itbox
            for point in player.getItBox((player.posX,player.posY)):
                pygame.draw.circle(self.window,(255,0,0),(point[0],point[1]), 1,1)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_z]:
                self.game.mouvePlayerTo(player.number,"TOP")

            if keys[pygame.K_s]:
                self.game.mouvePlayerTo(player.number,"BOTTOM")

            if keys[pygame.K_q]:
                self.game.mouvePlayerTo(player.number,"LEFT")

            if keys[pygame.K_d]:
                self.game.mouvePlayerTo(player.number,"RIGHT")


            if keys[pygame.K_SPACE]:
                self.game.placeBomb(player.number)
                



    def update_boxes(self):
        for y in range(len(self.game.map.Carte)):
            for x in range(len(self.game.map.Carte[y])):
                valElement = self.game.map.Carte[y][x]
                typeElement = type(valElement)

                images = self.getImagesOfElement(self.game.map.Carte[y][x])
                for image in images:
                    self.window.blit(image,(x*(465/15)+17,y*(465/15)+17))
                


                ##update module
                if typeElement == Elem.Bombe or typeElement == Elem.Explosion:
                    if typeElement == Elem.Bombe:
                        valElement : Elem.Bombe
                        valElement.checkStatus()
                        if valElement.Status == 0:
                            self.game.explosion(valElement,(x,y))
                            valElement.retourAuPlayer()

                    elif typeElement == Elem.Explosion:
                        
                        valElement: Elem.Explosion
                        valElement.checkStatus()
                        if valElement.Status == 0:
                            self.game.map.Carte[y][x] = Elem.Grass()
                        else:

                            image = self.imageBombe[0] # dois être une bombe

                


    def getImagesOfElement(self,element):
            typeElement = type(element)

            images = []
            if typeElement == Elem.BoxIncassable :
                images.append(self.imageBoxIncassable)
            elif typeElement == Elem.Grass:
                images.append(self.imageGrass)
            elif typeElement == Elem.Box:
                images.append(self.imageBox)
            elif typeElement == Elem.BonnusBombe or typeElement == Elem.BonnusFeu or typeElement == Elem.BonnusVitesse:
                if typeElement == Elem.BonnusBombe:
                    images.append(self.imageBonnus[0])
                elif typeElement == Elem.BonnusFeu:
                    images.append(self.imageBonnus[1])
                elif typeElement == Elem.BonnusVitesse:
                    images.append(self.imageBonnus[2])
            
            elif typeElement == Elem.Bombe or typeElement == Elem.Explosion:
                images.append(self.imageGrass)

                if typeElement == Elem.Bombe:
                    images.append(self.imageBombe[element.Status-1])
                elif typeElement == Elem.Explosion:
                    images.append(self.imageOfExplosion(element))

            return images
    
    def imageOfExplosion(self,explosion : Elem.Explosion):

        if explosion.Puissance == explosion.powerMax:
            return self.imageExplosion[0]
        elif explosion.Puissance == 0:
            return self.imageExplosion[2][explosion.Direction]
        elif explosion.Puissance < explosion.powerMax:
            return self.imageExplosion[1][explosion.Direction]
    


