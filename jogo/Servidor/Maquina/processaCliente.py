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
import json


_mapa_inicializado = False
_lock = threading.Lock()


class ProcessaCliente(threading.Thread):
    def __init__(self, connection, address, dados, clientes, mapa, jogador1, jogador2,tempo):
        super().__init__()
        self.tempo=tempo
        self.connection = connection
        self.address = address
        self.dados = dados
        self.clientes = clientes
        self.mapa = mapa
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def receive_int(self, connection, n_bytes):
        data = connection.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)

    def send_int(self, connection, value, n_bytes):
        connection.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

    def receive_str(self, connection, n_bytes):
        data = connection.recv(n_bytes)
        return data.decode()

    def send_str(self, connection, value):
        connection.send(value.encode())

    def receive_object(self, connection):
        size = self.receive_int(connection, Servidor.INT_SIZE)
        data = b""
        while len(data) < size:
            packet = connection.recv(size - len(data))
            if not packet:
                raise ConnectionError("Ligação perdida")
            data += packet
        return json.loads(data.decode('utf-8'))

    def send_object(self, connection, obj):
        data = json.dumps(obj).encode('utf-8')
        size = len(data)
        self.send_int(connection, size, Servidor.INT_SIZE)
        connection.sendall(data)  # sendall garante envio completo
    ###

    def run(self):

        print(self.address, "Thread iniciada")
        while True:
            # 1º envia o mapa ao próprio cliente
            self.send_object(self.connection, self.mapa.simplify())
            # 2º recebe o comando
            request_type = self.receive_str(self.connection, Servidor.COMMAND_SIZE)
            print(request_type)
            # 3º processa o comando
            isPlayer1 = self.clientes.clientes[0][1] == self.address
            print(isPlayer1)
            if isPlayer1:
                jogador=self.jogador1
            else:
                jogador=self.jogador2

            if request_type == Servidor.UP:
                self.mapa.move(jogador, Direcao.UP)
            elif request_type == Servidor.DOWN:
                self.mapa.move(jogador, Direcao.DOWN)
            elif request_type == Servidor.LEFT:
                self.mapa.move(jogador, Direcao.LEFT)
            elif request_type == Servidor.RIGHT:
                self.mapa.move(jogador, Direcao.RIGHT)
            elif request_type == Servidor.INTERACT:
                self.mapa.interact(jogador)


            # 4º envia o mapa atualizado aos OUTROS clientes
            print(self.mapa)
