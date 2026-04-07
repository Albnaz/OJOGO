class Pacote: 
    def __init__(self,len):
        self.maxlen= len
        self.pacote=[]

    def insertObject(self,object):
        self.pacote.append(object)

    def __str__(self):
        if len(self.pacote)==0:
            return"[◼]"
        elif len(self.pacote) == self.maxlen:
            return "[◫]"
        else:
            return "[◧]"