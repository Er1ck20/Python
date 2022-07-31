# Ejemplo
class Padre:
    # Metodo Init
    def __init__(self, apellido, altura, color_ojos, color_pelo):
        self.__apellido = apellido
        self.__altura = altura
        self.__color_ojos = color_ojos
        self.__color_pelo = color_pelo
    
    # Metodo Get
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def color_ojos(self):
        return self.__color_ojos
    
    @property
    def color_pelo(self):
        return self.__color_pelo

    # Metodo Set
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
    
    @color_ojos.setter
    def color_ojos(self, color_ojos):
        self.__color_ojos = color_ojos
    
    @color_pelo.setter
    def color_pelo(self, color_pelo):
        self.__color_pelo = color_pelo
    
    # Metodo Str
    def __str__(self):
        return f'APELLIDO: {self.apellido} | ALTURA: {self.altura} | COLOR DE OJOS: {self.color_ojos} | COLOR DE PELO: {self.color_pelo}'


class Hijo(Padre):
    def __init__(self, nombre ,apellido, altura, color_ojos, color_pelo):
        super().__init__(apellido, altura, color_ojos, color_pelo)
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    def __str__(self):
        return f'NOMBRE: {self.nombre} | {super().__str__()}'

if __name__ == '__main__':
    h1 = Hijo('Erick', 'P', '5"10', 'Negros', 'Negro')
    print(h1)
