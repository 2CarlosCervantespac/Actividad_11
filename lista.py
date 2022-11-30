from particula import Particula
import json

class Lista:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)
    
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
            
    def __str__(self):
        return "".join(
           str(particula) + '\n' for particula in  self.__particulas
        ) 

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0

    def sort_id(self):
        self.__particulas.sort(key=lambda particula: particula.id)

    def sort_distancia(self):
        self.__particulas.sort(key=lambda particula: particula.distancia, reverse=True)

    def sort_velocidad(self):
        self.__particulas.sort(key=lambda particula: particula.velocidad)

    def get_puntos(self):
        puntos = []

        for particula in self.__particulas:
            punto01 = Punto(particula.origen_x, particula.origen_y, particula.red, particula.green, particula.blue)
            punto02 = Punto(particula.destino_x, particula.destino_y, particula.red, particula.green, particula.blue)

            puntos.append(punto01)
            puntos.append(punto02)
        return puntos

    def cantidad(self):
        return len(self.__particulas)            

class Punto:
    def __init__(self, x:int=0, y:int=0, red:int=0, green:int=0, blue:int=0):
        self.x = x
        self.y = y
        self.red = red
        self.green = green
        self.blue = blue
