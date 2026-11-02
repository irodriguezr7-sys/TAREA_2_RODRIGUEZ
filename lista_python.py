from bisect import bisect_left
from pasajero import Pasajero

class ListaPasajerosPython:
    # ---- CONSTRUCTOR ----
    def __init__(self):
        self.pasajeros = []

    # ---- AÑADIR ----
    def añadir(self, pasajero):
        if self.buscar(pasajero.cedula) != -1:
            print("Ya existe un pasajero con esa cédula")
            return False
        self.pasajeros.append(pasajero)
        return True

    # ---- LISTAR ----
    def listar(self):
        if not self.pasajeros:
            print("(lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"[{i}] {p}")

    # ---- LONGITUD ----
    def longitud(self):
        return len(self.pasajeros)

    # ---- INSERTAR ----
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print("Posición no válida")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("Ya existe un pasajero con esa cédula")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    # ---- BUSCAR ----
    def buscar(self, cedula):
        posiciones = [i for i, p in enumerate(self.pasajeros)
                      if p.cedula == cedula]
        if not posiciones:
            return -1
        return posiciones[0]

    # ---- BUSCAR_BINARIA ----
    def buscar_binaria(self, cedula):
        cedulas = [p.cedula for p in self.pasajeros]
        i = bisect_left(cedulas, cedula)
        if i < len(cedulas) and cedulas[i] == cedula:
            return i
        return -1

    # ---- MODIFICAR ----
    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        pos = self.buscar(cedula)
        if pos == -1:
            print("No existe un pasajero con esa cédula")
            return False
        self.pasajeros[pos].nombre = nuevo_nombre
        self.pasajeros[pos].edad = nueva_edad
        return True

    # ---- ELIMINAR_POR_POSICION ----
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("Posición no válida")
            return None
        return self.pasajeros.pop(posicion)

    # ---- ELIMINAR_POR_VALOR ----
    def eliminar_por_valor(self, cedula):

        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
        if len(self.pasajeros) < antes:
            return True
        print("No existe un pasajero con esa cédula")
        return False

    # ---- ORDENAR_ASC ----
    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.cedula)

    # ---- ORDENAR_DESC ----
    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.cedula, reverse=True)

    # ---- REVERSAR ----
    def reversar(self):
        self.pasajeros.reverse()

    # ---- COPIAR ----
    def copiar(self):
        nueva = ListaPasajerosPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    # ---- FILTRAR_MAYORES_DE_EDAD ----
    def filtrar_mayores_de_edad(self):
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva

    # ---- NOMBRES_EN_MAYUSCULAS ----
    def nombres_en_mayusculas(self):
        return [p.nombre.upper() for p in self.pasajeros]

if __name__ == "__main__":
    lista = ListaPasajerosPython()
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana",   "0912345678", 28))
    lista.añadir(Pasajero("Luis",  "0987654321", 35))
    print(lista.buscar("0987654321"))
    lista.listar()