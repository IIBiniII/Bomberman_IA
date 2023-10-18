from View import TrainView,OptionView

from Controller import *


class ControleurEntrainementIABouton(MainControleur):

    def __init__(self,View) -> None:
        self.view : OptionView = View

    
    def OnAction(self,event):


        self.view.goTo(TrainView(self.view,MainControleur.Model.nbGen))