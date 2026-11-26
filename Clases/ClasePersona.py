from Clases.ClaseEvento import *

class Persona:
    def __init__(self, Nombre='', Paterno='', Materno='', Genero='', estatura=0.24, FechaNacimiento=Evento()):
        self._Nombre = Nombre
        self._Paterno = Paterno
        self._Materno = Materno
        self._Genero = Genero
        self._estatura = estatura
        self._FechaNacimiento = FechaNacimiento
        self.verificaPersona()

    def __del__(self):
        pass

    @property
    def Nombre(self):
        return self._Nombre
    
    @Nombre.setter
    def Nombre(self, Nombre):
        self._Nombre = Nombre
        self.verificaPersona()

    @property
    def Paterno(self):
        return self._Paterno
    
    @Paterno.setter
    def Paterno(self, Paterno):
        self._Paterno = Paterno
        self.verificaPersona()

    @property
    def Materno(self):
        return self._Materno
    
    @Materno.setter
    def Materno(self, Materno):
        self._Materno = Materno
        self.verificaPersona()

    @property
    def Genero(self):
        return self._Genero
    
    @Genero.setter
    def Genero(self, Genero):
        self._Genero = Genero
        self.verificaPersona()

    @property
    def estatura(self):
        return self._estatura
    
    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura
        self.verificaPersona()

    @property
    def FechaNacimiento(self):
        return self._FechaNacimiento
    
    @FechaNacimiento.setter
    def FechaNacimiento(self, FechaNacimiento):
        self._FechaNacimiento = FechaNacimiento
        self.verificaPersona()

    def __str__(self) -> str:
        datos = f'Nombre: {self._Nombre}\n'
        datos += f'Paterno: {self._Paterno}\n'
        datos += f'Materno: {self._Materno}\n'
        datos += f'Genero: {self._Genero}\n'
        datos += f'estatura: {self._estatura}\n'
        datos += f'FechaNacimiento: {self._FechaNacimiento}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        self._Nombre = input('Dame mi Nombre ')
        self._Paterno = input('Dame mi Paterno ')
        self._Materno = input('Dame mi Materno ')
        self._Genero = input('Dame mi Genero ')
        self._estatura = input('Dame mi estatura ')
        print('Dame mi Fecha de Nacimiento')
        self._FechaNacimiento.pideleAlUsuarioTuEstado()
        self.verificaPersona()
    
    def muestraTuEstado(self):
        print(self)

    def modificaPersona(self, Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento):
        self._Nombre = Nombre
        self._Paterno = Paterno
        self._Materno = Materno
        self._Genero = Genero
        self._estatura = estatura
        self._FechaNacimiento = FechaNacimiento
        self.verificaPersona()

    def verificaPersona(self):
        if not isinstance(self._Nombre,str):
            self._Nombre = ''

        if not isinstance(self._Paterno,str):
            self._Paterno = ''

        if not isinstance(self._Materno,str):
            self._Materno = ''

        if not isinstance(self._Genero,str):
            self._Genero = ''

        try:
            self._estatura = float(self._estatura)
        except:
            self._estatura = 0.24

        if self._estatura<0.24 or self._estatura>2.72:
            self._estatura = 0.24

        if not isinstance(self._FechaNacimiento, Evento):
            self._FechaNacimiento = Evento()
