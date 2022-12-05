"""
MEIDADES DE PESO:
1 onza = 28.35 gramos
1 libra = 0.45359 kilogramos
1 tonelada inglesa = 1.060 toneladas
"""

class Peso:
    # Metodo Init
    def __init__(self,x ):
        self.__x = x
    
    # Metodo Get
    @property
    def x(self):
        return self.__x
    
    # Metodo Set 
    @x.setter
    def x(self, x):
        self.__x = x

    # Metodo para convertir de onza a gramos
    def conversion_onza(self):
        # 1 onza = 28.35 gramos
        y =  28.35
        r = (self.x * y)
        print(f'{self.x} onza = {r:.2f} gramos')
    
    # Metodo para convertir de libra a kilogramos
    def conversion_libra(self):
        # 1 libra = 0.45359 kilogramos
        y =  0.45359
        r = (self.x * y)
        print(f'{self.x} libra = {r:.2f} kilogramos')
    
    # Metodo para convertir de tonelada inglesa a toneladas
    def conversion_toneladaI(self):
        # 1 tonelada inglesa = 1.060 toneladas
        y =  1.060
        r = (self.x * y)
        print(f'{self.x} libra = {r:.2f} kilogramos')
    

    
if __name__ == '__main__':
    p = Peso(23)
    p.conversion_onza()
    p.conversion_libra()
    p.conversion_toneladaI()