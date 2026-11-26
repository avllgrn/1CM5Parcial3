from Clases.ClasePersona import *

class Empleado (Persona):
    def __init__(self, Nombre='', Paterno='', Materno='', Genero='', estatura=1.65, FechaNacimiento=Evento(), numeroEmpleado=0, sueldo=7467.9, Puesto='Trabajador'):
            super().__init__( Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento )
            self.__numeroEmpleado = numeroEmpleado
            self.__sueldo = sueldo
            self.__Puesto = Puesto
            self.verificaEmpleado()

    def __del__(self):
        pass

    @property
    def numeroEmpleado(self):
        return self.__numeroEmpleado

    @numeroEmpleado.setter
    def numeroEmpleado(self, numeroEmpleado):
        self.__numeroEmpleado = numeroEmpleado
        self.verificaEmpleado()

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self.__sueldo = sueldo
        self.verificaEmpleado()

    @property
    def Puesto(self):
        return self.__Puesto

    @Puesto.setter
    def Puesto(self, Puesto):
        self.__Puesto = Puesto
        self.verificaEmpleado()

    def __str__(self) -> str:
        datos = super().__str__()
        datos += f'Numero de empleado: {self.__numeroEmpleado}\n'
        datos += f'Sueldo: {self.__sueldo}\n'
        datos += f'Puesto: {self.__Puesto}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        super().pideleAlUsuarioTuEstado()
        self.__numeroEmpleado = input('Dame mi número de empleado ')
        self.__sueldo = input('Dame mi sueldo ')
        self.__Puesto = input('Dame mi puesto ')
        self.verificaEmpleado()

    def muestraTuEstado(self):
        print(self)

    def modificaEmpleado(self, Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento, numeroEmpleado, sueldo, Puesto):
            super().modificaPersona( Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento )
            self.__numeroEmpleado = numeroEmpleado
            self.__sueldo = sueldo
            self.__Puesto = Puesto
            self.verificaEmpleado()

    def verificaEmpleado(self):
        if not isinstance(self.__Puesto,str):
            self.__Puesto = 'Trabajador'

        try:
            self.__numeroEmpleado = int(self.__numeroEmpleado)
        except:
            self.__numeroEmpleado = 0
        try:
            self.__sueldo = float(self.__sueldo)
        except:
            self.__sueldo = 7467.9

        if self.__numeroEmpleado < 0:
            self.__numeroEmpleado = 0

        if self.__sueldo < 7467.9:
            self.__sueldo = 7467.9

