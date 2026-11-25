class Hora:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo
        self.verificaTuEstado()

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, valor):
        self.__hora = valor
        self.verificaTuEstado()

    @property
    def minuto(self):
        return self.__minuto

    @minuto.setter
    def minuto(self, valor):
        self.__minuto = valor
        self.verificaTuEstado()

    @property
    def segundo(self):
        return self.__segundo

    @segundo.setter
    def segundo(self, valor):
        self.__segundo = valor
        self.verificaTuEstado()

    def __str__(self):
        return f'{self.__hora}:{self.__minuto}:{self.__segundo}'

    def pideleAlUsuarioTuEstado(self):
        self.__hora = input('Dame mi hora ')
        self.__minuto = input('Dame mi minuto ')
        self.__segundo = input('Dame mi segundo ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, hora, minuto, segundo):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo
        self.verificaTuEstado()

    def verificaTuEstado(self):
        try:
            self.__hora = int(self.__hora)
        except:
            self.__hora = 0
        try:
            self.__minuto = int(self.__minuto)
        except:
            self.__minuto = 0
        try:
            self.__segundo = int(self.__segundo)
        except:
            self.__segundo = 0

        if self.__hora<0 or self.__hora>23:
            self.__hora = 0            
        if self.__minuto<0 or self.__minuto>59:
            self.__minuto = 0
        if self.__segundo<0 or self.__segundo>59:
            self.__segundo = 0
