import math
from Clases.ClasePunto2D import Punto2D

class RectanguloP:
    def __init__(self, P1=Punto2D(), P2=Punto2D()):
        self.__P1 = P1
        self.__P2 = P2
        self.verificaRectanguloP()
        # print(f'Objeto con P1{self.__P1} P2{self.__P2} construido...')

    @property
    def P1(self):
        return self.__P1

    @P1.setter
    def P1(self, P1):
        self.__P1 = P1
        self.verificaRectanguloP()

    @property
    def P2(self):
        return self.__P2

    @P2.setter
    def P2(self, P2):
        self.__P2 = P2
        self.verificaRectanguloP()

    def __del__(self):
        pass
        # print(f'Objeto con P1 {self.__P1} P2{self.__P2} destruido...')

    def __str__(self):
        cadena = ''
        cadena = cadena + f'P1{self.__P1}\n'
        cadena = cadena + f'P2{self.__P2}\n'
        cadena = cadena + f'Base:\t   {self.dameTuBase()}\n'
        cadena = cadena + f'Altura:    {self.dameTuAltura()}\n'
        cadena = cadena + f'Área:\t   {self.dameTuArea()}\n'
        cadena = cadena + f'Perímetro: {self.dameTuPerimetro()}\n'
        return cadena

    def pideleAlUsuarioTuEstado(self):
        print('P1')
        self.__P1.pideleAlUsuarioTuEstado()
        print('P2')
        self.__P2.pideleAlUsuarioTuEstado()
        self.verificaRectanguloP()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, P1):
        self.__P1 = P1
        self.verificaRectanguloP()

    def dameTuBase(self):
        return math.fabs(self.P1.x - self.P2.x)

    def dameTuAltura(self):
        return math.fabs(self.P1.y - self.P2.y)

    def dameTuArea(self):
        return self.dameTuBase() * self.dameTuAltura()

    def dameTuPerimetro(self):
        return 2*self.dameTuBase() + 2*self.dameTuAltura()

    def verificaRectanguloP(self):
        if not isinstance(self.__P1, Punto2D):
            del self.__P1
            self.__P1 = Punto2D()

        if not isinstance(self.__P2, Punto2D):
            del self.__P2
            self.__P2 = Punto2D()
