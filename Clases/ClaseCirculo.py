import math

class Circulo:
    def __init__(self, radio=0.0):
        self.__radio = radio
        self.verificaCirculo()
        # print(f'Objeto con radio {self.__radio} construido...')

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, radio):
        self.__radio = radio
        self.verificaCirculo()

    def __del__(self):
        pass
        # print(f'Objeto con radio {self.__radio} destruido...')

    def __str__(self):
        cadena = ''
        cadena = cadena + f'Radio: {self.__radio}\n'
        cadena = cadena + f'Diámetro: {self.dameTuDiametro()}\n'
        cadena = cadena + f'Área: {self.dameTuArea()}\n'
        cadena = cadena + f'Perímetro: {self.dameTuPerimetro()}\n'
        return cadena

    def pideleAlUsuarioTuEstado(self):
        self.__radio = input('Dame mi radio ')
        self.verificaCirculo()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, radio):
        self.__radio = radio
        self.verificaCirculo()

    def dameTuDiametro(self):
        return 2 * self.__radio

    def dameTuArea(self):
        return math.pi * self.__radio**2

    def dameTuPerimetro(self):
        return 2 * math.pi * self.__radio

    def verificaCirculo(self):
        try:
            self.__radio = float(self.__radio)
        except:
            self.__radio = 0.0

        if self.__radio<0:
            self.__radio = 0.0
