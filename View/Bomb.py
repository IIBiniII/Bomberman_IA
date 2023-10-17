from tkinter import *
import threading

class Bomb:
    def __init__(self,canva:Canvas,x,y,w,h) -> None:

        self.posX = x
        self.posY = y
        self.canva = canva
        self.create_bomb()
        timer = threading.Timer(1, self.active)  
        timer.start()


        
    def create_bomb(self):
        self.bomb =self.canva.create_oval(self.posX, self.posY, self.posX + 20, self.posY + 20, fill="black",tags="bomb")

    def active(self):
        del self.bomb #Revoir la suppression de la bombe