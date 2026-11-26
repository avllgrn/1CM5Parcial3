from Clases.ClaseEmpleado import *

class Profesor (Empleado):
    def __init__(self, Nombre='',Paterno='',Materno='',Genero='',estatura=1.65,FechaNacimiento=Evento(),numeroEmpleado=0,sueldo=7467.9,Puesto='Trabajador',numeroGrupos=0,carga=0.0,Academia='Física'):
            super().__init__(  Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento, numeroEmpleado, sueldo, Puesto )
            self.__numeroGrupos = numeroGrupos
            self.__carga = carga
            self.__Academia = Academia
            self.verificaProfesor()

    def __del__(self):
        pass

    @property
    def numeroGrupos(self):
        return self.__numeroGrupos

    @numeroGrupos.setter
    def numeroGrupos(self, numeroGrupos):
        self.__numeroGrupos = numeroGrupos
        self.verificaProfesor()

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, carga):
        self.__carga = carga
        self.verificaProfesor()

    @property
    def Academia(self):
        return self.__Academia

    @Academia.setter
    def Academia(self, Academia):
        self.__Academia = Academia
        self.verificaProfesor()

    def __str__(self) -> str:
        datos = super().__str__()
        datos += f'Numero de grupos: {self.__numeroGrupos}\n'
        datos += f'Carga: {self.__carga}\n'
        datos += f'Academia: {self.__Academia}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        super().pideleAlUsuarioTuEstado()
        self.__numeroGrupos = input('Dame mi número de grupos ')
        self.__carga = input('Dame mi carga ')
        self.__Academia = input('Dame mi academia ')
        self.verificaProfesor()

    def muestraTuProfstado(self):
        print(self)

    def modificaProfesor(self, Nombre='',Paterno='',Materno='',Genero='',estatura=1.65,FechaNacimiento=Evento(),numeroEmpleado=0,sueldo=7467.9,Puesto='Trabajador',numeroGrupos=0,carga=0.0,Academia='Física'):
            super().modificaEmpleado(  Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento, numeroEmpleado, sueldo, Puesto )
            self.__numeroGrupos = numeroGrupos
            self.__carga = carga
            self.__Academia = Academia
            self.verificaProfesor()

    def verificaProfesor(self):
        if not isinstance(self.__Academia,str):
            self.__Academia = 'Computación'

        try:
            self.__numeroGrupos = int(self.__numeroGrupos)
        except:
            self.__numeroGrupos = 0
        try:
            self.__carga = float(self.__carga)
        except:
            self.__carga = 0.0

        if self.__numeroGrupos < 0:
            self.__numeroGrupos = 0

        if self.__carga < 0.0 and self.__carga > 24.0:
            self.__carga = 0.0
