from math import sqrt, pow

class Punto2D:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
        self.verificaTuEstado()

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        self.__x = valor
        self.verificaTuEstado()

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valor):
        self.__y = valor
        self.verificaTuEstado()

    def __del__(self):
        pass

    def __str__(self):
        return f'({self.__x}, {self.__y})'

    def pideleAlUsuarioTuEstado(self):
        self.__x = input('Dame mi x ')
        self.__y = input('Dame mi y ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, x, y):
        self.__x = x
        self.__y = y
        self.verificaTuEstado()

    def verificaTuEstado(self):
        try:
            self.__x = float(self.__x)
        except:
            self.__x = 0.0

        try:
            self.__y = float(self.__y)
        except:
            self.__y = 0.0

    def __add__(self, Derecho):
        S = Punto2D()
        if isinstance(Derecho, Punto2D):
            S.__x = self.__x + Derecho.__x
            S.__y = self.__y + Derecho.__y
        return S

    def __sub__(self, Derecho):
        S = Punto2D()
        if isinstance(Derecho, Punto2D):
            S.__x = self.__x - Derecho.__x
            S.__y = self.__y - Derecho.__y
        return S

def add(P1, P2):
    P3 = Punto2D()
    if isinstance(P1, Punto2D) and isinstance(P2, Punto2D):
        P3.x = P1.__x + P2.__x
        P3.y = P1.__y + P2.__y
    return P3

def sub(P1, P2):
    P3 = Punto2D()
    if isinstance(P1, Punto2D) and isinstance(P2, Punto2D):
        P3.x = P1.__x - P2.__x
        P3.y = P1.__y - P2.__y
    return P3

def distanciaEntre(P1:Punto2D, P2:Punto2D):
    return sqrt( pow(P2.y - P1.y, 2) + pow(P2.x - P1.x, 2) )

def pendienteDados(P1:Punto2D, P2:Punto2D):
    return (P2.y - P1.y) / (P2.x - P1.x)
