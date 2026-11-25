import subprocess
import math

def contadorAscendente(ini, fin, inc):
    if inc>0:
        i = ini
        while i<=fin:
            print(i)
            i += inc

def contadorDescendente(ini, fin, dec):
    dec = math.fabs(dec)
    if dec>0:
        i = ini
        while i>=fin:
            print(i)
            i -= dec

def muestraContador(ini, fin, salto):
    if ini<fin:
        contadorAscendente(ini,fin,salto)
    else:
        contadorDescendente(ini,fin,salto)

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    ini = float(input('Dame ini '))
    fin = float(input('Dame fin '))
    salto = float(input('Dame salto '))

    muestraContador(ini, fin, salto)
