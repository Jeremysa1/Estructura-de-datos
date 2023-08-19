class Vehículo:
    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible

    def encender(self):
        print("El vehículo está encendido.")

    def arrancar(self):
        print("El vehículo está en movimiento.")

    def __str__(self):
        return f"Marca: {self.marca}, Combustible: {self.combustible}"

mi_vehiculo = Vehículo("inpect", "Gasolina")
print(mi_vehiculo)  # Esto llama automáticamente el método __str__
mi_vehiculo.encender()
mi_vehiculo.arrancar()

