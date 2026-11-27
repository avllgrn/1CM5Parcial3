import subprocess
from Clases.ClaseProfesor import *

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    Lista = [ Persona(), Empleado(), Profesor(), Persona(), Empleado(), Profesor() ] # Lista de objetos
    nLista = len( Lista ) # Número de objetos en la Lista

    for contador in range( nLista ):                            # Conteo en rango [0, nLista]
        objeto = Lista[ contador ]
        print(objeto.__class__.__name__, 'es objeto', contador)  # Clase y número de objeto en la Lista
        print(objeto, '\n')                                     # Se muestra cada objeto, gracias a su propio __str__()

    subprocess.run('pause', shell=True)
    subprocess.run('cls', shell=True)

    for contador in range( nLista ):                            # Conteo en rango [0, nLista]
        objeto = Lista[ contador ]
        print(objeto.__class__.__name__, 'es objeto', contador)  # Clase y número de objeto en la Lista
        objeto.muestraTuEstado()                                # Se muestra cada objeto, gracias a su propio muestraTuEstado() 
        print()

    subprocess.run('pause', shell=True)
    subprocess.run('cls', shell=True)

    for contador in range( nLista ):                            # Conteo en rango [0, nLista]
        objeto = Lista[ contador ]
        print(objeto.__class__.__name__, 'es objeto', contador)  # Clase y número de objeto en la Lista
        objeto.pideleAlUsuarioTuEstado()                        # Se pide cada objeto, gracias a su propio pideleAlUsuarioTuEstado() 
        print()
        objeto.muestraTuEstado()                                # Se muestra cada objeto, gracias a su propio muestraTuEstado() 
        print('\n')
        subprocess.run('pause', shell=True)
        subprocess.run('cls', shell=True)
