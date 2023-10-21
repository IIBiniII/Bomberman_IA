from Model import Player
from Model.Game import Game
from Model.Box import Box


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
            police = pygame.font.SysFont("Arial", 10)
            text = police.render(player.name, True, "black")
            self.window.blit(text, (player.posX - 10, player.posY - 20))
            pygame.draw.circle(self.window, pygame.color.Color(0, 200, 50), (player.posX, player.posY), 5, 3)
            keys = pygame.key.get_pressed()

            case_x, case_y = player.player_case()  # Récupérez les coordonnées de la case actuelle du joueur

            if keys[pygame.K_z]:
                new_posY = player.posY - player.speed
                if new_posY >= 0:
                    new_case_y = max(0, self.get_Case(player.posX,player.posY-player.speed)[1])
                    if self.game.map.Carte[new_case_y][case_x] != 0 and not self.game.map.is_box_at(case_x, new_case_y):
                        player.moveTo(0, -player.speed)

            if keys[pygame.K_s]:
                new_posY = player.posY + player.speed
                if new_posY <= self.window_height:
                    new_case_y = min(15, self.get_Case(player.posX,player.posY+player.speed)[1])
                    if self.game.map.Carte[new_case_y][case_x] != 0 and not self.game.map.is_box_at(case_x, new_case_y):
                        player.moveTo(0, player.speed)

            if keys[pygame.K_q]:
                new_posX = player.posX - player.speed
                if new_posX >= 0:
                    new_case_x = max(0, self.get_Case(player.posX-player.speed,player.posY)[0])
                    if self.game.map.Carte[case_y][new_case_x] != 0 and not self.game.map.is_box_at(new_case_x, case_y):
                        player.moveTo(-player.speed, 0)

            if keys[pygame.K_d]:
                new_posX = player.posX + player.speed
                if new_posX <= self.window_width:
                    new_case_x = min(15, self.get_Case(player.posX+player.speed,player.posY)[0])

                    if self.game.map.Carte[case_y][new_case_x] != 0 and not self.game.map.is_box_at(new_case_x, case_y):
                        player.moveTo(player.speed, 0)
            if keys[pygame.K_SPACE]:
                if player.last_move[1]<0:
                    print("Placer bombe en Haut")
                if player.last_move[1]>0:
                    print("Placer bombe en Bas")
                if player.last_move[0]<0:
                    print("Placer bombe à Gauche")
                if player.last_move[0]>0:
                    print("Placer bombe à Droite")

    def get_Case(self, posX, posY) -> (int, int):
        x, y = (posX - 17) / (465 / 15), (posY - 17) / (465 / 15)
        return int(x), int(y)
    
    def update_boxes(self):
        for box in self.game.boxes:
            if not box.broken : 
                self.window.blit(box.box_image, (box.x*(465/15)+17,box.y*(465/15)+17))


