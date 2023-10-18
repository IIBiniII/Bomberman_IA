

class Box:

    def __init__(self,x,y,canBroke = False) -> None:
        self.x = x
        self.y = y 
        self.broken = False
        self.canBroke = canBroke