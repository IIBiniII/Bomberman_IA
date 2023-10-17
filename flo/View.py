from tkinter import *


class Game(Frame):
    
    def __init__(self,master):
        super().__init__(master)

        player = Label(self,text="player 1")
        player.pack()#place(x=10,y=10)


class ControlerBoutonPlay:

    def __init__(self,View) -> None:
        self.view = View

    def onAction(self,event):
        print("play")
        print(type(self.view))
        self.view.goTo(Game(self.view))


class Menu(Frame):

    def __init__(self,master):

        super().__init__(master)

        controleurplay = ControlerBoutonPlay(self.master)

        self.boutonPlay = Button(self,text="play")
        self.boutonPlay.bind("<Button-1>",controleurplay.onAction)

        self.boutonPlay.grid(row=0,column=0)


class MainView(Tk):


    def __init__(self) -> None:
        
        super().__init__()
        self.page = Menu(self)
        self.history = [self.page]

        self.page.pack()

    def goBack(self):
        self.page.forget()
        self.page = self.history[-1]
        del self.history[-1]
        self.page.pack()

    def goTo(self,pannel : Frame):
        self.page.forget()
        self.history.append(self.page)
        self.page = pannel
        self.page.pack()






f = MainView()
f.mainloop()