class Vehiculo:
    def __init__(self, Fecha_Fabricacion , Vin_chasis, Vin_motor):
        self.Fecha_Fabricacion = Fecha_Fabricacion
        self.Vin_chasis = Vin_chasis
        self.Vin_motor = Vin_motor

    def obtenerFecha_Fabricacion(self):
        return self.Fecha_Fabricacion

    def obtenerVin_chasis(self):
        return self.Vin_chasis

    def obtenerVin_motor(self):
        return self.Vin_motor


class Automovil(Vehiculo):
    def __init__(self, Fecha_Fabricacion, Vin_chasis, Vin_motor, marca, modelo, precio):
    
        Vehiculo.__init__(self, Fecha_Fabricacion, Vin_chasis, Vin_motor)
        
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def obtener_marca(self):
        return self.marca

    def obtener_modelo(self):
        return self.modelo

    def obtener_precio(self):
        return self.precio

    def imprimir_datos(self):
        return (f"Fecha de Fabricación: {self.obtenerFecha_Fabricacion()}\n"  f"VIN Chasis: {self.obtenerVin_chasis()}\n" f"VIN Motor: {self.obtenerVin_motor()}\n" f"Marca: {self.obtener_marca()}\n"  f"Modelo: {self.obtener_modelo()}\n"  f"Precio: ${self.obtener_precio():,.2f}")


automovil  = Automovil(Fecha_Fabricacion="2011-07-11", Vin_chasis="4983HDSPE2TR56", Vin_motor="U84OFS867UOPA23456", marca="Nissan", modelo="Verza",   precio=99900.00
)


print("Detalles del Automóvil:\n" + automovil.imprimir_datos())

