import subprocess
from Clases.ClaseEmpleado import *

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    E1 = Empleado()
    print(f'E1')
    E1.muestraTuEstado()

    FN = Evento( Fecha(1,2,2003),Hora(4,5,6) )
    E2 = Empleado('Juan','Perez','Lopez','m',1.82,FN,2,4967.6,'Intendente')
    print(f'E2\n{E2}')

    E3 = Empleado(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'mil', 'un millón', 56.78)
    print(f'E5\n{E3}')

    print(f'E1\n{E1}')
    print(f'E1')
    E1.pideleAlUsuarioTuEstado()
    print(f'\nE1\n{E1}')    

    print('Se intenta E1.modificaEmpleado(1, 2.3, 4, 5.6, \'uno ochenta\', 789, \'mil\', \'un millón\', 56.78)')
    E1.modificaEmpleado(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'mil', 'un millón', 56.78)
    print(f'\nE1\n{E1}')

    print('Se intenta asignar valores incorrectos a los atributos')
    E1.Nombre = 1
    E1.Paterno = 2.3
    E1.Materno = 4
    E1.Genero = 5.6
    E1.estatura = 'uno ochenta'
    E1.FechaNacimiento = 789
    E1.numeroEmpleado = 'uno dos tres cuatro'
    E1.sueldo = 'siete mil cuatrocientos sesenta y siete punto nueve'
    E1.Puesto = 456.654
    print(f'\nE1\n{E1}')
