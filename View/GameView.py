from Model import Player
from Model.Game import Game

import pygame


class GameView(): #Classe pour une Partie
    
    def __init__(self):
        pygame.init()
        self.window_height = 500
        self.window_width = 500
        self.window = pygame.display.set_mode((self.window_width,self.window_height))
        self.background = pygame.image.load("Assets/background.jpg")
        self.background = pygame.transform.scale(self.background, (self.window_width,self.window_height))

        pygame.display.set_caption("Ma Fenêtre Pygame")

        self.box_image = pygame.image.load('Assets/Box.png')
        self.box_image = pygame.transform.scale(self.box_image, (465/15,465/15))

        self.box_image_incassable = pygame.image.load('Assets/BoxIncassable.png')
        self.box_image_incassable = pygame.transform.scale(self.box_image_incassable, (465/15,465/15))


        self.game : Game = Game() #Permettera de changer la partie affiché

    def update(self): 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        self.clear()
        self.update_boxes()
        self.update_player()
        pygame.display.update()
        return True

    def stop(self):
        pygame.quit()

    def add_player(self,ply:Player): 
         self.players.append(ply)
    
    def clear(self):
        self.window.blit(self.background, (0, 0))

    def update_player(self):
        for player in self.game.players:
                police = pygame.font.SysFont("Arial",10)
                text = police.render(player.name,True,"black")
                self.window.blit(text,(player.posX - 10 ,player.posY - 20))
                pygame.draw.circle(self.window,pygame.color.Color(0,0,0),(player.posX,player.posY),5,3)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_z]:
                    if player.posY>0:
                        player.moveTo(0,-player.speed)
                if keys[pygame.K_s]:
                    if player.posY<=self.window_height:
                        player.moveTo(0,player.speed)
                if keys[pygame.K_q]:
                    if player.posX>0:
                        player.moveTo(-player.speed,0)
                if keys[pygame.K_d]:
                    if player.posX<=self.window_width:
                        player.moveTo(player.speed,0)

    def update_boxes(self):
        for box in self.game.boxes:
            if not box.broken : 
                if not box.canBroke:
                    self.window.blit(self.box_image_incassable, (box.x*(465/15) +17,box.y*(465/15)+17))
                else :
                    self.window.blit(self.box_image, (box.x*(465/15)+17,box.y*(465/15)+17))


