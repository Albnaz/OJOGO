from direcao import Direcao
class Jogador:
    def __init__(self,pID,posx,posy):
        self.pID= pID
        self.direcao = Direcao.DOWN
        self.posx = posx
        self.posy = posy
    
    def getPosX(self):
        return self.posX
    
    def getPosY(self):
        return self.posY
    
    def getDirecao(self):
        return self.direcao
    def __str__(self):
        return "["+str(self.pID)+"]"