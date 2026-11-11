from math import sqrt, pow

class Punto2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __del__(self):
        pass

    def __str__(self):
        return f'({self.x}, {self.y})'

    def pideleAlUsuarioTuEstado(self):
        self.x = float(input('Dame mi x '))
        self.y = float(input('Dame mi y '))

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, Derecho):
        S = Punto2D()
        S.x = self.x + Derecho.x
        S.y = self.y + Derecho.y
        return S

    def __sub__(self, Derecho):
        S = Punto2D()
        S.x = self.x - Derecho.x
        S.y = self.y - Derecho.y
        return S

def add(P1, P2):
    P3 = Punto2D()
    P3.x = P1.x + P2.x
    P3.y = P1.y + P2.y
    return P3

def sub(P1, P2):
    P3 = Punto2D()
    P3.x = P1.x - P2.x
    P3.y = P1.y - P2.y
    return P3
