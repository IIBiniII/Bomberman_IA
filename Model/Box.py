from Model.Player import Player
import pygame

class Box:

    def __init__(self,x,y,canBroke = False) -> None:
        self.x = x                  #Position dans la matrice de la map en X
        self.y = y                  #Position dans la matrice de la map en Y
        self.posX = (465//15)*x+17  #Position sur le fenêtre en X
        self.posY = (465//15)*y+17  #Position sur le fenêtre en Y
        if canBroke :
            self.box_image = pygame.image.load('Assets/Box.png')
            self.box_image = pygame.transform.scale(self.box_image, (465//15,465//15))
        else:
            self.box_image = pygame.image.load('Assets/BoxIncassable.png')
            self.box_image = pygame.transform.scale(self.box_image, (465//15,465//15))
            
        self.broken = False
        self.canBroke = canBroke

    def willCollide(self,player:Player,x,y):
        w,h = self.box_image.get_size()
        # print(self.x,self.y)
        # print(player.posX)
        if(player.posX + x >= self.posX and player.posX + x <= self.posX + w):
            if(player.posY + y >= self.posY and player.posY + y <= self.posY + h):
                return True
        return False