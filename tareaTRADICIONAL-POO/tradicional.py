
# Ejercicio de Clima Semanal
# Programación Tradicional


def ingresar_temperaturas():
    """
    Función que solicita al usuario las temperaturas
    de los 7 días de la semana.
    """
    temperaturas = []

    for dia in range(1, 8):
        temp = float(input("Ingrese la temperatura del día " + str(dia) + ": "))
        temperaturas.append(temp)

    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función que calcula el promedio semanal.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def main():
    """
    Función principal del programa.
    """
    print("Registro de Temperaturas Semanales")

    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)

    print("El promedio semanal de temperaturas es:", round(promedio, 2), "°C")


# Inicio del programa
main()
