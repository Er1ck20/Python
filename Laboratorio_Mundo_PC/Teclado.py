from Dispositivo_Entrada import DispotivoEntrada


class Teclado(DispotivoEntrada):
    # Variable de clase
    contador_teclado = 0

    # Metodo de clase
    @classmethod
    def contador(cls):
        cls.contador_teclado += 1
        return cls.contador_teclado

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        self.__id_teclado = Teclado.contador()

    # Metodo Get
    @property
    def id_teclado(self):
        return self.__id_teclado

    # Metodo Set
    @id_teclado.setter
    def id_teclado(self, id_teclado):
        self.__id_teclado = id_teclado

    # Metodo Str
    def __str__(self):
        return f'ID TECLADO: {self.id_teclado} | {super().__str__()}'


if __name__ == '__main__':
    teclado = Teclado('DELL', 'USB')
    print(teclado)

    teclado2 = Teclado('HP', 'USB')
    print(teclado2)
