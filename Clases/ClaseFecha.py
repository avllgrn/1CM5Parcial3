class Fecha:
    def __init__(self, dia=1, mes=1, anio=2026):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.verificaTuEstado()

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, valor):
        self.__dia = valor
        self.verificaTuEstado()

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, valor):
        self.__mes = valor
        self.verificaTuEstado()

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, valor):
        self.__anio = valor
        self.verificaTuEstado()

    def __str__(self):
        return f'{self.__dia}/{self.__mes}/{self.__anio}'

    def pideleAlUsuarioTuEstado(self):
        self.__dia = input('Dame mi dia ')
        self.__mes = input('Dame mi mes ')
        self.__anio = input('Dame mi anio ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, dia, mes, anio):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.verificaTuEstado()

    def verificaTuEstado(self):
        try:
            self.__dia = int(self.__dia)
        except:
            self.__dia = 1
        try:
            self.__mes = int(self.__mes)
        except:
            self.__mes = 1
        try:
            self.__anio = int(self.__anio)
        except:
            self.__anio = 2026

        
        if self.__anio<0:
            self.__anio = 2026
        elif esBiciesto(self.__anio) and self.__mes==2 and self.dia>29:
            self.__dia = 1
        elif not esBiciesto(self.__anio) and self.__mes==2 and self.dia>28:
            self.__dia = 1
        
        if self.__mes<1 or self.__mes>12:
            self.__mes = 1
        elif (self.__mes==1 or self.__mes==3 or self.__mes==5 or self.__mes==7 or self.__mes==8 or self.__mes==10 or self.__mes==12) and self.__dia>31:
            self.__dia=1
        elif (self.__mes==4 or self.__mes==6 or self.__mes==9 or self.__mes==11) and self.__dia>30:
            self.__dia=1

        if self.__dia<1 or self.__dia>31:
            self.__dia = 1

def esBiciesto(anio):
    if anio%4 == 0 or anio%400 == 0:
        return True
    else:
        return False
