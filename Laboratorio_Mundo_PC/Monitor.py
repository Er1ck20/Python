class Monitor:

    # Variable de clase
    contador_monitor = 0

    # Metodo de clase
    @classmethod
    def contador(cls):
        cls.contador_monitor += 1
        return cls.contador_monitor

    def __init__(self, marca, tamano):
        self.__id_monitor = Monitor.contador()
        self.__marca = marca
        self.__tamano = tamano

    # Metodo Get
    @property
    def id_monitor(self):
        return self.__id_monitor

    @property
    def marca(self):
        return self.__marca

    @property
    def tamano(self):
        return self.__tamano

    # Metodo Set
    @id_monitor.setter
    def id_monitor(self, id_monitor):
        self.__id_monitor = id_monitor

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @tamano.setter
    def tamano(self, tamano):
        self.__tamano = tamano

    # Metodo Str
    def __str__(self):
        return f'ID MONITOR: {self.id_monitor} | MARCA: {self.marca}' \
               f' | TAMAÑO: {self.tamano}'


if __name__ == '__main__':
    monitor = Monitor('DELL', '24 Pulgadas')
    print(monitor)