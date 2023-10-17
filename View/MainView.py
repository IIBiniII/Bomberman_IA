import pygame

class MainView:

    def __init__(self) -> None:
        pygame.init()
        window = pygame.display.set_mode((300,300))
        #pygame.display.set_caption("Ma Fenêtre Pygame")

        
    def play(self):
        running = True
        while running : 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
        pygame.quit()

        
