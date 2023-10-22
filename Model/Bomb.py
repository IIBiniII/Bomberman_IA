import pygame
import time
class Bomb:

    def __init__(self,player,tailleExplosion=2,caseX=0,caseY=0) -> None:
        self.delai = 3
        self.explosion = tailleExplosion
        self.caseX = caseX
        self.caseY = caseY

        self.bomb_image = pygame.image.load('Assets/bomb.png')
        self.bomb_image = pygame.transform.scale(self.bomb_image, (465//15,465//15))
        self.exploded = False
        self.time_place = time.localtime()
        self.player = player


    

        