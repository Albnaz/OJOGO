from jogador import Jogador
from direcao import Direcao
from contentor import Contentor

def gridgen(gridSizeX,gridSizeY):
    grid=[]
    for i in range(gridSizeY):
        grid.append([])
        for j in range(gridSizeX):
            grid[i].append("[ ]")
    return grid

class Mapa: 
    def __init__(self,sizeX,sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = gridgen(sizeX,sizeY)

    def insertPlayer(self,jogador:Jogador):
        self.grid[jogador.posy][jogador.posx]=jogador

    def insertContainer(self,contentor:Contentor):
        self.grid[contentor.posy][contentor.posx]=contentor

    def interact(self,jogador:Jogador):
        match jogador.getDirecao():
            case Direcao.UP:
                interactingObject = self.grid[jogador.posy-1][jogador.posx]
            case Direcao.DOWN:
                interactingObject = self.grid[jogador.posy+1][jogador.posx]
            case Direcao.LEFT:
                interactingObject = self.grid[jogador.posy][jogador.posx-1]
            case Direcao.RIGHT:
                interactingObject = self.grid[jogador.posy][jogador.posx+1]

        match interactingObject:
            case str():
                print("PORRA NENHUMA")
            case Contentor():
                print("CONTENTOR")
                

    def move(self,jogador:Jogador,dir:Direcao):
        posx=jogador.posx
        posy=jogador.posy
        match dir:
            case Direcao.UP:
                if  posy>0: 
                    if self.grid[jogador.posy-1][jogador.posx] == str():
                        self.grid[posy][posx]="[ ]"
                        jogador.posy-=1
                        self.grid[jogador.posy][posx]=jogador
                    else:
                        print("COLISSION HAPPENED")
                else:
                    print("MOVEERROR")
        
            case Direcao.DOWN:
                if posy<self.sizeY-1: 
                    if self.grid[jogador.posy+1][jogador.posx] == str():
                        self.grid[posy][posx]="[ ]"
                        jogador.posy+=1
                        self.grid[jogador.posy][posx]=jogador
                    else:
                        print("COLISSION HAPPENED")
                else:
                    print("MOVEERROR")
            case Direcao.LEFT:
                if posx>0: 
                    if self.grid[jogador.posy][jogador.posx+1] == str():
                        self.grid[posy][posx]="[ ]"
                        jogador.posx-=1
                        self.grid[posy][jogador.posx]=jogador
                    else:
                        print("COLISSION HAPPENED")
                else:
                    print("MOVEERROR")
        
            case Direcao.RIGHT:
                print(posx)
                if posx<self.sizeX-1: 
                    self.grid[posy][posx]="[ ]"
                    jogador.posx+=1
                    self.grid[posy][jogador.posx]=jogador
                else:
                    print("MOVEERROR")
        jogador.direcao=dir
    
    def __str__(self):
        string=""
        for line in self.grid:
            string+="\n"
            for object in line:
                string+=str(object)
        return string

