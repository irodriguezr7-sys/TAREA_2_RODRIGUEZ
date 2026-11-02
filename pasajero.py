class Pasajero:

    # ---- CONSTRUCTOR ----
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    # ---- ES_MAYOR_DE_EDAD ----
    def es_mayor_de_edad(self):
        return self.edad >= 18

    # ---- __STR__ ----
    def __str__(self):
        return f"{self.nombre:<10} | cédula: {self.cedula} | {self.edad} años"