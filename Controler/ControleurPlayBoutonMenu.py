from View import Game

class ControleurPlayBoutonMenu:

    def __init__(self,View) -> None:
        self.view = View

    def onAction(self,event):
        print("play")
        print(type(self.view))
        self.view.goTo(Game(self.view))