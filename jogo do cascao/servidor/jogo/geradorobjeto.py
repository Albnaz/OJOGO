class GeradorObjeto:
    def __init__(self,tipo):
        self.tipo=tipo

    
    def getTipo(self):
        return self.tipo



    def __str__(self):
        return "["+str(self.tipo)+"]"

    