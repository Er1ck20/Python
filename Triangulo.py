# Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulo:

    # Metodo Init - Inicializador
    def __init__(self, lado1, lado2, lado3):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3


    # METODO GET
    @property
    def lado1(self):
        return self.__lado1
    
    @property
    def lado2(self):
        return self.__lado2
    
    @property
    def lado3(self):
        return self.__lado3
    
    # METODO SET 
    @lado1.setter
    def lado1(self, lado1):
        self.__lado1 = lado1
    
    @lado2.setter
    def lado2(self, lado2):
        self.__lado2 = lado2
    
    @lado3.setter
    def lado3(self, lado3):
        self.__lado3 = lado3

    # Metodo para determinar el Tipo de Triagulo.
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print(f'Es un triangulo Equilátero')
        
        elif self.lado1 != self.lado2 and self.lado1 == self.lado3:
            print(f'Es un triangulo Isósceles')
        
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
            print(f'Es un triangulo Escaleno')

    # Metodo para determinar cual es el Lado Mayor.
    def mayor_lado(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(f'El lado # 1 con: {self.lado1}. Es el lado mayor.')
        
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print(f'El lado # 2 con: {self.lado2}. Es el lado mayor.')

        elif self.lado3 > self.lado1 and self.lado3 > self.lado2:
            print(f'El lado # 3 con: {self.lado3}. Es el lado mayor.')
        
        else:
            print('Todos los lados on iguales.')


if __name__ == '__main__':
    lado1 = int(input('Ingrese el valor del primer lado: '))
    lado2 = int(input('Ingrese el valor del segundo lado: '))
    lado3 = int(input('Ingrese el valor del tercer lado: '))
    t = Triangulo(lado1, lado2, lado3)
    t.tipo_triangulo()
    t.mayor_lado()