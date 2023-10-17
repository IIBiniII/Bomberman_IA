from View import Game

class ControleurPlayBoutonMenu:

    def __init__(self,View) -> None:
        self.view = View

    def onAction(self,event):

        self.view.goTo(Game(self.view))