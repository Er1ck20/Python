class Longitud:

    # Metodo Init
    def __init__(self, pulgada, yarda, milla, pulgada2, pie2, yarda2, acre, milla2):
        self.__pulgada = pulgada
        self.__yarda = yarda
        self.__milla = milla
        self.__pulgada2 = pulgada2
        self.__pie2 = pie2
        self.__yarda2 = yarda2
        self.__acre == acre
        self.__milla2 = milla2
    
    # Metodo Get
    @property
    def pulgada(self):
        return self.__pulgada
    
    @property
    def yarda(self):
        return self.__yarda
    
    @property
    def milla(self):
        return self.__milla
    
    
    
