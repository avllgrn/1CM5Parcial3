import subprocess
from Clases.ClaseEvento import *

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    E1 = Evento()
    print(f'\nE1')
    E1.muestraTuEstado()

    UnaFecha = Fecha(20,11,2024)
    UnaHora = Hora(8,53,26)
    E2 = Evento(UnaFecha, UnaHora)
    print(f'E2\n{E2}')

    print(f'E1')
    E1.pideleAlUsuarioTuEstado()
    print(f'E1\n{E1}')

    print('Se asignan los valores de E3 a E1')
    E1.F.dia = E2.F.dia
    E1.F.mes = E2.F.mes
    E1.F.anio = E2.F.anio
    E1.H.hora = E2.H.hora
    E1.H.minuto = E2.H.minuto
    E1.H.segundo = E2.H.segundo
    print(f'E1\n{E1}')

    print('Se intenta E1.F = 5')
    E1.F = 5
    print(f'E1\n{E1}')
    print('Se intenta E1.F = 6.7')
    E1.F = 6.7
    print(f'E1\n{E1}')
    print('Se intenta E1.F = \'ocho\'')
    E1.F = 'ocho'
    print(f'E1\n{E1}')
    print('Se intenta E1.F = UnaHora')
    E1.F = UnaHora
    print(f'E1\n{E1}')
    print('Se intenta E1.F = UnaFecha')
    E1.F = UnaFecha
    print(f'E1\n{E1}')
    print('Se intenta E1.H = 5')
    E1.H = 5
    print(f'E1\n{E1}')
    print('Se intenta E1.H = 6.7')
    E1.H = 6.7
    print(f'E1\n{E1}')
    print('Se intenta E1.H = \'ocho\'')
    E1.H = 'ocho'
    print(f'E1\n{E1}')
    print('Se intenta E1.H = UnaFecha')
    E1.H = UnaFecha
    print(f'E1\n{E1}')
    print('Se intenta E1.H = UnaHora')
    E1.H = UnaHora
    print(f'E1\n{E1}')
