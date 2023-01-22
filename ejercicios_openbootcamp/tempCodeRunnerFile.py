class Vehiculo:
    def __init__(self,color,ruedas,puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas,velocidad,cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

if __name__ == "__main__":
    carro=Coche("azul",4,4,"125km",45)
    print("hola")