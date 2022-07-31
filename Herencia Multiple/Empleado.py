from Jefe import Datos


class Empleado(Datos):
    # Metodo Init
    def __init__(self, nombre, apellido, edad, sueldo, direccion):
        Datos.__init__(self, nombre, apellido, edad, sueldo)
        self.__direccion = direccion

    # Metodo Get
    @property
    def direccion(self):
        return self.__direccion

    # Metodo Set
    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    # Metodo Str
    def __str__(self):
        return f'{self.__class__.__name__}: \n{super().__str__()} | DIRECCION: {self.direccion}'


if __name__ == '__main__':
    Empleado1 = Empleado('Erick', 'Colon', 22, '23,000', 'Santo Domingo Este / Calle Mirador #9')
    print(Empleado1)
