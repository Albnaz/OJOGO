from mapa import Mapa
from jogador import Jogador
from direcao import Direcao as D
from contentor import Contentor
player1=Jogador(1,2,3)
container=Contentor()
map=Mapa(5,5)
map.insertPlayer(player1)
map.insertContainer(container)
map.interact(player1)
map.move(player1,D.UP)
print(map)

