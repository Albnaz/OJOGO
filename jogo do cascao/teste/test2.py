from mapa import Mapa
from cliente.jogador import Jogador
from direcao import Direcao as D
from geradorobjeto import GeradorObjeto
player1=Jogador(1,2,1)
generator=GeradorObjeto("objeto",2,2)
map=Mapa(5,5)
map.insertPlayer(player1)
map.insertGenerator(generator)
print(player1.objeto)
map.interact(player1)
print(player1.objeto)
map.interact(player1)
map.move(player1,D.UP)
print(map)

