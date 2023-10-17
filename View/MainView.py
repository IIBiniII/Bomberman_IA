from View import *
from View.Button import Button
import pygame

class MainView:

    def __init__(self) -> None:
        print(pygame.version)
        pygame.init()
        self.window = pygame.display.set_mode((300,300))
        self.clock = pygame.time.Clock()

        #pygame.display.set_caption("Ma Fenêtre Pygame")

        self.bouton = Button(self.window,"ok",(30,30),60,60)

        
    def play(self):
        running = True
        while running : 
            ##event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()



            ##draw
            self.bouton.draw()
                    


            pygame.display.update()
            self.clock.tick(60)

            
        pygame.quit()

        
