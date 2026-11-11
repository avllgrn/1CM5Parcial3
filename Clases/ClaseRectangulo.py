class Rectangulo:
    def __init__(self, base=0, altura=0):
        self.__base = base
        self.__altura = altura
        self.verificaRectangulo()

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base):
        self.__base = base
        self.verificaRectangulo()

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura
        self.verificaRectangulo()

    def __str__(self):
        cadena = f'Base: {self.__base}\n'
        cadena += f'Altura: {self.__altura}\n'
        cadena += f'Área: {self.dameTuArea()}\n'
        cadena += f'Perímetro: {self.dameTuPerimetro()}\n'
        return cadena
    
    def del__(self):
        pass

    def pideleAlUsuarioTuEstado(self):
        self.__base = input('Dame mi base ')
        self.__altura = input('Dame mi altura ')
        self.verificaRectangulo()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, base, altura):
        self.__base = base
        self.__altura = altura
        self.verificaRectangulo()

    def dameTuArea(self):
        return self.__base*self.__altura

    def dameTuPerimetro(self):
        return 2*self.__base + 2*self.__altura

    def verificaRectangulo(self):
        try:
            self.__base = float(self.__base)
            self.__altura = float(self.__altura)
        except:
            self.__base = 0
            self.__altura = 0

        if self.__base<=0 or self.altura<=0:
            self.__base = 0
            self.__altura = 0
