import subprocess
from Clases.ClaseCubo import *

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    C0 = Cubo()
    print(C0)
    C0.muestraTuEstado()
    print()

    C = Cubo(1)

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
