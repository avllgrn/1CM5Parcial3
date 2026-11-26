from Clases.ClasePersona import *

class Empleado (Persona):
    def __init__(self, Nombre='', Paterno='', Materno='', Genero='', estatura=1.65, FechaNacimiento=Evento(), numeroEmpleado=0, sueldo=7467.9, Puesto='Trabajador'):
            super().__init__( Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento )
            self._numeroEmpleado = numeroEmpleado
            self._sueldo = sueldo
            self._Puesto = Puesto
            self.verificaEmpleado()

    def __del__(self):
        pass

    @property
    def numeroEmpleado(self):
        return self._numeroEmpleado

    @numeroEmpleado.setter
    def numeroEmpleado(self, numeroEmpleado):
        self._numeroEmpleado = numeroEmpleado
        self.verificaEmpleado()

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo
        self.verificaEmpleado()

    @property
    def Puesto(self):
        return self._Puesto

    @Puesto.setter
    def Puesto(self, Puesto):
        self._Puesto = Puesto
        self.verificaEmpleado()

    def __str__(self) -> str:
        datos = super().__str__()
        datos += f'Numero de empleado: {self._numeroEmpleado}\n'
        datos += f'Sueldo: {self._sueldo}\n'
        datos += f'Puesto: {self._Puesto}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        super().pideleAlUsuarioTuEstado()
        self._numeroEmpleado = input('Dame mi número de empleado ')
        self._sueldo = input('Dame mi sueldo ')
        self._Puesto = input('Dame mi puesto ')
        self.verificaEmpleado()

    def muestraTuEstado(self):
        print(self)

    def modificaEmpleado(self, Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento, numeroEmpleado, sueldo, Puesto):
            super().__init__( Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento )
            self._numeroEmpleado = numeroEmpleado
            self._sueldo = sueldo
            self._Puesto = Puesto
            self.verificaEmpleado()

    def verificaEmpleado(self):
        if not isinstance(self._Puesto,str):
            self._Puesto = 'Trabajador'

        try:
            self._numeroEmpleado = int(self._numeroEmpleado)
        except:
            self._numeroEmpleado = 0
        try:
            self._sueldo = float(self._sueldo)
        except:
            self._sueldo = 7467.9

        if self._numeroEmpleado < 0:
            self._numeroEmpleado = 0

        if self._sueldo < 7467.9:
            self._sueldo = 7467.9

