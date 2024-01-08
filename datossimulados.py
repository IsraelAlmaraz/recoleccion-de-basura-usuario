"""
Línea 1: 19.037 <= lat <= 19.06                 lon = -98.233, creciente

Línea 2:        lat = 19.06          -98.233 <= lon <= -98.196, creciente

Línea 3: 19.037 <= lat <= 19.06                 lon = -98.196,  decreciente

Línea 4:        lat = 19.037          -98.233 <= lon <= -98.196, decreciente
"""
import random


class Camion():
    "su propiedad es un diccionario que contiene su lat, lon, iden y línea"

    def __init__(self, iden, line):

        if line == 1:
            lat = round(random.uniform(19.037, 19.06), 3)
            lon = -98.233

        elif line == 3:
            lat = round(random.uniform(19.037, 19.06), 3)
            lon = -98.196

        elif line == 2:
            lon = round(random.uniform(-98.233, -98.196), 3)
            lat = 19.06

        elif line == 4:
            lon = round(random.uniform(-98.233, -98.196), 3)
            lat = 19.037

        self.dicc = {'id': iden, 'lat': lat, 'lon': lon, 'line': line}

    def avanzar(self):
        "avanzar en sentido horario"
        if self.dicc['line'] == 1:

            aux = round(self.dicc['lat'] + 0.002, 3)

            if 19.037 <= aux <= 19.06:
                self.dicc['lat'] = aux
            else:  # ir a línea 2
                self.dicc['lat'] = 19.06
                self.dicc['lon'] = -98.233
                self.dicc['line'] = 2

        elif self.dicc['line'] == 2:

            aux = round(self.dicc['lon'] + 0.002, 3)

            if -98.233 <= aux <= -98.196:
                self.dicc['lon'] = aux

            else:  # ir a línea 3
                self.dicc['lat'] = 19.06
                self.dicc['lon'] = -98.196
                self.dicc['line'] = 3

        elif self.dicc['line'] == 3:

            aux = round(self.dicc['lat'] - 0.002, 3)

            if 19.037 <= aux <= 19.06:
                self.dicc['lat'] = aux

            else:  # ir a línea 4
                self.dicc['lat'] = 19.037
                self.dicc['lon'] = -98.196
                self.dicc['line'] = 4

        elif self.dicc['line'] == 4:

            aux = round(self.dicc['lon'] - 0.002, 3)

            if -98.233 <= aux <= -98.196:
                self.dicc['lon'] = aux

            else:  # ir a línea 1
                self.dicc['lat'] = 19.037
                self.dicc['lon'] = -98.233
                self.dicc['line'] = 1

        return self.dicc


def circular(camiones):
    "hace que todos los camiones avancen, regresa lista de diccionarios"
    diccionarios = []
    for cam in camiones:
        # actualizar lista con posiciones más recientes
        diccionarios.append(cam.avanzar())

    return diccionarios


# U1 = Camion("camion 1", 1)
# U2 = Camion("camion 2", 2)
# U3 = Camion("camion 3", 3)
# U4 = Camion("camion 4", 4)

# lista = [U1, U2, U3, U4]

# lista = circular(lista)
# print(lista)
