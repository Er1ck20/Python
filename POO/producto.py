'''Crear una clase Producto con los siguientes atributos:
 - Codigo
 - Nombre
 - Precio
 Crearle su contructor, su get y settter y una funcion llamada calcular total.
 '''

class Producto:

    codigo = 0

    # Metodo de clase
    @classmethod
    def codigo_producto(cls):
        cls.codigo += 1
        return cls.codigo
    
    # Metodo init - Inicializador
    def __init__(self, nombre, precio):
        self.codigo = Producto.codigo_producto()
        # Volvemos los atributos privados.
        self.__nombre = nombre
        self.__precio = precio

    # Metodo Get
    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio
    
    # Metodo Set
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @precio.setter
    def precio(self, precio):
        self.__precio = precio
    
    # Calcular total
    def calcular_total(self):
        cantidad = int(input('Proporcione la cantidad: '))
        r = (cantidad * self.precio)
        print(f'PRODUCTO: {self.nombre} | CANTIDAD: {cantidad} | PRECIO: {self.precio} | TOTAL: {r}')


if __name__ == '__main__':
    p = Producto('Brugal', 1500)
    p.calcular_total()
