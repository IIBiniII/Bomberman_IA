import pygame
from View.Personnage import *



class MainView:

    def __init__(self) -> None:
        pygame.init()
        self.window_height = 300
        self.window_width = 300
        self.window = pygame.display.set_mode((self.window_width,self.window_height))
        self.background = pygame.image.load("background.jpg")
        self.player = []
        #pygame.display.set_caption("Ma Fenêtre Pygame")

        
    def play(self):
        running = True
        while running : 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.clear()
            self.update_player()
            pygame.display.update()
            
    def stop(self):
        pygame.quit()

    def add_player(self,ply:Player): 
         self.player.append(ply)
    
    def clear(self):
        self.window.blit(self.background, (0, 0))

    def update_player(self):
        for player in self.player:
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

        
