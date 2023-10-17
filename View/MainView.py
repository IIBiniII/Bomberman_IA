from tkinter import *
import View
class MainView(Tk):


    def __init__(self) -> None:
        
        super().__init__()
        self.geometry("500x500")
        self.runing = True
        self.protocol("WM_DELETE_WINDOW", self.stop)

        self.page = View.Menu(self)
        self.configure(bg="light blue")

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

    def stop(self):
        self.runing = False
    
    def start(self):
        while self.runing:
            if type(self.page) is View.Game:
                self.page.player.moveif()
            self.update()
