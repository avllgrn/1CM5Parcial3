import subprocess
from Clases.ClaseCirculoP import *

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    A = Punto2D( )
    B = Punto2D(1, 1)

    Q1 = CirculoP()
    print('Q1')
    print(Q1)
    print('Q1')
    Q1.muestraTuEstado()
    print()

    Q2 = CirculoP(A, B)
    print('Q2')
    print(Q2)
    print('Q2')
    Q2.muestraTuEstado()
    print()

    Q3 = CirculoP('Cadena1', 'Cadena2')
    print('Q3')
    print(Q3)
    print('Q3')
    Q3.muestraTuEstado()
    print()

    Q3.C = 'Cadena3'
    Q3.P = 'Cadena4'
    print('Q3')
    print(Q3)
    print('Q3')
    Q3.muestraTuEstado()
    print()
