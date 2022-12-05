# Conversion de medidas de volumen
'''
MEDIDAAS DE VOLUMEN:
1 pie^3 = 0.02832 metros^3
1 yarda^3 = 0.7646 metros ^3
1 pinta = 0.56826 litros
1 galon = 4.54609 litros

'''

class Volumen:

    # Metodo init
    def __init__(self,x):
        self.__x = x
    
    # Metodo Get
    @property
    def x(self):
        return self.__x
    
    # Metodo set
    @x.setter
    def x(self,x):
        self.__x = x
    
    # Metodo para convertir pie^3 a metros^3
    def conversion_pie3(self):
        # 1 pie^3 = 0.02832 metros^3
        y = 0.02832
        r = (self.x * y)
        print(f'{self.x} pie^3 es igual a: {r} metros ^3')
    
    # Metodo para convertir yarda^3 a metros^#
    def conversion_yarda3(self):
        # 1 yarda^3 = 0.7646 metros ^3
        y = 0.7646 
        r = (self.x * y)
        print(f'{self.x} yarda^3 es igual a: {r} metros ^3')
    
    # Metodo para convertir 1 pinta a litros
    def conversion_pinta(self):
        # 1 pinta = 0.56826 litros
        y = 0.56826 
        r = (self.x * y)
        print(f'{self.x} pintas es igual a: {r} litros')
    
    # Metodo para convertir 1 galon a litros
    def conversion_galon(self):
        # 1 galon = 4.54609 litros
        y = 4.54609
        r = (self.x * y)
        print(f'{self.x} galones es igual a: {r} litros')

if __name__ == '__main__':
    v = Volumen(23)
    v.conversion_pie3()
    v.conversion_yarda3()
    v.conversion_pinta()
    v.conversion_galon()

    
