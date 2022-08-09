from Computadora import Computadora
from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor


class Orden:
    # Variable de clase
    contador_ordenes = 0

    # Metodo de clase
    @classmethod
    def contador(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    # Metodo Init
    def __init__(self, computadora):
        self.__id_orden = Orden.contador()
        self.__computadora = list(computadora)

    # Metodo Get
    @property
    def id_orden(self):
        return self.__id_orden

    @property
    def computadora(self):
        return self.__computadora

    @id_orden.setter
    def id_orden(self, id_orden):
        self.__id_orden = id_orden

    @computadora.setter
    def computadora(self, computadora):
        self.__computadora = computadora

    # Metodo Agregar computadora
    def agregar_computadora(self, computadora):
        # agregamos con .append las los elementos que vayamos ingresando
        self.computadora.append(computadora)

    def __str__(self):
        # Variable de clase
        computadora_str = ''

        # Ciclo for
        for computadora in self.computadora:
            computadora_str += computadora.__str__()

        return f'''
                ID ORDEN: {self.id_orden}
                {computadora_str}
                '''


if __name__ == '__main__':
    # Importamos las clases y las llamamos
    monitor = Monitor('MSI', '24 Pulgadas')
    teclado = Teclado('Logitech', 'Bluetooth')
    raton = Raton('Logitech', 'Bluetooth')
    computadora1 = Computadora('MSI', monitor, teclado, raton)

    monitor2 = Monitor('Lenovo', '17 Pulgadas')
    teclado2 = Teclado('Red Dragon', 'USB')
    raton2 = Raton('Red Dragon', 'USB')
    computadora2 = Computadora('Lenovo', monitor2, teclado2, raton2)
    Orden1 = Orden([computadora1, computadora2])
    print(Orden1)

    monitor3 = Monitor('HP', '17 Pulgadas')
    teclado3 = Teclado('HP', 'USB')
    raton3 = Raton('HP', 'USB')
    computadora3 = Computadora('HP', monitor3, teclado3, raton3)
    Orden2 = Orden([computadora3])
    print(Orden2)


