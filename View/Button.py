
import pygame

class Button:

    ListButton = []

    def __init__(self,window : pygame.surface.Surface, text :str,  position : (float,float), largeur: float, hauteur : float, colorfont = "black", Colorbg = "white", police = "Arial", font = 10,padding : (float,float) = (2,2)) -> None:
            
        print(type(window))
        self.activate = True
        self.window = window
        self.text = text

        self.position = position

        self.largeur = largeur
        self.hauteur = hauteur

        self.font = font
        self.police = police

        self.colorfont = colorfont
        self.Colorbg = Colorbg
        
        self.padding = padding

        self.ListButton.append(self)
            
    def draw(self):
        if self.activate:
            pygame.draw.rect(self.window,self.Colorbg,pygame.Rect(self.position[0],self.position[1],self.largeur,self.hauteur))

            police = pygame.font.SysFont(self.police,self.font)
            text = police.render(self.text,True,self.colorfont)
            self.window.blit(text,(self.position[0] + self.padding[0] ,self.position[1] + self.padding[1]))
    
    def estClique(self,mouse : (float,float)):
        if self.activate:
            if self.position[0] <= mouse[0] and mouse[0] < self.position[0] + self.largeur: #x
                if self.position[1] <= mouse[1] and mouse[1] < self.position[1] + self.hauteur: #y:
                    return True
        
        return False
    
    def set(self,activate):
        if activate == None:
            raise ValueError
        
        self.activate = activate
    
    def UnBoutonEstClique(self,mouse : (float,float)):
        for button in self.ListButton:
            if button.estClique():
                pass