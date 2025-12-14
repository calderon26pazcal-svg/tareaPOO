# ==========================================
# Ejercicio de Clima Semanal
# Programación Orientada a Objetos (POO)
# Segundo Semestre
# ==========================================

class Clima:
    """
    Clase que representa el clima semanal.
    """

    def __init__(self):
        # Atributo que almacena las temperaturas
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias.
        """
        for dia in range(1, 8):
            temp = float(input("Ingrese la temperatura del día " + str(dia) + ": "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método que calcula el promedio semanal.
        """
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio


def main():
    """
    Función principal del programa.
    """
    print("Registro de Temperaturas Semanales (POO)")

    clima = Clima()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()

    print("El promedio semanal de temperaturas es:", round(promedio, 2), "°C")


# Inicio del programa
main()
