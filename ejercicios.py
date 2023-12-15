import random
import pdb

class Coche():
    def __init__(self, nombre, caballos):
        self.nombre=nombre
        self.caballos=caballos

    def to_string(self):
        return "{marca:", self.nombre, "caballos: ", self.caballos, "}"
    
class Carrera():
    def __init__(self, coches):
        self.coches=coches
        self.resultado=[] #### UTILIZAR

    def mostrar_parrilla_de_salida(self):
        aux = 1
        for coche in self.coches:
            print("El coche ", coche.nombre, "sale en [",aux,"] posicion")
            aux = aux+1
    
    def empieza_carrera(self):
        print("La carrera ha empezado..")

    def finaliza_carrera(self):
        # Generar randoms entre mis self.coches
        random.shuffle(self.coches)
        self.resultado.extend(self.coches)

    
    def muestra_resultado(self):
        # RECORRER (FOR SOBRE RESULTADO)
        for coche in self.resultado:
            print(coche.to_string())

if __name__ == '__main__':
    c1 = Coche("Mercedes", "120hp")
    c2 = Coche("Ferrari", "200hp")
    c3 = Coche("Mustang", "200hp")
    coches=[c1, c2, c3]
    
    c = Carrera(coches)
    c.mostrar_parrilla_de_salida()
    c.empieza_carrera()
    c.finaliza_carrera()
    c.muestra_resultado()
    
