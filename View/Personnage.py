from tkinter import *
import keyboard as kb

class Player(Canvas) : 
    def __init__(self,master,name:str,w,h)->None:

        super().__init__(master,width=w,height=h,highlightbackground="red", highlightthickness=2)
        #highlightbackground="blue", highlightthickness=2

        self.speed = 0.05
        self.posX = 5
        self.posY = 5
        self.name = name
        #Init of bonuses
        self.fire_range = 3
        self.fire_bonus = 0
        self.bomb_bonus = 0
        self.angel_bonus_time = 0
        self.boot_bonus = 0 
        
        self.create_player()
        self.focus_set()


    def create_player(self):
        self.rect = self.create_rectangle(self.posX, self.posY, self.posX + 20, self.posY + 20, fill="blue")

    def move_to(self, x=0, y=0):
        self.posX += x
        self.posY += y
        self.move(self.rect, x, y)
        
    def move_left(self):
        if self.posX -self.speed > 0:
            self.move_to(-self.speed)
    
    def move_right(self):
        if self.posX +self.speed < self.winfo_width()-20:
            self.move_to(self.speed)

    def move_top(self):
        if self.posY -self.speed > 0:
            self.move_to(y=-self.speed)

    def move_bottom(self):
        if self.posY +self.speed < self.winfo_height()-20:
            self.move_to(y=self.speed)

    def moveif(self):
        
        if kb.is_pressed("q"):
            self.move_left()
        if kb.is_pressed("d"):
            self.move_right()
        if kb.is_pressed("z"):
            self.move_top()
        if kb.is_pressed("s"):
            self.move_bottom()