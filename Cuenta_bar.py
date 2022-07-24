class Cuenta:

    # Menu - Hacemos un diccionario para almacenar el menu.
    menu = {
        'Refresco': 50,
        'Agua': 25,
        'Vino': 200,
        'Cerveza': 175,
    }
    
    # Metodo Init
    def __init__(self):
        # El total sera igual a 0
        self.total = 0
        # Almacenamos el objeto en una lista vacia
        self.objetos = []
    
    # Metodo agregar
    def agregar(self, objeto):
        # Agregamos el objeto con el metodo append()
        self.objetos.append(objeto)
        # El total sera + igual al objeto del menu
        self.total = self.menu[objeto]
    
    # Metodo factura
    def factura(self, impuesto, servicio):
        # Impuesto
        impuesto = (impuesto / 100) * self.total
        # Servicio
        servicio = (servicio / 100) * self.total

        total = self.total + impuesto + servicio
    
        # Bucle for
        for objeto in self.objetos:
            # Imprimimos el objeto y el total del objeto en el menu
            print(f'{objeto} ${self.menu[objeto]}')

        print(f'Total: ${total:.2f}')


if __name__ == '__main__':
    cuenta1 = Cuenta()
    cuenta1.agregar('Agua')
    cuenta1.factura(10, 5)