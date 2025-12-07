class carreraUniversitaria:
    def __init__(self, nombre):
        self.nombre = nombre

    def informacion(self):
        print(f"Carrera de {self.nombre}")

class Ingenieria(carreraUniversitaria):
    def laboratorio(self):
        print("Esta carrera incluye laboratorios especializados")

carrera = Ingenieria("Ingenieria Quimica")
carrera.informacion()
carrera.laboratorio()