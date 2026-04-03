class GeradorObjeto:
    def __init__(self,tipo,y,x):
        self.tipo=tipo
        self.posy=y
        self.posx=x
    
    def getTipo(self):
        return self.tipo

    def getX(self):
        return self.x

    def getY(self):
        return self.Y

    def __str__(self):
        return "["+str(self.tipo)+"]"

    