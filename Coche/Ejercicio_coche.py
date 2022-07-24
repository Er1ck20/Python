"""

Crear una clase Coche, a través de la cual se pueda conocer el color del coche, la marca, el modelo, el número
de puertas y la placa. Crear el constructor del coche, así como los métodos que considere necesarios.
Crear una clase PruebaCoche que instancie varios coches, cambiándole el color a algunos de ellos y mostrándolo
por pantalla.

"""


class Coche:
    def __init__(self, marca, modelo, color, puertas, placa):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__puertas = puertas
        self.__placa = placa

    # Metodo Get
    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def color(self):
        return self.__color

    @property
    def puertas(self):
        return self.__puertas

    @property
    def placa(self):
        return self.__placa

    # Metodo Set
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @color.setter
    def color(self, color):
        self.__color = color

    @puertas.setter
    def puertas(self, puertas):
        self.__puertas = puertas

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    # Metodo Str - SobreEscritura
    def __str__(self):
        return f'MARCA: {self.marca} \nMODELO: {self.modelo} \nCOLOR: {self.color} \nPUERTAS: {self.puertas} \n' \
               f'PLACA: {self.placa}'


if __name__ == '_main_':
    print('1'.center(50, '-'))
    coche1 = Coche('Hyundai', 'Hyundai Accent', 'Rojo', 4, 'SDS2X1S5DX')
    print(coche1)

    print('2'.center(50, '-'))
    coche2 = Coche('Hyundai', 'Hyundai Sonata N20', 'Gris', 4, 'XXX2S15DXX')
    print(coche2)
