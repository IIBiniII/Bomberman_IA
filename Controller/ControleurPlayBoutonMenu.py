from View import GameView

class ControleurPlayBoutonMenu:

    def __init__(self,View) -> None:
        self.view = View

    def onAction(self,event):
        #self.view.goTo(Game(self.view)) # --> Remplacer par la vue d'option suivante
        self.view.game = GameView()