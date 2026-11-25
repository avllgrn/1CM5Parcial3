import subprocess
from Clases.ClaseRectanguloP import *

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    A = Punto2D( )
    B = Punto2D(2, 4)

    R1 = RectanguloP()
    print('R1')
    print(R1)
    print('R1')
    R1.muestraTuEstado()
    print()

    R1.pideleAlUsuarioTuEstado()
    print('R1')
    print(R1)
    print('R1')
    R1.muestraTuEstado()
    print()

    R2 = RectanguloP(A, B)
    print('R2')
    print(R2)
    print('R2')
    R2.muestraTuEstado()
    print()

    R3 = RectanguloP('Cadena1', 'Cadena2')
    print('R3')
    print(R3)
    print('R3')
    R3.muestraTuEstado()
    print()

    R3.C = 'Cadena3'
    R3.P = 'Cadena4'
    print('R3')
    print(R3)
    print('R3')
    R3.muestraTuEstado()
    print()
