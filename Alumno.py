# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´

class Alumno:

    # Metodo Init - Inicializador
    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota

    # Metodo Get
    @property
    def nombre(self):
        return self.__nombre

    @property
    def nota(self):
        return self.__nota
    
    # Metodo Set
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @nota.setter
    def nota(self, nota):
        self.__nota = nota
    

    # NOTA
    def nota_alumno(self):
        if self.nota >= 70:
            print(f'Usted ha Aprobado.')
        
        else:
            print('Usted ha Reprobado')
    
    # Metodo Str - Sobreescritura
    def __str__(self):
        return f'NOMBRE: {self.nombre} | NOTA: {self.nota}'

if __name__ == '__main__':
    a = Alumno('Erick', 72)
    print(a)
    a.nota_alumno()

    b = Alumno('Enrique', 69)
    print(b)
    b.nota_alumno()