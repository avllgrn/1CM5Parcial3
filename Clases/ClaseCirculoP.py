import math
from Clases.ClasePunto2D import Punto2D
from Clases.ClasePunto2D import distanciaEntre

class CirculoP:
    def __init__(self, C=Punto2D(), P=Punto2D()):
        self.__C = C
        self.__P = P
        self.verificaCirculoP()
        # print(f'Objeto con C{self.__C} P{self.__P} construido...')

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, C):
        self.__C = C
        self.verificaCirculoP()

    @property
    def P(self):
        return self.__P

    @P.setter
    def P(self, P):
        self.__P = P
        self.verificaCirculoP()

    def __del__(self):
        pass
        # print(f'Objeto con C {self.__C} P{self.__P} destruido...')

    def __str__(self):
        cadena = ''
        cadena = cadena + f'C{self.C}\n'
        cadena = cadena + f'P{self.P}\n'
        cadena = cadena + f'Radio:\t   {self.dameTuRadio()}\n'
        cadena = cadena + f'Diámetro:  {self.dameTuDiametro()}\n'
        cadena = cadena + f'Área:\t   {self.dameTuArea()}\n'
        cadena = cadena + f'Perímetro: {self.dameTuPerimetro()}\n'
        return cadena

    def pideleAlUsuarioTuEstado(self):
        print('C')
        self.__C.pideleAlUsuarioTuEstado()
        print('P')
        self.__P.pideleAlUsuarioTuEstado()
        self.verificaCirculoP()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, C):
        self.__C = C
        self.verificaCirculoP()

    def dameTuRadio(self):
        return distanciaEntre(self.__C, self.__P)

    def dameTuDiametro(self):
        return 2 * self.dameTuRadio()

    def dameTuArea(self):
        return math.pi * self.dameTuRadio()**2

    def dameTuPerimetro(self):
        return 2 * math.pi * self.dameTuRadio()

    def verificaCirculoP(self):
        if not isinstance(self.__C, Punto2D):
            del self.__C
            self.__C = Punto2D()

        if not isinstance(self.__P, Punto2D):
            del self.__P
            self.__P = Punto2D()
