from os import system

class Fraccion:
    def __init__(self, numerador=0, denominador=1):
        self.__numerador = numerador
        self.__denominador = denominador
        self.verificaFraccion()

    @property
    def numerador(self):
        return self.__numerador

    @numerador.setter
    def numerador(self, numerador):
        self.__numerador = numerador
        self.verificaFraccion()

    @property
    def denominador(self):
        return self.__denominador

    @denominador.setter
    def denominador(self, denominador):
        self.__denominador = denominador
        self.verificaFraccion()

    def __str__(self):
        estado = f'{self.__numerador}/'
        estado += f'{self.__denominador}'
        return estado
    def del__(self):
        pass

    def pideleAlUsuarioTuEstado(self):
        self.__numerador = input('Dame mi numerador ')
        self.__denominador = input('Dame mi denominador ')
        self.verificaFraccion()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador
        self.verificaFraccion()

    def verificaFraccion(self):
        try:
            self.__numerador = int(self.__numerador)
            self.__denominador = int(self.__denominador)
        except:
            self.__numerador = 0
            self.__denominador = 1

        if self.__denominador<0:
            self.__numerador *= -1
            self.__denominador *= -1

        if self.__denominador==0:
            raise ZeroDivisionError

    def __add__(self, Derecho):
        S = Fraccion()
        S.numerador = self.__numerador*Derecho.denominador + self.__denominador*Derecho.numerador
        S.denominador = self.__denominador*Derecho.denominador
        return S

    def __sub__(self, Derecho):
        R = Fraccion()
        R.numerador = self.__numerador*Derecho.denominador - self.__denominador*Derecho.numerador
        R.denominador = self.__denominador*Derecho.denominador
        return R

    def __mul__(self, Derecho):
        M = Fraccion()
        M.numerador = self.__numerador*Derecho.numerador
        M.denominador = self.__denominador*Derecho.denominador
        return M

    def __truediv__(self, Derecho):
        D = Fraccion()
        D.numerador = self.__numerador*Derecho.denominador
        D.denominador = self.__denominador*Derecho.numerador
        return D
    
def add(Izquierdo, Derecho):
    S = Fraccion()
    S.numerador = Izquierdo.numerador*Derecho.denominador + Izquierdo.denominador*Derecho.numerador
    S.denominador = Izquierdo.denominador*Derecho.denominador
    return S

def sub(Izquierdo, Derecho):
    S = Fraccion()
    S.numerador = Izquierdo.numerador*Derecho.denominador - Izquierdo.denominador*Derecho.numerador
    S.denominador = Izquierdo.denominador*Derecho.denominador
    return S

def mul(Izquierdo, Derecho):
    M = Fraccion()
    M.numerador = Izquierdo.numerador*Derecho.numerador
    M.denominador = Izquierdo.denominador*Derecho.denominador
    return M

def truediv(Izquierdo, Derecho):
    D = Fraccion()
    D.numerador = Izquierdo.numerador*Derecho.denominador
    D.denominador = Izquierdo.denominador*Derecho.numerador
    return D
