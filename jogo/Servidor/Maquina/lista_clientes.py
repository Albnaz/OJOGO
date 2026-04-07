class ListaClientes:
    def __init__(self):
        self.clientes=[]

    def connetar(self,cliente:list):
        if cliente[1] not in self.clientes:
            self.clientes.append(cliente)

    def disconectar(self,cliente:list):
        if cliente in self.clientes:
            self.clientes.remove(cliente)

    def listar(self):
        return self.clientes
