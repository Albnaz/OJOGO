from cliente.jogador import Jogador
from direcao import Direcao
from contentor import Contentor
from geradorobjeto import GeradorObjeto 
from clientes import Cliente
from mapa import Mapa
from objetos import Objetos
from pacote import Pacote



mapa=Mapa(11,5)
jogador=Jogador(1,2,2)
jogador2=Jogador(2,8,2)
for line in mapa.grid:
    line[5]= Contentor()
cliente=Cliente("C")
geradorQuadrado=GeradorObjeto(tipo=Objetos.QUADRADO)
geradorTriangulo=GeradorObjeto(tipo=Objetos.TRIANGULO)
geradorRetangulo=GeradorObjeto(tipo=Objetos.RETANGULO)
geradorCirculo=GeradorObjeto(tipo=Objetos.CIRCULO)
pacote = Pacote(3)
mapa.insertGenerator(geradorQuadrado,2,0)
mapa.insertGenerator(geradorCirculo,3,0)
mapa.insertGenerator(geradorTriangulo,1,0)
mapa.insertGenerator(geradorRetangulo,0,0)
mapa.insertPackage(pacote,8,0)
mapa.insertPlayer(jogador)
mapa.insertPlayer(jogador2)
mapa.insertClient(cliente,2,4)
print(mapa)
print(cliente.pedido)

opt=""
while opt != "n":
    opt=input()
    match opt:
        case "w1":
            mapa.move(jogador,Direcao.UP)
        case "s1":
            mapa.move(jogador,Direcao.DOWN)
        case "a1":
            mapa.move(jogador,Direcao.LEFT)
        case "d1":
            mapa.move(jogador,Direcao.RIGHT)
        case "e1":
            mapa.interact(jogador)
            print(jogador.objeto)
        case "w2":
            mapa.move(jogador2,Direcao.UP)
        case "s2":
            mapa.move(jogador2,Direcao.DOWN)
        case "a2":
            mapa.move(jogador2,Direcao.LEFT)
        case "d2":
            mapa.move(jogador2,Direcao.RIGHT)
        case "e2":
            mapa.interact(jogador2)
    print(mapa)
