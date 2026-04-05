from cliente.jogador.jogador import Jogador
from enums.direcao import Direcao
from servidor.jogo.contentor import Contentor
from servidor.jogo.geradorobjeto import GeradorObjeto
from pacote import Pacote
from servidor.jogo.clientes import Cliente

# ficheiro principal do servidor

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

    def insertContainer(self,contentor:Contentor,x,y):
        self.grid[x][y]=contentor

    def insertGenerator(self,gerador:GeradorObjeto,x,y):
        self.grid[y][x]=gerador
    
    def insertClient(self,cliente:Cliente,x,y):
        self.grid[y][x]=cliente

    def insertPackage(self,pacote:Pacote,x,y):
        self.grid[y][x]=pacote
    

    
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
                if interactingObject.objeto is not None:
                    if jogador.objeto is None: 
                        jogador.objeto = interactingObject.objeto 
                        interactingObject.objeto = None
                        print(jogador.objeto)
                        print(interactingObject.objeto)
                    else:
                        print("OS DOIS TÊM COISAS")
                else: 
                    if jogador.objeto is not None:
                        interactingObject.objeto = jogador.objeto
                        jogador.objeto = None
                        print(jogador.objeto)
                        print(interactingObject.objeto)
                    else:
                        print("OS DOIS N TÊM COISAS")

            case GeradorObjeto():
                if jogador.objeto is None: 
                    jogador.objeto = interactingObject.getTipo()
            
                else:
                    print("O JOGADOR JÁ TEM UMA CENA")
            case Pacote():
                if jogador.objeto is not None:
                    if len(interactingObject.pacote) < interactingObject.maxlen:
                        interactingObject.insertObject(jogador.objeto)
                        jogador.objeto = None
                    else: 
                        print("N DÁ PRA PEGAR")
                else:
                    if len(interactingObject.pacote) < interactingObject.maxlen:
                        jogador.objeto = interactingObject.pacote.pop(-1)
                    else:
                        jogador.objeto = interactingObject.pacote
                        interactingObject.pacote = []

            case Cliente():
                print(interactingObject.getPedido)
                if jogador.objeto is None:
                    print("nao tens nada para entregar")
                else:
                    if jogador.objeto==interactingObject.pedido:
                        print("SUCESSO")
                        
                    else:
                        print("OS COISOS SÃO DIFERENTES")

                        


    def move(self,jogador:Jogador,dir:Direcao): 
        posx=jogador.posx
        posy=jogador.posy
        match dir:
            case Direcao.UP:
                if  posy>0: 
                    if isinstance(self.grid[jogador.posy-1][jogador.posx] ,str):
                        self.grid[posy][posx]="[ ]"
                        jogador.posy-=1
                        self.grid[jogador.posy][posx]=jogador
                    else:
                        print("COLISSION HAPPENED")
                else:
                    print("MOVEERROR")
        
            case Direcao.DOWN:
                if posy<self.sizeY-1: 
                    if isinstance(self.grid[jogador.posy+1][jogador.posx] ,str):
                        self.grid[posy][posx]="[ ]"
                        jogador.posy+=1
                        self.grid[jogador.posy][posx]=jogador
                    else:
                        print("COLISSION HAPPENED")
                else:
                    print("MOVEERROR")
            case Direcao.LEFT:
                if posx>0: 
                    if isinstance(self.grid[jogador.posy][jogador.posx-1] ,str):
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
                    if isinstance(self.grid[jogador.posy][jogador.posx+1] ,str):
                        self.grid[posy][posx]="[ ]"
                        jogador.posx+=1
                        self.grid[posy][jogador.posx]=jogador
                    else:
                        print("COLISSION HAPPENED")
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

