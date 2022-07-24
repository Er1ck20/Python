# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora:

    # Metodo Init - Inicializador
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2
    
    # METODO GET
    @property
    def num1(self):
        return self.__num1
    
    @property
    def num2(self):
        return self.__num2
    
    # METODO SET
    @num1.setter
    def num1(self, num1):
        self.__num1 = num1
    
    @num2.setter
    def num2(self, num2):
        self.__num2 = num2
    
    # METODO SUMA
    def sumar(self):
        r = (self.num1 + self.num2)
        print(f'EL RESULTADO DE LA SUMA ES: {r}')
    
    # METODO PARA RESTAR
    def restar(self):
        r = (self.num1 - self.num2)
        print(f'EL RESULTADO DE LA RESTA ES: {r}')
    
    # METODO PARA DIVIDIR
    def dividir(self):
        r = (self.num1 // self.num2)
        print(f'EL RESULTADO DE LA DIVISION ES: {r}')
    
    # METODO PARA MULTIPLICAR
    def multiplicar(self):
        r = (self.num1 * self.num2)
        print(f'EL RESULTADO DE LA MULTIPLICACION ES: {r}')
    
if __name__ == '__main__':
    num1 = int(input('Ingrese el primer numero: '))
    num2 = int(input('Ingrese el segundo numero: '))

    c = Calculadora(num1, num2)

    c.sumar()

    c.restar()

    c.dividir()

    c.multiplicar()
        