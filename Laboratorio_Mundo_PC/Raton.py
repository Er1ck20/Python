from Dispositivo_Entrada import DispotivoEntrada


class Raton(DispotivoEntrada):
    # Variable de clase
    contador_raton = 0

    # Metodo de clase
    @classmethod
    def contador(cls):
        cls.contador_raton += 1
        return cls.contador_raton

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        self.__id_Raton = Raton.contador()

    # Metodo Get
    @property
    def id_Raton(self):
        return self.__id_Raton

    # Metodo Set
    @id_Raton.setter
    def id_Raton(self, id_Raton):
        self.__id_Raton = id_Raton

    # Metodo Str
    def __str__(self):
        return f'ID RATON: {self.id_Raton} | {super().__str__()}'


if __name__ == '__main__':
    raton = Raton('DELL', 'USB')
    print(raton)

    raton2 = Raton('Logitech', 'Bluetooth')
    print(raton2)
