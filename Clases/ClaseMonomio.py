from os import system

class Monomio:
    def __init__(self, coeficiente=1, exponente=0):
        self.__coeficiente = coeficiente
        self.__exponente = exponente
        self.verificaMonomio()

    def __del__(self):
        pass

    @property
    def coeficiente(self):
        return self.__coeficiente

    @coeficiente.setter
    def coeficiente(self, coeficiente):
        self.__coeficiente = coeficiente
        self.verificaMonomio()

    @property
    def exponente(self):
        return self.__exponente

    @exponente.setter
    def exponente(self, exponente):
        self.__exponente = exponente
        self.verificaMonomio()

    def __str__(self) -> str:
        return f'{self.__coeficiente}x^{self.__exponente}'

    def muestraTuEstado(self):
        print(self)

    def pideleAlUsuarioTuEstado(self):
        self.__coeficiente = input('Dame mi coeficiente ')
        self.__exponente = input('Dame mi exponente ')
        self.verificaMonomio()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, coeficiente, exponente):
        self.__coeficiente = coeficiente
        self.__exponente = exponente
        self.verificaMonomio()

    def verificaMonomio(self):
        try:
            self.__coeficiente = float(self.__coeficiente)
            self.__exponente = float(self.__exponente)
        except:
            self.__coeficiente = 1.0
            self.__exponente = 0.0

        if self.__coeficiente == 0.0 and self.__exponente == 0.0:
            raise ValueError('Coeficiente y exponente indeterminados...')