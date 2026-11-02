# =====================================================================
#  ejercicios.py  —  OPCIÓN 3 DEL MENÚ: "Listar ejercicios"
# ---------------------------------------------------------------------
#     • 3 ejercicios DESARROLLADOS (taller)  -> T1, T2, T3
#     • 5 ejercicios PROPUESTOS              -> P1 ... P5
#
#  Cada ejercicio es UNA función sin parámetros que imprime su
#  enunciado, usa datos fijos y muestra el resultado.
#  ✋ = versión MANUAL (bucles)   🐍 = versión PYTHON (built-ins)
# =====================================================================
from lista_python import ListaPasajerosPython
from pasajero import Pasajero


# ============================ DESARROLLADOS ==========================
def ejercicio_t1():
    """T1 — CRUD de pasajeros con clase Pasajero + list."""
    print("T1 — CRUD de pasajeros con clase Pasajero + list")
    lista = ListaPasajerosPython()

    print("\n1) Añadir 3 pasajeros")
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana",   "0912345678", 28))
    lista.añadir(Pasajero("Luis",  "0987654321", 35))

    print("\n2) Listar")
    lista.listar()

    print("\n3) Buscar por cédula 0912345678")
    pos = lista.buscar("0912345678")
    if pos == -1:
        print("   No existe")
    else:
        print(f"   Encontrado en [{pos}]: {lista.pasajeros[pos]}")

    print("\n4) Modificar 0912345678 -> Anita, 29 años")
    if lista.modificar("0912345678", "Anita", 29):
        print("   ✓ Modificado")

    print("\n5) Eliminar a Luis (cédula 0987654321)")
    if lista.eliminar_por_valor("0987654321"):
        print("   ✓ Eliminado")

    print("\n6) Listar otra vez")
    lista.listar()

    print("\n7) Ordenar por NOMBRE (sort con key=lambda p: p.nombre)")
    lista.pasajeros.sort(key=lambda p: p.nombre)
    lista.listar()


def ejercicio_t2():
    """T2 — Estadísticas de una lista de notas."""
    print("T2 — Estadísticas de una lista de notas")
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]

    # ✋ MANUAL: un solo for con acumulador, campeón y contador
    suma = 0
    maxima = notas[0]
    minima = notas[0]
    mejor = nombres[0]
    aprobados = 0
    for i in range(len(notas)):
        suma = suma + notas[i]
        if notas[i] > maxima:
            maxima = notas[i]
            mejor = nombres[i]
        if notas[i] < minima:
            minima = notas[i]
        if notas[i] >= 7:
            aprobados = aprobados + 1
    promedio = suma / len(notas)
    print(f"✋ Promedio {promedio:.2f} · Máx {maxima} ({mejor}) · "
          f"Mín {minima} · Aprobados {aprobados} de {len(notas)}")

    # 🐍 PYTHON: sum, max, min, len, index y comprensión
    promedio = sum(notas) / len(notas)
    maxima = max(notas)
    minima = min(notas)
    mejor = nombres[notas.index(maxima)]
    aprobados = len([n for n in notas if n >= 7])
    print(f"🐍 Promedio {promedio:.2f} · Máx {maxima} ({mejor}) · "
          f"Mín {minima} · Aprobados {aprobados} de {len(notas)}")


def ejercicio_t3():
    """T3 — Ordenar una lista (bubble sort)."""
    print("T3 — Ordenar una lista (bubble sort)")
    datos = [5, 2, 8, 1, 9, 3, 7]

    # ✋ MANUAL: burbuja con bandera hubo_swap sobre una COPIA
    lista = datos[:]
    n = len(lista)
    for vuelta in range(n - 1):
        hubo_swap = False
        for i in range(n - 1 - vuelta):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                hubo_swap = True
        if not hubo_swap:          # ya estaba ordenada: corto antes
            break
    print(f"✋ Burbuja:            {lista}")

    # 🐍 PYTHON
    print(f"🐍 sorted(lista):      {sorted(datos)}")
    desc = datos[:]
    desc.sort(reverse=True)
    print(f"🐍 sort(reverse=True): {desc}")

    # Extra: ordenar palabras por longitud con key=len
    palabras = ["python", "a", "código", "el"]
    print(f"Extra (key=len):       {sorted(palabras, key=len)}")


# ============================= PROPUESTOS ============================
def ejercicio_p1():
    """P1 — Contar apariciones de un valor."""
    print("P1 — Contar apariciones de un valor")
    lista = [1, 3, 2, 3, 4, 3, 5]
    v = 3

    # ✋ MANUAL: patrón contador
    contador = 0
    for x in lista:
        if x == v:
            contador = contador + 1
    print(f"✋ {v} aparece {contador} veces")

    # 🐍 PYTHON: count()
    print(f"🐍 {v} aparece {lista.count(v)} veces")

    # 🧩 COMPRENSIÓN
    print(f"🧩 {v} aparece {len([x for x in lista if x == v])} veces")


