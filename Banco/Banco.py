class Banco:
    # Variable de clase
    contador = 0

    # Metodo de clase
    @classmethod
    def contador_banco(cls):
        cls.contador += 1
        return cls.contador
        
    # Metodo Init
    def __init__(self, nombre, cedula):
        self.ID = Banco.contador_banco()
        self.__nombre = nombre
        self.cedula = cedula
        self.__cantidad = 10000

    # Metodo GET
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    # Metodo para depositar efectivo
    def depositar(self):
        depositar = int(input('Ingrese la cantidad que desea depositar: '))
        self.cantidad += depositar
        print(f'Usted ha depositado: {depositar}')

    # Metodo para retirar efectivo
    def retirar(self):
        retirar = int(input('Ingrese la cantidad que desea retirar: '))
        self.cantidad -= retirar
        print(f'Usted ha retirado: {retirar}')
        
    # Metodo para mostrar el total
    def total(self):
        print(f'Tiene un total de: {self.cantidad} en su cuenta.')

    # Metodo str - Sobreescritura
    def __str__(self):
        print('INFORMACION DEL CLIENTE'.center(50, '*'))
        
        return f'ID: {self.ID} | NOMBRE: {self.nombre} \nCEDULA: {self.cedula} \nTOTAL EFECTIVO: {self.cantidad}'

if __name__ == '__main__':

    Cliente1 = Banco('Erick' , 402)
    print(Cliente1)
    Cliente1.depositar()
    
    print(Cliente1.total())
    
    print(f'CUENTA ACTUALIZADA: {Cliente1}')

    Cliente2 = Banco('Aldrick', 302)
    print(Cliente2)
    Cliente2.retirar()
    print(f'Cuenta actualizada: {Cliente2}')