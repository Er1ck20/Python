# Definimos la clase PADRE.
class Padre:
    
    # Metodo Init - Inicializador
    def __init__(self, nombre, apellido, edad):
        # Encapsulamos con (__) los parametros
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    # Metodo get - Para obtener/recuperar los atributos de nuestra class
    @property # Decorador Property - Permite el acceso desde el exterior
    def nombre(self):
        # Retornamos  
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def edad(self):
        return self.__edad
    
    # Metodo Set -Permite modificar el valor desde el exterior.
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    
    # Metodo Str - Sobreescritura
    def __str__(self):
        return f'NOMBRE: {self.nombre} | APELLIDO: {self.apellido} | EDAD: {self.edad}'

# if __name__ == '__main__':
#     P1 = Padre('E', 'P', 23)
#     print(P1)

    
# Creamos la clase hijo que hereda los atributos y parametros de la clase padre
class Hijo(Padre):
    
    # Agregaremos un contador
    # Variable de clase
    contador = 0
    
    # Metodo de clase
    @classmethod
    def contadorID(cls):
        cls.contador += 1 
        return cls.contador
    
    # METODO INIT - Inicializador'
    def __init__(self, nombre, apellido, edad):
        # Usamos el metodo super() - Para acceder a los metodos de la clase padre.
        super().__init__(nombre, apellido, edad)
        # Encapsulamos el ID
        self.__ID = Hijo.contadorID()
        
    # METODO GET 
    @property
    def ID(self):
        return self.__ID
    
    # METODO SET
    @ID.setter
    def ID(self, ID):
        self.__ID = ID
    # METODO STR - Sobreescritura
    def __str__(self):
        return f'ID: {self.ID} | {super().__str__()}'

Hijo1 = Hijo('Erick', 'P', 23)

print(Hijo1)
