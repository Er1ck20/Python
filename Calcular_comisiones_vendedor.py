# Cada auto tiene un precio de venta y un porcentaje por venta diferente, elabore un programa que calcule el valor de las comisiones que se deben determinar luego de que el vendedor venda el auto.

# Tener en cuenta:
# Comision AUTO tipo A: %8
# Comision AUTO tipo B: %5
# Comision AUTO TIPO C: 3%


class AUTOS:
    # Metodo init
    def __init__(self, auto):
        self.__auto = auto

    # Metodo Get
    @property
    def auto(self):
        return self.__auto
    
    # Metodo Set
    @auto.setter
    def auto(self, auto):
        self.__auto = auto
       
    # Metodo para determinar la comision
    def comision(self):
        try:
            precio = int(input('Proporcione el precio: '))
            if precio >= 100000:
                r = precio * 0.08
                print(f'''
                    VEHICULO: {self.auto}
                    CATEGORIA: A
                    PRECIO: {precio}
                    EL VENDEDOR OBTUVO UNA COMISION DEL 8%: {r}
                    ''')
            
            elif precio >= 50000 <= 85000:
                r = precio * 0.05
                print(f'''
                    VEHICULO: {self.auto}
                    CATEGORIA: B
                    PRECIO: {precio}
                    EL VENDEDOR OBTUVO UNA COMISION DEL 5%: {r}
                    ''')
               
            
            elif precio >= 25000 <= 49999:
                r = precio * 0.03
                print(f'''
                    VEHICULO: {self.auto}
                    CATEGORIA: C
                    PRECIO: {precio}
                    EL VENDEDOR OBTUVO UNA COMISION DEL 3%: {r}
                    ''')
            
            else:
                print(f'ERROR!!!')
        
        except Exception as ex:
            print(f'ERROR: {ex}')
        



vehiculo = input('Proporcione la marca del vehiculo: ')
a = AUTOS(vehiculo)
a.comision()




        

