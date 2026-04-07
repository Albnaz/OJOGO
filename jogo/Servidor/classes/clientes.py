import random as rand
from Servidor.enums.objetos import Objetos

def randomizar():
    lista=[]
    objetos=[Objetos.QUADRADO,Objetos.TRIANGULO,Objetos.RETANGULO,Objetos.CIRCULO]
    for  i in range(3):
        lista.append(objetos[rand.randint(0,len(objetos)-1)])
    return lista 

class Cliente:
    def __init__(self,ID):
        self.ID=ID
        self.tempo=10
        self.pedido=randomizar()

    def getId(self):
        return self.ID
    def getEspera(self):
        return self.espera
    
    def getPedido(self):
        return self.pedido
    
    def mudarpedido(self):
        self.pedido=[randomizar()]

    def __str__(self):
        return "["+str(self.ID)+"]"
