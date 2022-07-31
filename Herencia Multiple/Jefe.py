class Datos:
    # Variable de clase
    contador = 0

    @classmethod
    def contador_id(cls):
        cls.contador += 1
        return cls.contador

    # Metodo Init
    def __init__(self, nombre, apellido, edad, sueldo):
        self._id = Datos.contador_id()
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__sueldo = sueldo

    # Metodo Get
    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def edad(self):
        return self.__edad

    @property
    def sueldo(self):
        return self.__sueldo

    # Metodo Set
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @sueldo.setter
    def sueldo(self, sueldo):
        self.__sueldo = sueldo

    # Metodo Str - Sobrescritura
    def __str__(self):
        return f'ID: {self._id} | NOMBRE: {self.nombre} | APELLIDO: {self.apellido} | EDAD: {self.edad} | ' \
               f'SUELDO: {self.sueldo}'


if __name__ == '__main__':
    Jefe1 = Datos('Erick', 'P', '23', '21,000')
    print(Jefe1)
