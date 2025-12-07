class Celular:
    def __init__(self, bateria):
        self.__bateria = bateria

    def cargar(self, cantidad):
        self.__bateria += cantidad

    def usar(self, cantidad):
        self.__bateria -= cantidad

    def get_bateria(self):
        return self.__bateria
    
cel = Celular(65)
cel.cargar(25)
cel.usar(15)

print(cel.get_bateria())