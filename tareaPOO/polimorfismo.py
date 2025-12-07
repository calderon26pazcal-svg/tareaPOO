class sistemaOperativo:
    def iniciar(self):
        pass

class Windows(sistemaOperativo):
    def iniciar(self):
       return"Windows esta cargando el escritorio..."

class Linux(sistemaOperativo):
    def iniciar(self):
       return"Linux esta iniciiando el kernel y servicios..."

class MacOS(sistemaOperativo):
    def iniciar(self):
       return"MacOS esta configurando el entorno grafico..."

sistemas = [Windows(), Linux(), MacOS() ]

for sistemaOperativo in sistemas:
    print(sistemaOperativo.iniciar())