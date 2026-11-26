import subprocess
from Clases.ClaseProfesor import *

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    Prof1 = Profesor()
    print(f'Prof1')
    Prof1.muestraTuEstado()

    FN = Evento(Fecha(1,2,2003),Hora(4,5,6))
    Prof2 = Profesor('Juan','Perez','Lopez','m',1.82,FN,2,4967.6,'Docente', 1, 1.5, 'Humanidades')
    print(f'Prof2\n{Prof2}')

    Prof3 = Profesor(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'mil', 'un millón', 56.78, 'siete', 'Diez punto cinco', 3.1416)
    print(f'Prof3\n{Prof3}')

    print(f'Prof1\n{Prof1}')
    print(f'Prof1')
    Prof1.pideleAlUsuarioTuEstado()
    print(f'\nProf1\n{Prof1}')    

    print('Se intenta P1.modificaProfesor()')
    Prof1.modificaProfesor()
    print(f'\nProf1\n{Prof1}')

    print('Se intenta Prof1.modificaProfesor(1, 2.3, 4, 5.6, \'uno ochenta\', 789, \'mil\', \'un millón\', 56.78, \'dos\', \'tres\', 2.71)')
    Prof1.modificaProfesor(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'mil', 'un millón', 56.78, 'dos', 'tres', 2.71)
    print(f'\nProf1\n{Prof1}')

    print('Se intenta asignar valores incorrectos a los atributos')
    Prof1.Nombre = 1
    Prof1.Paterno = 2.3
    Prof1.Materno = 4
    Prof1.Genero = 5.6
    Prof1.estatura = 'uno ochenta'
    Prof1.FechaNacimiento = 789
    Prof1.numeroEmpleado = 'uno dos tres cuatro'
    Prof1.sueldo = 'siete mil cuatrocientos sesenta y siete punto nueve'
    Prof1.Puesto = 456.654
    Prof1.numeroGrupos = 'cinco'
    Prof1.carga = 'siete punto cinco'
    Prof1.Academia = 9.81
    print(f'\nProf1\n{Prof1}')