def ejercicio_p2():
    """P2 — Invertir una lista SIN lista.reverse()."""
    print("P2 — Invertir una lista")
    lista = [1, 2, 3, 4, 5]

    # ✋ MANUAL: recorrer al revés
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    print(f"✋ {invertida}")

    # 🐍 PYTHON: slicing y reversed
    print(f"🐍 {lista[::-1]}")
    print(f"🐍 {list(reversed(lista))}")

    # 🧩 COMPRENSIÓN
    print(f"🧩 {[lista[i] for i in range(len(lista) - 1, -1, -1)]}")


def ejercicio_p3():
    """P3 — Números únicos manteniendo el orden."""
    print("P3 — Números únicos")
    nums = [1, 3, 2, 3, 4, 1, 5, 2]

    # ✋ MANUAL: añadir solo si todavía no está
    unicos = []
    for x in nums:
        if x not in unicos:
            unicos.append(x)
    print(f"✋ {unicos}")

    # 🐍 PYTHON: dict.fromkeys conserva el orden de inserción
    print(f"🐍 {list(dict.fromkeys(nums))}")

    # list(set(nums)) NO garantiza el orden: un set no guarda el orden
    # de inserción (organiza los elementos según su valor hash), por eso
    # el resultado puede salir en un orden distinto al original.


def ejercicio_p4():
    """P4 — Segundo mayor (sin ordenar toda la lista)."""
    print("P4 — Segundo mayor")
    nums = [5, 2, 9, 7, 9, 3, 8]

    # ✋ MANUAL: dos campeones en un solo recorrido
    mayor = nums[0]
    segundo = None
    for x in nums:
        if x > mayor:
            segundo = mayor
            mayor = x
        elif x != mayor and (segundo is None or x > segundo):
            segundo = x
    print(f"✋ Mayor {mayor} · Segundo {segundo}")

    # 🐍 PYTHON (para comprobar)
    print(f"🐍 Mayor {max(nums)} · Segundo {sorted(set(nums))[-2]}")


def ejercicio_p5():
    """P5 — Fusionar dos listas ordenadas (sin sort)."""
    print("P5 — Fusionar dos listas ordenadas")
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]

    # ✋ MANUAL: dos índices comparando cabezas (base del merge sort)
    resultado = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i = i + 1
        else:
            resultado.append(b[j])
            j = j + 1
    resultado.extend(a[i:])      # lo que sobre de a
    resultado.extend(b[j:])      # lo que sobre de b
    print(f"✋ {resultado}")

    # 🐍 PYTHON (para comprobar)
    print(f"🐍 {sorted(a + b)}")


# ============================== CATÁLOGO =============================
#  (código, título, tipo, función)   ->  tipo: "taller" o "propuesto"
EJERCICIOS = [
    ("T1", "CRUD de pasajeros con clase Pasajero + list", "taller", ejercicio_t1),
    ("T2", "Estadísticas de una lista de notas",          "taller", ejercicio_t2),
    ("T3", "Ordenar una lista (bubble sort)",             "taller", ejercicio_t3),
    ("P1", "Contar apariciones de un valor",              "propuesto", ejercicio_p1),
    ("P2", "Invertir una lista",                          "propuesto", ejercicio_p2),
    ("P3", "Números únicos",                              "propuesto", ejercicio_p3),
    ("P4", "Segundo mayor",                               "propuesto", ejercicio_p4),
    ("P5", "Fusionar dos listas ordenadas",               "propuesto", ejercicio_p5),
]


def menu_ejercicios():
    """Muestra los ejercicios agrupados y ejecuta el que elija el usuario
    hasta que escriba 0."""
    # 1. Separar el catálogo con COMPRENSIONES
    taller = [e for e in EJERCICIOS if e[2] == "taller"]
    propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]

    while True:
        # 2. Mostrar los dos grupos
        print("\n--- DESARROLLADOS (taller) ---")
        for e in taller:
            print(f"  {e[0]}. {e[1]}")
        print("--- PROPUESTOS ---")
        for e in propuestos:
            print(f"  {e[0]}. {e[1]}")
        print("  0.  Volver")

        # 3. Leer el código en mayúsculas
        codigo = input("Código: ").strip().upper()
        if codigo == "0":
            break

        # 4. Buscar la tupla con otra COMPRENSIÓN
        encontrados = [e for e in EJERCICIOS if e[0] == codigo]

        # 5. Ejecutar o avisar
        if encontrados:
            print()
            encontrados[0][3]()
        else:
            print("  Código no válido")
