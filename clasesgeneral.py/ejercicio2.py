class Vehiculo:
    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible

    def encender(self):
        print("El vehículo está encendido.")

    def arrancar(self):
        print("El vehículo está en movimiento.")

    def __str__(self):
        return f"Marca: {self.marca}, Combustible: {self.combustible}"

class Moto(Vehiculo):
    def __init__(self, marca, combustible, cilindrada):
        super().__init__(marca, combustible)
        self.cilindrada = cilindrada

    def encender(self):
        print("La moto está encendida.")

class Carro(Vehiculo):
    def __init__(self, marca, combustible, num_puertas):
        super().__init__(marca, combustible)
        self.num_puertas = num_puertas

    def arrancar(self):
        print("El carro está arrancando.")

# Instancias de las clases
mi_moto = Moto("inpect", "Gasolina", "750cc")
mi_carro = Carro("Toyota", "Gasolina", 4)

print("Moto:")
print(mi_moto)
mi_moto.encender()

print("\nCarro:")
print(mi_carro)
mi_carro.arrancar()
