

class Hotel:
    def __init__(self, nombre, habitaciones_totales, habitaciones_disponibles):
        self.nombre = nombre
        self.habitaciones_totales = habitaciones_totales
        self.habitaciones_disponibles = habitaciones_disponibles
    
    def info_hotel(self):
        return f"Nombre: {self.nombre}, Habitaciones totales: {self.habitaciones_totales}, Habitaciones disponibles: {self.habitaciones_disponibles}"

class HotelEconomico(Hotel):
    def __init__(self, nombre, habitaciones_totales, habitaciones_disponibles, tarifa):
        super().__init__(nombre, habitaciones_totales, habitaciones_disponibles)
        self.tarifa = tarifa
    
    def calcular_precio(self, noches):
        return self.tarifa * noches
    
class HotelLujo(Hotel):
    def __init__(self, nombre, habitaciones_totales, habitaciones_disponiblles, servicios_adicionales):
        super().__init__(nombre, habitaciones_totales, habitaciones_disponiblles)
        self.servicios_adicionales = servicios_adicionales
        
    def mostrar_servicios(self):
        return f"Servicios adicionales: {', '.join(self.servicios_adicionales)}"







