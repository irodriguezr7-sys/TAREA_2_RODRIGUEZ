# =====================================================================
#  lista_python.py  —  LISTA 2: con el list de PYTHON (built-in)
# ---------------------------------------------------------------------
#  Mismas operaciones que la Lista 1, pero ahora usamos lo que Python
#  ya trae: append, insert, pop, remove, sort, reverse, copy, len,
#  enumerate, bisect ... y LIST COMPREHENSIONS.
#
#      self.pasajeros -> [Pasajero, Pasajero, ...]   (crece sola)
#
#  Comprensiones usadas en: buscar · buscar_binaria · eliminar_por_valor
#  · filtrar_mayores_de_edad · nombres_en_mayusculas
#
#  Al lado de cada método se indica cuántas líneas tenía la versión
#  manual (lista_manual.py) y cuántas tiene esta (sin contar docstring
#  ni comentarios).
# =====================================================================
from bisect import bisect_left
from pasajero import Pasajero


class ListaPasajerosPython:
    def __init__(self):
        self.pasajeros = []               # list de Python: crece sola

    # -----------------------------------------------------------------
    # 1. AÑADIR  (con la mejora: no permite cédulas repetidas)
    # -----------------------------------------------------------------
    def añadir(self, pasajero):
        """Añade al final con append(), sin cédulas repetidas."""
        if self.buscar(pasajero.cedula) != -1:
            print("⚠ Ya existe un pasajero con esa cédula")
            return False
        self.pasajeros.append(pasajero)
        return True

    # -----------------------------------------------------------------
    # 2. LISTAR
    # -----------------------------------------------------------------
    def listar(self):
        """Muestra los pasajeros con su posición usando enumerate()."""
        if not self.pasajeros:                  # lista vacía es False
            print("(lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"[{i}] {p}")

    # -----------------------------------------------------------------
    # 3. LONGITUD            (manual: 1 línea | Python: 1 línea)
    # -----------------------------------------------------------------
    def longitud(self):
        """USA len(). RETORNA int."""
        return len(self.pasajeros)

    # -----------------------------------------------------------------
    # 4. INSERTAR            (manual: ~8 líneas | Python: 1 línea útil)
    # -----------------------------------------------------------------
    def insertar(self, posicion, pasajero):
        """
        USA insert(). Valida 0 <= posicion <= len(...).

        PREGUNTA 3 (Fase 3): insert parece "gratis", pero ¿Python corre
        los elementos o no? ¿Qué complejidad tiene?
        RESPUESTA: SÍ los corre. Internamente Python hace lo mismo que
        el while de la Lista 1: desplaza una posición a la derecha todos
        los elementos desde 'posicion' hasta el final para abrir el
        hueco. Solo que lo hace en C, por eso es mucho más rápido, pero
        la cantidad de trabajo es la misma: la complejidad es O(n)
        (en el peor caso, insertar al inicio mueve los n elementos).
        Insertar al final es O(1) amortizado, igual que append.
        """
        if posicion < 0 or posicion > len(self.pasajeros):
            print("⚠ Posición no válida")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("⚠ Ya existe un pasajero con esa cédula")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    # -----------------------------------------------------------------
    # 5. BUSCAR POR CÉDULA  (COMPRENSIÓN)   (manual: 4 | Python: 3)
    # -----------------------------------------------------------------
    def buscar(self, cedula):
        """Retorna la posición (int) o -1, usando una comprensión."""
        posiciones = [i for i, p in enumerate(self.pasajeros)
                      if p.cedula == cedula]
        if not posiciones:
            return -1
        return posiciones[0]
        # EXTRA (versión con next, más corta):
        # return next((i for i, p in enumerate(self.pasajeros)
        #              if p.cedula == cedula), -1)

    # -----------------------------------------------------------------
    # 6. BUSCAR BINARIA  (COMPRENSIÓN + bisect)  (manual: 9 | Python: 4)
    # -----------------------------------------------------------------
    def buscar_binaria(self, cedula):
        """Requiere la lista ordenada por cédula (ordenar_asc antes)."""
        cedulas = [p.cedula for p in self.pasajeros]    # COMPRENSIÓN
        i = bisect_left(cedulas, cedula)   # dónde "debería" estar
        if i < len(cedulas) and cedulas[i] == cedula:
            return i
        return -1

    # -----------------------------------------------------------------
    # 7. MODIFICAR           (manual: 6 | Python: 6, igual)
    # -----------------------------------------------------------------
    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        """Busca, y si existe cambia nombre y edad."""
        pos = self.buscar(cedula)
        if pos == -1:
            print("⚠ No existe un pasajero con esa cédula")
            return False
        self.pasajeros[pos].nombre = nuevo_nombre
        self.pasajeros[pos].edad = nueva_edad
        return True

    # -----------------------------------------------------------------
    # 8. ELIMINAR POR POSICIÓN   (manual: 8 | Python: 1 línea útil)
    # -----------------------------------------------------------------
    def eliminar_por_posicion(self, posicion):
        """USA pop(posicion), que retorna el eliminado."""
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("⚠ Posición no válida")
            return None
        return self.pasajeros.pop(posicion)

    # -----------------------------------------------------------------
    # 9. ELIMINAR POR VALOR (por cédula)  — DOS formas
    # -----------------------------------------------------------------
    def eliminar_por_valor(self, cedula):
        """
        FORMA 2 (COMPRENSIÓN) — la activa.
        FORMA 1 (remove) — comentada para comparar.
        """
        # --- FORMA 1 (remove) ---
        # pos = self.buscar(cedula)
        # if pos == -1:
        #     print("⚠ No existe un pasajero con esa cédula")
        #     return False
        # self.pasajeros.remove(self.pasajeros[pos])
        # return True

        # --- FORMA 2 (comprensión) ---
        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
        if len(self.pasajeros) < antes:         # True si eliminó algo
            return True
        print("⚠ No existe un pasajero con esa cédula")
        return False

    # -----------------------------------------------------------------
    # 10. ORDENAR ASCENDENTE  (manual: 7 | Python: 1)
    # -----------------------------------------------------------------
    def ordenar_asc(self):
        """
        USA sort(key=lambda p: p.cedula).

        PREGUNTA 1 (Fase 3): ¿qué hace key=? ¿Qué error sale si lo quitas?
        RESPUESTA: key= recibe una función que Python aplica a CADA
        elemento para obtener el valor por el que va a comparar. Aquí,
        lambda p: p.cedula le dice "ordena los pasajeros mirando su
        cédula". Sin key=, sort() intenta comparar directamente dos
        objetos Pasajero con '<', y como la clase no define cómo se
        comparan, sale:
        TypeError: '<' not supported between instances of
        'Pasajero' and 'Pasajero'
        """
        self.pasajeros.sort(key=lambda p: p.cedula)

    # -----------------------------------------------------------------
    # 11. ORDENAR DESCENDENTE
    # -----------------------------------------------------------------
    def ordenar_desc(self):
        """USA sort(key=..., reverse=True)."""
        self.pasajeros.sort(key=lambda p: p.cedula, reverse=True)

    # -----------------------------------------------------------------
    # 12. REVERSAR           (manual: 6 | Python: 1)
    # -----------------------------------------------------------------
    def reversar(self):
        """USA reverse(). No es lo mismo que ordenar_desc: solo invierte
        el orden actual, no compara nada."""
        self.pasajeros.reverse()

    # -----------------------------------------------------------------
    # 13. COPIAR             (manual: 4 | Python: 3)
    # -----------------------------------------------------------------
    def copiar(self):
        """
        Retorna una copia SUPERFICIAL.

        PREGUNTA 2 (Fase 3): reversa la copia (original intacto). Luego
        modifica un pasajero de la copia y lista el original… ¿qué pasó
        y por qué?
        RESPUESTA: al reversar la copia, el original NO cambia, porque
        son dos listas distintas (cada una con su propio orden). Pero si
        modificas un pasajero de la copia (por ejemplo su nombre), el
        cambio SÍ se ve en el original. Es una copia superficial: copy()
        duplica la lista, pero no duplica los objetos Pasajero de
        adentro; las dos listas apuntan a los MISMOS objetos. Para
        separarlos del todo habría que hacer una copia profunda
        (copy.deepcopy).
        """
        nueva = ListaPasajerosPython()
        nueva.pasajeros = self.pasajeros.copy()    # o self.pasajeros[:]
        return nueva

    # -----------------------------------------------------------------
    # 14. FILTRAR MAYORES DE EDAD  (COMPRENSIÓN que FILTRA)
    # -----------------------------------------------------------------
    def filtrar_mayores_de_edad(self):
        """Retorna una NUEVA ListaPasajerosPython (manual: 6 | Python: 1)."""
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva

    # -----------------------------------------------------------------
    # 15. NOMBRES EN MAYÚSCULAS  (COMPRENSIÓN que TRANSFORMA)
    # -----------------------------------------------------------------
    def nombres_en_mayusculas(self):
        """Retorna list de str (manual: 4 | Python: 1)."""
        return [p.nombre.upper() for p in self.pasajeros]


# Prueba rápida: python lista_python.py
if __name__ == "__main__":
    lista = ListaPasajerosPython()
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana",   "0912345678", 28))
    lista.añadir(Pasajero("Luis",  "0987654321", 35))
    print(lista.buscar("0987654321"))   # debe imprimir 2
    lista.listar()
