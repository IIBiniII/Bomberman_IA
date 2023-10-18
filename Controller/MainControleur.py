from Model import BomberManModel


class MainControleur:

    Model : BomberManModel = None

    def setModel(self,model : BomberManModel):
        self.__class__.Model = model