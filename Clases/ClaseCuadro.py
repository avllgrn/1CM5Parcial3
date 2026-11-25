class Cuadro:
    def __init__(self, lado=0.0):
        self.__lado = lado
        self.verificaTuEstado()

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, valor):
        self.__lado = valor
        self.verificaTuEstado()

    def __str__(self):
        estado = ''
        estado += f'Lado:\t   {self.__lado}\n'
        estado += f'Área:\t   {self.dameTuArea()}\n'
        estado += f'Perímetro: {self.dameTuPerimetro()}\n'
        return estado

    def pideleAlUsuarioTuEstado(self):
        self.__lado = input('Dame mi lado ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def dameTuArea(self):
        return self.lado**2

    def dameTuPerimetro(self):
        return self.lado*4

    def verificaTuEstado(self):
        try:
            self.__lado = float(self.__lado)
        except:
            self.__lado = 0.0

        if self.__lado < 0:
            self.__lado = 0.0
