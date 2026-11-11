from math import sqrt, pow

class Complejo:
    def __init__(self, real=0.0, imaginario=0.0):
        self.real = real
        self.imaginario = imaginario

    def __del__(self):
        pass

    def __str__(self):
        cadena = f'{self.real}'
        if self.imaginario<0:
            cadena = cadena + f'{self.imaginario}'
        else:
            cadena = cadena + f'+{self.imaginario}'
        cadena = cadena + 'i'
        return cadena

    def pideleAlUsuarioTuEstado(self):
        self.real = float(input('Dame mi real '))
        self.imaginario = float(input('Dame mi imaginario '))

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, real, imaginario):
        self.real = float(real)
        self.imaginario = float(imaginario)
