"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad.

Crea sus métodos get, set.

Tendrá dos métodos especiales:
    - ingresar
    - retirar
"""

class Cuenta:

    # METODO INIT - Inicializador
    def __init__(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = cantidad

    # Metodo Get
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
    
    # Metodo ingresar
    def ingresar(self):
        ingresar_monto = int(input('Introduzca la cantidad de dinero que desea ingresar: '))
        r = self.cantidad + ingresar_monto
        print(f'''
            Titular: {self.titular}
            Efectivo: {self.cantidad} 
            Usted ha ingresado: {ingresar_monto} 
            Total: {r}
        ''')
    
    # Metodo retirar
    def retirar(self):
        retirar_monto = int(input('Introduzca la cantidad de dinero que desea retirar: '))
        r = self.cantidad - retirar_monto
        print(f'''
            Titular: {self.titular}
            Efectivo: {self.cantidad} 
            Usted ha retirado: {retirar_monto} 
            Total: {r}
        ''')

if __name__ == '__main__':
    c = Cuenta('Erick', 2300)
    c.ingresar()

    c2 = Cuenta('Perla', 25650)
    c2.retirar()

