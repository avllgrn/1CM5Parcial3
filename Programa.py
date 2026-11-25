import subprocess
from Clases.ClasePunto3D import *

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    P0 = Punto3D()
    print(P0)
    P0.muestraTuEstado()
    print()

    P = Punto3D('uino', 'dos', 'tres')

    print(P)
    P.muestraTuEstado()
    print()

    P.pideleAlUsuarioTuEstado()
    print(P)
    P.muestraTuEstado()
    print()

    P.modificaTuEstado('siete', 'ocho', 'nueve')
    print(P)
    P.muestraTuEstado()
    print()

    P.x = 1
    P.y = 2.5
    P.z = 3
    print(P)
    P.muestraTuEstado()
    print()
