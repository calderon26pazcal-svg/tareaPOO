class miembroFamilia:
    def __init__(self, nombres, edades):
        self.nombres = nombres
        self.edades = edades

    def descripcion(self):
        print("Mi familia es muy unida, amable y respetuosa")

miembro = miembroFamilia("Fernanda", "22")
miembro.descripcion()