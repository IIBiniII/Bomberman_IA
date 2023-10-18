from Model import BomberManModel


class MainControleur:

    Model : BomberManModel = None

    #@classmethod
    def setModel(self,model : BomberManModel):
        self.__class__.Model = model

    def OnAction(self,event):
        pass