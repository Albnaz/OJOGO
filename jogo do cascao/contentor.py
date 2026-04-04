class Contentor: 
    def __init__(self):
        self.objeto = None
        self.ID=5



    def __str__(self):
        if self.objeto == None:
            return "[⛶]"
        if self.objeto == list():
            return "[◫]"
        else:
            return "["+str(self.objeto)+"]"
