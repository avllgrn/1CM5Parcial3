from Clases.ClasePunto2D import *

class Punto3D (Punto2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.__z = z
        self.verificaTuEstado()

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, valor):
        self.__z = valor
        self.verificaTuEstado()

    def __str__(self):
        return f'({self.x}, {self.y}, {self.__z})'

    def verificaTuEstado(self):
        super().verificaTuEstado()
        try:
            self.__z = float(self.__z)
        except:
            self.__z = 0.0

    def pideleAlUsuarioTuEstado(self):
        super().pideleAlUsuarioTuEstado()
        self.__z = input('Dame mi z ')
        self.verificaTuEstado()

    def modificaTuEstado(self, x, y, z):
        super().modificaTuEstado(x, y)
        self.__z = z
        self.verificaTuEstado()
