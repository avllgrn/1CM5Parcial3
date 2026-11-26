from Clases.ClaseEvento import *

class Persona:
    def __init__(self, Nombre='', Paterno='', Materno='', Genero='', estatura=0.24, FechaNacimiento=Evento()):
        self.__Nombre = Nombre
        self.__Paterno = Paterno
        self.__Materno = Materno
        self.__Genero = Genero
        self.__estatura = estatura
        self.__FechaNacimiento = FechaNacimiento
        self.verificaPersona()

    def __del__(self):
        pass

    @property
    def Nombre(self):
        return self.__Nombre
    
    @Nombre.setter
    def Nombre(self, Nombre):
        self.__Nombre = Nombre
        self.verificaPersona()

    @property
    def Paterno(self):
        return self.__Paterno
    
    @Paterno.setter
    def Paterno(self, Paterno):
        self.__Paterno = Paterno
        self.verificaPersona()

    @property
    def Materno(self):
        return self.__Materno
    
    @Materno.setter
    def Materno(self, Materno):
        self.__Materno = Materno
        self.verificaPersona()

    @property
    def Genero(self):
        return self.__Genero
    
    @Genero.setter
    def Genero(self, Genero):
        self.__Genero = Genero
        self.verificaPersona()

    @property
    def estatura(self):
        return self.__estatura
    
    @estatura.setter
    def estatura(self, estatura):
        self.__estatura = estatura
        self.verificaPersona()

    @property
    def FechaNacimiento(self):
        return self.__FechaNacimiento
    
    @FechaNacimiento.setter
    def FechaNacimiento(self, FechaNacimiento):
        self.__FechaNacimiento = FechaNacimiento
        self.verificaPersona()

    def __str__(self) -> str:
        datos = f'Nombre: {self.__Nombre}\n'
        datos += f'Paterno: {self.__Paterno}\n'
        datos += f'Materno: {self.__Materno}\n'
        datos += f'Genero: {self.__Genero}\n'
        datos += f'estatura: {self.__estatura}\n'
        datos += f'FechaNacimiento: {self.__FechaNacimiento}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        self.__Nombre = input('Dame mi Nombre ')
        self.__Paterno = input('Dame mi Paterno ')
        self.__Materno = input('Dame mi Materno ')
        self.__Genero = input('Dame mi Genero ')
        self.__estatura = input('Dame mi estatura ')
        print('Dame mi Fecha de Nacimiento')
        self.__FechaNacimiento.pideleAlUsuarioTuEstado()
        self.verificaPersona()
    
    def muestraTuEstado(self):
        print(self)

    def modificaPersona(self, Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento):
        self.__Nombre = Nombre
        self.__Paterno = Paterno
        self.__Materno = Materno
        self.__Genero = Genero
        self.__estatura = estatura
        self.__FechaNacimiento = FechaNacimiento
        self.verificaPersona()

    def verificaPersona(self):
        if not isinstance(self.__Nombre,str):
            self.__Nombre = ''

        if not isinstance(self.__Paterno,str):
            self.__Paterno = ''

        if not isinstance(self.__Materno,str):
            self.__Materno = ''

        if not isinstance(self.__Genero,str):
            self.__Genero = ''

        try:
            self.__estatura = float(self.__estatura)
        except:
            self.__estatura = 0.24

        if self.__estatura<0.24 or self.__estatura>2.72:
            self.__estatura = 0.24

        if not isinstance(self.__FechaNacimiento, Evento):
            self.__FechaNacimiento = Evento()
