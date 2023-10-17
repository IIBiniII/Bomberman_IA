from tkinter import *
import keyboard as kb

class Player(Canvas) : 
    def __init__(self,master,name:str)->None:

        super().__init__(master,highlightbackground="red", highlightthickness=2)
        #highlightbackground="blue", highlightthickness=2

        self.speed = 1
        self.posX = 5
        self.posY = 5
        self.name = name
        #Init of bonuses
        self.fire_range = 3
        self.fire_bonus = 0
        self.bomb_bonus = 0
        self.angel_bonus_time = 0
        self.boot_bonus = 0 



        #Movement
        self.left_pressed = False
        self.right_pressed = False
        self.top_pressed = False
        self.bottom_pressed = False

        #Bind 
        self.bind("<KeyPress>", self.on_key_press)
        self.bind("<KeyRelease>", self.on_key_release)
        
        self.create_player()
        self.focus_set()


    def create_player(self):
        self.rect = self.create_rectangle(self.posX, self.posY, self.posX + 20, self.posY + 20, fill="blue")

    def move(self, x=0, y=0):
        self.delete("all")
        self.posX += x
        self.posY += y
        #self.move(self.rect, x, y)
        
    def move_left(self):
        self.move(-self.speed)
    
    def move_right(self):
        self.move(self.speed)

    def move_top(self):
        self.move(y=-self.speed)

    def move_bottom(self):
        self.move(y=self.speed)

    def update_move(self):
        while self.left_pressed or self.right_pressed or self.top_pressed or self.bottom_pressed:
            if self.left_pressed:
                self.move_left()
            if self.right_pressed:
                self.move_right()
            if self.top_pressed:
                self.move_top()
            if self.bottom_pressed:
                self.move_bottom()

    def on_key_press(self,event):
        if kb.is_pressed("z"):
            self.top_pressed = True
        if kb.is_pressed("s"):
            self.bottom_pressed = True
        if kb.is_pressed("q"):
            self.left_pressed = True
        if kb.is_pressed("d"):
            self.right_pressed = True
        self.update_move()

    def on_key_release(self,event):
        if not kb.is_pressed("z"):
            self.top_pressed = False
        if not kb.is_pressed("s"):
            self.bottom_pressed = False
        if not kb.is_pressed("q"):
            self.left_pressed = False
        if not kb.is_pressed("d"):
            self.right_pressed = False

