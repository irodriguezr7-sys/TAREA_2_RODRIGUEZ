from pasajero import Pasajero

class ListaPasajerosManual:
    # ---- CONSTRUCTOR ----
    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    # ---- AÑADIR ----
    def añadir(self, pasajero):
        if self.cantidad == self.capacidad:
            print("La lista está llena")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("Ya existe un pasajero con esa cédula")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    # ---- LISTAR ----
    def listar(self):
        if self.cantidad == 0:
            print("(lista vacía)")
            return
        for i in range(self.cantidad):
            print(f"[{i}] {self.datos[i]}")

    # ---- LONGITUD ----
    def longitud(self):
        return self.cantidad

    # ---- INSERTAR ----
    def insertar(self, posicion, pasajero):
        if self.cantidad == self.capacidad:
            print("La lista está llena")
            return False
        if posicion < 0 or posicion > self.cantidad:
            print("Posición no válida")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("Ya existe un pasajero con esa cédula")
            return False
        i = self.cantidad
        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i = i - 1
        self.datos[posicion] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    # ---- BUSCAR ---- 
    def buscar(self, cedula):
        for i in range(self.cantidad):
            if self.datos[i].cedula == cedula:
                return i
        return -1

    # ---- BUSCAR_BINARIA ----
    def buscar_binaria(self, cedula):
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio].cedula == cedula:
                return medio
            if self.datos[medio].cedula < cedula:
                izq = medio + 1
            else:
                der = medio - 1
        return -1

    # ---- MODIFICAR ----
    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        pos = self.buscar(cedula)
        if pos == -1:
            print("No existe un pasajero con esa cédula")
            return False
        self.datos[pos].nombre = nuevo_nombre
        self.datos[pos].edad = nueva_edad
        return True

    # ---- ELIMINAR_POR_POSICION ----
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print("Posición no válida")
            return None
        valor = self.datos[posicion]
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return valor

    # ---- ELIMINAR_POR_VALOR ----
    def eliminar_por_valor(self, cedula):
        pos = self.buscar(cedula)
        if pos == -1:
            print("No existe un pasajero con esa cédula")
            return False
        self.eliminar_por_posicion(pos)
        return True

    # ---- ORDENAR_ASC ----
    def ordenar_asc(self):
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].cedula > self.datos[i + 1].cedula:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux

    # ---- ORDENAR_DESC ----
    def ordenar_desc(self):
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].cedula < self.datos[i + 1].cedula:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux

    # ---- REVERSAR ----
    def reversar(self):
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq = izq + 1
            der = der - 1

    # ---- COPIAR ----
    def copiar(self):
        nueva = ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva

    # ---- FILTRAR_MAYORES_DE_EDAD ----
    def filtrar_mayores_de_edad(self):
        resultado = ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            if self.datos[i].es_mayor_de_edad():
                resultado.añadir(self.datos[i])
        return resultado

    # ---- NOMBRES_EN_MAYUSCULAS ----
    def nombres_en_mayusculas(self):
        resultado = [None] * self.cantidad
        for i in range(self.cantidad):
            resultado[i] = self.datos[i].nombre.upper()
        return resultado

if __name__ == "__main__":
    lista = ListaPasajerosManual()
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana",   "0912345678", 28))
    lista.añadir(Pasajero("Luis",  "0987654321", 35))
    print(lista.buscar("0987654321"))
    lista.listar()