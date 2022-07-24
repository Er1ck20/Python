from Ejercicio_coche import Coche


class Precio(Coche):
    def __init__(self, marca, modelo, color, puertas, placa, precio):
        super().__init__(marca, modelo, color, puertas, placa)
        self.__precio = precio

    # Metodo Get
    @property
    def precio(self):
        return self.__precio

    # Metodo Set
    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    # Metodo Str
    def __str__(self):
        return f'{super().__str__()} \nPRECIO: {self.precio}'


if __name__ == '_main_':
    coche1 = Precio('Hyundai', 'Hyundai Accent', 'Rojo', 4, 'SDS2X1S5DX', 150000.00)
    print(coche1)
