from os import system
from Clases.ClaseFecha import *
from Clases.ClaseHora import *

class Evento:
    def __init__(self, F = Fecha(), H = Hora()):
        self.__F = F
        self.__H = H
        self.verificaTuEstado()

    def __del__(self):
        pass

    @property
    def F(self):
        return self.__F
    
    @F.setter
    def F(self, F):
        self.__F = F
        self.verificaTuEstado()

    @property
    def H(self):
        return self.__H
    
    @H.setter
    def H(self, H):
        self.__H = H
        self.verificaTuEstado()

    def __str__(self) -> str:
        return f'{self.__F} {self.__H}'

    def pideleAlUsuarioTuEstado(self):
        print('Dame mi F ')
        self.__F.pideleAlUsuarioTuEstado()
        print('Dame mi H')
        self.__H.pideleAlUsuarioTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, F, H):
        self.__F = F
        self.__H = H
        self.verificaTuEstado()

    def verificaTuEstado(self):
        if not isinstance(self.__F, Fecha):
            self.__F = Fecha()

        if not isinstance(self.__H, Hora):
            self.__H = Hora()

