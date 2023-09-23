#ejercicio libre 

class Vehiculo:
    def __init__(self, tipo, marca, combustible, nivel_combustible):
        self.tipo = tipo
        self.marca = marca
        self.combustible = combustible
        self.nivel_combustible = nivel_combustible

    def encender(self):
        if self.nivel_combustible < 0.1:
            print("Advertencia: El nivel de combustible es muy bajo. Debe ir a la gasolinera.")
        else:
            print(f"El {self.tipo} está encendido.")

    def arrancar(self):
        print(f"El {self.tipo} está en movimiento.")

    def marchar(self, distancia):
        consumo_por_km = 0.05
        consumo_total = distancia * consumo_por_km

        if self.nivel_combustible <= 0:
            print("El vehículo no puede marchar, está sin combustible.")
        elif self.nivel_combustible - consumo_total <= 0:
            print("Advertencia: El nivel de combustible es muy bajo. Debe ir a la gasolinera.")
            self.nivel_combustible = 0
            print("El vehículo se detuvo por falta de combustible.")
        else:
            self.nivel_combustible -= consumo_total
            print(f"El {self.tipo} ha recorrido {distancia} km. Nivel de Combustible restante: {self.nivel_combustible:.2f} galones.")

    def __str__(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Combustible: {self.combustible}, Nivel de Combustible: {self.nivel_combustible:.2f} galones"

class Moto(Vehiculo):
    def __init__(self, marca, combustible, cilindrada, nivel_combustible):
        super().__init__("Moto", marca, combustible, nivel_combustible)
        self.cilindrada = cilindrada

    def encender(self):
        if self.nivel_combustible < 0.1:
            print("Advertencia: El nivel de combustible es muy bajo. Debe ir a la gasolinera.")
        else:
            print("La moto está encendida.")

class Carro(Vehiculo):
    def __init__(self, marca, combustible, num_puertas, nivel_combustible):
        super().__init__("Carro", marca, combustible, nivel_combustible)
        self.num_puertas = num_puertas

    def arrancar(self):
        print("El carro está arrancando.")

# Instancias de las clases
mi_moto = Moto("Harley-Davidson", "Gasolina", "750cc", 0.3)
mi_carro = Carro("Toyota", "Gasolina", 4, 0.2)

# Imprimir los objetos instanciados
print("Moto:")
print(mi_moto)
mi_moto.encender()
mi_moto.marchar(50)

print("\nCarro:")
print(mi_carro)
mi_carro.arrancar()
mi_carro.marchar(20)
