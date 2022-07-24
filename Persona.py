# Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.

class Persona:

    # Metodo Init - Inicializador
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    # METODO GET
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    # METODO SET
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    
    # Metodo para mostrar si la persona es mayor de edad
    def mayor_edad(self):
        if self.edad > 18:
            print(f'Usted tiene {self.edad} y es mayor de edad.')
        
        else:
            print(f'Usted tiene {self.edad} y no es mayor de edad.')
    
    # Metodo STR - Sobreescritura
    def __str__(self):
        return f'NOMBRE: {self.nombre} | EDAD: {self.edad}'

if __name__ == '__main__':
    P = Persona('Erick', 22)
    print(P) 
    P.mayor_edad()