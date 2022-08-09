from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor


class Computadora:
    # Variable de clase
    contador_computadoras = 0

    # Metodo de clase
    @classmethod
    def contador(cls):
        cls.contador_computadoras += 1
        return cls.contador_computadoras

    # Metodo Init
    def __init__(self, nombre, monitor, teclado, raton):
        self.__id_computadora = Computadora.contador()
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    # Metodo Get
    @property
    def id_computadora(self):
        return self.__id_computadora

    @property
    def nombre(self):
        return self.__nombre

    @property
    def monitor(self):
        return self.__monitor

    @property
    def teclado(self):
        return self.__teclado

    @property
    def raton(self):
        return self.__raton

    # Metodo Set
    @id_computadora.setter
    def id_computadora(self, id_computadora):
        self.__id_computadora = id_computadora

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @monitor.setter
    def monitor(self, monitor):
        self.__monitor = monitor

    @teclado.setter
    def teclado(self, teclado):
        self.__teclado = teclado

    @raton.setter
    def raton(self, raton):
        self.__raton = raton

    # Metodo Str = Sobreescritura
    def __str__(self):
        return f'''
                ID: {self.id_computadora}  NOMBRE: {self.nombre}
                MONITOR: {self.monitor}
                TECLADO: {self.teclado}
                RATON: {self.raton}
                '''


if __name__ == '__main__':
    # Importamos las clases y las llamamos
    monitor = Monitor('MSI', '24 Pulgadas')
    teclado = Teclado('Logitech', 'Bluetooth')
    raton = Raton('Logitech', 'Bluetooth')

    computadora1 = Computadora('MSI', monitor, teclado, raton)
    print(computadora1)

    monitor2 = Monitor('Lenovo', '17 Pulgadas')
    teclado2 = Teclado('Red Dragon', 'USB')
    raton2 = Raton('Red Dragon', 'USB')
    computadora2 = Computadora('Lenovo', monitor2, teclado2, raton2)
    print(computadora2)



