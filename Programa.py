import subprocess
from Clases.ClasePersona import *

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    P1 = Persona()
    print(f'P1\n{P1}')

    E = Evento( Fecha(2,12,2024), Hora(7,10,32) )
    P2 = Persona('Juan','Perez','Lopez','Masculino',1.65, E)
    print(f'P2')
    P2.muestraTuEstado()

    print(f'P1\n{P1}')
    P1.pideleAlUsuarioTuEstado()
    print(f'\nP1\n{P1}')

    print('Se realiza P1.modificaPersona(P2.Nombre, P2.Paterno, P2.Materno, P2.Genero, P2.estatura, P2.FechaNacimiento)')
    P1.modificaPersona(P2.Nombre, P2.Paterno, P2.Materno, P2.Genero, P2.estatura, P2.FechaNacimiento)
    print(f'P2\n{P2}')
    print(f'P1\n{P1}')

    print('Se intenta Persona(12.3, 45.6, 78.9, 8.76, \'uno sesenta\', 123)')
    P3 = Persona(12.3, 45.6, 78.9, 8.76, 'uno sesenta', 123)
    print(f'P3\n{P3}')

    print('Se intenta P3.modificaPersona(12.3, 45.6, 78.9, 8.76, \'uno sesenta\', 123)')
    P3.modificaPersona(12.3, 45.6, 78.9, 8.76, 'uno sesenta', 123)
    print(f'P3\n{P3}')

    print('Se intenta asignar valores incorrectos a los atributos de P3')
    P3.Nombre = 12.3
    P3.Paterno = 45.6
    P3.Materno = 78.9
    P3.Genero = 8.76
    P3.estatura = 'uno sesenta'
    P3.FechaNacimiento = 123
    print(f'P3\n{P3}')
