from enum import Enum
class Objetos(Enum):
    def __str__(self):
        return self.value
    CIRCULO = "◯"
    TRIANGULO = "△"
    QUADRADO = "◻"
    RETANGULO="▭"
    