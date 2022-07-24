# Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.

# La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar la información, datos del titular plazo, interés y total de interés.

# Crear al menos un objeto de cada subclase.

class Cuenta:

    # Metodo Init - Metodo Inicializador
    def __init__(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = cantidad
    
    # Metode Get
    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad
    
    # Metodo Set
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    # Metodo str - Sobreescritura
    def __str__(self):
        return f'TITULAR: {self.titular} \nCANTIDAD: {self.cantidad}'

class CajaAhorro(Cuenta):

    # Metodo init - Metodo Inicializador
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

    # Metodo para mostrar
    def mostrar(self):
        print('Caja Ahorro'.center(50, '-'))
        return f'{super().__str__()}'

class PlazoFijo(Cuenta):

    # Metodo Init - Metodo Inicializador
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.__plazo = plazo
        self.__interes = interes
    
    # Metodo Get
    @property
    def plazo(self):
        return self.__plazo
    
    @property
    def interes(self):
        return self.__interes
    
    # Metodo Set
    @plazo.setter
    def plazo(self, plazo):
        self.__plazo = plazo
    
    @interes.setter
    def interes(self, interes):
        self.__interes = interes
        
    # Metodo para obtener el importe
    def obtener_importe(self):
        return f'TOTAL INTERES: {self.cantidad * self.interes / 100}'

    # Metodo str - Sobreescritura
    def __str__(self):
        print(f'Plazo Fijo'.center(50, '-'))
        return f'{super().__str__()} \nPLAZO: {self.plazo} \nINTERES: {self.interes}'

if __name__ == '__main__':
    c = Cuenta('Erick P.', 500000)
    print(c)

    Ch = CajaAhorro('Erick', 20)
    print(Ch.mostrar())

    Pf = PlazoFijo('Erick P. C.', 20000, '8 Meses', 5)
    print(Pf)   
    print(Pf.obtener_importe())     