import socket
import json
import Cliente
from Cliente.interface.broadcast_receiver import BroadcastReceiver
# PORT e SERVER ADDRESS

class Interface:
    #def __init__(self, maq:object):
    def __init__(self):
        #self.m:object = maq
        self.connection = socket.socket()
        self.connection.connect((Cliente.SERVER_ADDRESS,Cliente.PORT))

###
    # ----- enviar e receber strings ----- #
    def receive_str(self,connect, n_bytes: int) -> str:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next string read from the current connection
        """
        data = connect.recv(n_bytes)
        return data.decode()

    def send_str(self,connect, value: str) -> None:

        connect.send(value.encode())

    def send_int(self,connect:socket.socket, value: int, n_bytes: int) -> None:

        connect.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

    def receive_int(self,connect: socket.socket, n_bytes: int) -> int:

        data = connect.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)


    #TODO
    # Implement a method that sends and object and returns an object.
    # ...
    def receive_object(self, connection):
        size = self.receive_int(connection, Cliente.INT_SIZE)
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
        self.send_int(connection, size, Cliente.INT_SIZE)
        connection.sendall(data)  # sendall garante envio completo

    ###

    def execute(self):

            receiver=BroadcastReceiver(self.connection)
            receiver.start()
            print("O jogo vai comecar rawr!!!!")
            res = ""

            while res != ".":
                recieve = self.receive_object(self.connection)
                print(recieve)

                print("Movimento: w s a d e ('p' para fim)")
                res: str = input()

                if res =="w":
                    self.send_str(self.connection, Cliente.UP)
                if res =="s":
                    self.send_str(self.connection, Cliente.DOWN)
                if res =="a":
                    self.send_str(self.connection, Cliente.LEFT)
                if res =="d":
                    self.send_str(self.connection, Cliente.RIGHT)
                if res =="e":
                    self.send_str(self.connection, Cliente.INTERACT)
                else:
                    continue


            self.send_str(self.connection, Cliente.END_OP)
            self.connection.close()

