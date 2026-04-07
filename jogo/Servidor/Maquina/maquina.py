from Servidor.Maquina.lista_clientes import ListaClientes
import socket
import Servidor
from Servidor.Maquina.processaCliente import ProcessaCliente
from Servidor.classes.mapa import Mapa
from Servidor.classes.jogador import Jogador
from dados.dados import Dados

import threading
from Servidor.classes.jogador import Jogador
from Servidor.enums.direcao import Direcao
from Servidor.classes.contentor import Contentor
from Servidor.classes.geradorobjeto import GeradorObjeto
from Servidor.classes.clientes import Cliente
from Servidor.classes.mapa import Mapa
from Servidor.enums.objetos import Objetos
from Servidor.classes.pacote import Pacote
import Servidor
from  Servidor.Maquina.broadast_emissor import ThreadBroadastEmissor
class Maquina:
    def __init__(self):
        self.maxtempo=60
        self.s = socket.socket()
        self.dados = Dados()
        self.s.bind(('', Servidor.PORT))
        self.clientes = ListaClientes()
        self.mapa = Mapa(11, 5)
        self.jogador1 = Jogador(1, 2, 2)
        self.jogador2 = Jogador(2, 8, 2)


    def execute(self):
        self.s.listen(10)
        print("Waiting for clients on port " + str(Servidor.PORT))
        for line in self.mapa.grid:
            line[5] = Contentor()
        geradorQuadrado = GeradorObjeto(tipo=Objetos.QUADRADO)
        geradorTriangulo = GeradorObjeto(tipo=Objetos.TRIANGULO)
        geradorRetangulo = GeradorObjeto(tipo=Objetos.RETANGULO)
        geradorCirculo = GeradorObjeto(tipo=Objetos.CIRCULO)
        pacote = Pacote(3)
        self.mapa.insertGenerator(geradorQuadrado, 2, 0)
        self.mapa.insertGenerator(geradorCirculo, 3, 0)
        self.mapa.insertGenerator(geradorTriangulo, 1, 0)
        self.mapa.insertGenerator(geradorRetangulo, 0, 0)
        self.mapa.insertPackage(pacote, 8, 0)
        self.mapa.insertPlayer(self.jogador1)
        self.mapa.insertPlayer(self.jogador2)
        cliente1 = Cliente("C")
        cliente2 = Cliente("D")
        cliente3 = Cliente("E")
        cliente4 = Cliente("F")

        self.mapa.insertClient(cliente1, 0, 4)
        self.mapa.insertClient(cliente2, 1, 4)
        self.mapa.insertClient(cliente3, 2, 4)
        self.mapa.insertClient(cliente4, 3, 4)
        while True:
            print("On accept...")
            connection, address = self.s.accept()
            if len(self.clientes.clientes) < 2:
                self.clientes.connetar(cliente=[connection, address])
            else:
                print("nao da mais amigo")
            print("Client", address, " connected")
            processo_cliente = ProcessaCliente(connection, address, self.dados, self.clientes, self.mapa, self.jogador1, self.jogador2,self.maxtempo)
            processo_cliente.start()
            broadcast=ThreadBroadastEmissor((self.jogador1,self.jogador2),self.mapa,4,self.maxtempo,self.clientes)
            broadcast.start()