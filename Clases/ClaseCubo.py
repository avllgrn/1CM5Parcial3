from Clases.ClaseCuadro import *

class Cubo (Cuadro):
    def __str__(self):
        return super().__str__()+f'Volumen:   {self.dameTuVolumen()}\n'

    def dameTuVolumen(self):
        return self.lado**3
