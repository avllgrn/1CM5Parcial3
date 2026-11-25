import subprocess
from Clases.ClaseCuadro import *

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    P0 = Cuadro()
    print(P0)
    P0.muestraTuEstado()
    print()

    C = Cuadro(1)

    print(C)
    C.muestraTuEstado()
    print()

    C.pideleAlUsuarioTuEstado()
    print(C)
    C.muestraTuEstado()
    print()

    C.lado = 'diez'
    print(C)
    C.muestraTuEstado()
    print()
