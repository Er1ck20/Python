# Conversion de medidas de longitud.

'''
1 pulgada = 25.40 milimetros
1 yarda = 0.9144 metros
1 milla = 1.6093 kilometros
1 pulgada^2 = 6.452 centimetros
1 pie^2 = 0.09290 metros ^2
1 yarda^2 = 0.8361 metros ^2
1 acre = 0.4047 hectareas
1 milla^2 = 2.59 kilometros^2
'''

class Longitud:

    # Metodo Init
    def __init__(self, x):
        self.__x = x
    
    # Metodo Get
    @property
    def x(self):
        return self.__x
    
    # Metodo Set 
    @x.setter
    def x(self, x):
        self.__x = x

    # Metodo para convertir de pulgadas a milimetros.
    def conversion_pulgada(self):
        # 1 pulgada = 25.40 milimetros
        y = 25.40
        r = (self.x * y)
        print(f'{self.x} pulgadas = {r:.2f} milimetros')
    
    # Metodo para convertir de yardas a metros.
    def conversion_yarda(self):
        # 1 yarda = 0.9144 metros 
        y = 0.9144
        r = (self.x * y)
        print(f'{self.x} yardas = {r:.2f} metros')

    # Metodo para convertir de milla a kilometros.
    def conversion_milla(self):
        # 1 milla = 1.6093 kilometros
        y = 1.6093 
        r = (self.x * y)
        print(f'{self.x} millas = {r:.2f} kilometros')
    
    # Metodo para convertir de pulgada^2 a centimettros
    def conversion_pulgada2(self):
        # 1 pulgada^2 = 6.452 centimetros
        y = 6.4516 
        r = (self.x * y)
        print(f'{self.x} pulgadas^2 = {r:.2f} centimetros')

    # Metodo para convertir de pie^2 a metros^2
    def conversion_pie2(self):
        # 1 pie^2 = 0.09290 metros ^2
        y = 0.09290 
        r = (self.x * y)
        print(f'{self.x} pie^2 = {r:.2f} metros^2')
    
    # Metodo para convertir yarda^2 a metros^2
    def conversion_yarda2(self):
        # 1 yarda^2 = 0.8361 metros ^2
        y = 0.8361
        r = (self.x * y)
        print(f'{self.x} yarda^2 = {r:.2f} metros^2')
    
    # Metodo para convertir acre a hectareas
    def conversion_acre(self):
        # 1 acre = 0.4047 hectareas
        y = 0.4047 
        r = (self.x * y)
        print(f'{self.x} acres = {r:.2f} hectareas')

    # Metodo para convertir milla ^2 a kilometros^2
    def conversion_milla2(self):
        # 1 milla^2 = 2.59 kilometros^2
        y = 2.59 
        r = (self.x * y)
        print(f'{self.x} millas^2 = {r:.2f} kilometros^2')
        

if __name__ == '__main__':
    longtiud = int(input('Proporcione la medida: '))
    l = Longitud(longtiud)
    l.conversion_pulgada()
    l.conversion_yarda()
    l.conversion_milla()
    l.conversion_pulgada2()
    l.conversion_pie2()
    l.conversion_yarda2()
    l.conversion_acre()
    l.conversion_milla2()