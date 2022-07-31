from Jefe import Datos


class Gerente(Datos):
    # Metodo Init
    def __init__(self, nombre, apellido, edad, sueldo, sucursal, direccion):
        Datos.__init__(self, nombre, apellido, edad, sueldo)
        self.__sucursal = sucursal
        self.__direccion = direccion

    # Metodo Get
    @property
    def sucursal(self):
        return self.__sucursal

    @property
    def direccion(self):
        return self.__direccion

    # Metodo Set
    @sucursal.setter
    def sucursal(self, sucursal):
        self.__sucursal = sucursal

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    # Metodo Str
    def __str__(self):
        return f'{self.__class__.__name__}: \n{super().__str__()}| SUCURSAL: {self.sucursal} | ' \
               f'DIRECCION: {self.direccion}'


if __name__ == '__main__':
    ok = Gerente('Erick', 'P', 23, '21,000', 'Principal', 'SD')
    print(ok)
