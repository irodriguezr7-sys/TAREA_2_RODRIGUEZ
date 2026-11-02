from lista_python import ListaPasajerosPython
from pasajero import Pasajero

# ======== DESARROLLADOS ========
# ---- EJERCICIO_T1 ----
def ejercicio_t1():
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
        print("   Modificado")

    print("\n5) Eliminar a Luis (cédula 0987654321)")
    if lista.eliminar_por_valor("0987654321"):
        print("   Eliminado")

    print("\n6) Listar otra vez")
    lista.listar()

    print("\n7) Ordenar por NOMBRE (sort con key=lambda p: p.nombre)")
    lista.pasajeros.sort(key=lambda p: p.nombre)
    lista.listar()

# ---- EJERCICIO_T2 ----
def ejercicio_t2():
    print("T2 — Estadísticas de una lista de notas")
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]

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
    print(f"Manual: Promedio {promedio:.2f} · Máx {maxima} ({mejor}) · "
          f"Mín {minima} · Aprobados {aprobados} de {len(notas)}")

    promedio = sum(notas) / len(notas)
    maxima = max(notas)
    minima = min(notas)
    mejor = nombres[notas.index(maxima)]
    aprobados = len([n for n in notas if n >= 7])
    print(f"Python: Promedio {promedio:.2f} · Máx {maxima} ({mejor}) · "
          f"Mín {minima} · Aprobados {aprobados} de {len(notas)}")

# ---- EJERCICIO_T3 ----
def ejercicio_t3():
    print("T3 — Ordenar una lista (bubble sort)")
    datos = [5, 2, 8, 1, 9, 3, 7]

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
        if not hubo_swap:
            break
    print(f"Manual: Burbuja: {lista}")

    print(f"Python: sorted(lista): {sorted(datos)}")
    desc = datos[:]
    desc.sort(reverse=True)
    print(f"Python: sort(reverse=True): {desc}")

    palabras = ["python", "a", "código", "el"]
    print(f"Extra (key=len): {sorted(palabras, key=len)}")

# ======== PROPUESTOS ========
# ---- EJERCICIO_P1 ----
def ejercicio_p1():
    print("P1 — Contar apariciones de un valor")
    lista = [1, 3, 2, 3, 4, 3, 5]
    v = 3

    contador = 0
    for x in lista:
        if x == v:
            contador = contador + 1
    print(f"Manual: {v} aparece {contador} veces")

    print(f"Python: {v} aparece {lista.count(v)} veces")

    print(f"Comprension: {v} aparece {len([x for x in lista if x == v])} veces")

# ---- EJERCICIO_P2 ----
def ejercicio_p2():
    print("P2 — Invertir una lista")
    lista = [1, 2, 3, 4, 5]

    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    print(f"Manual: {invertida}")

    print(f"Python: {lista[::-1]}")
    print(f"Python: {list(reversed(lista))}")

    print(f"Comprension: {[lista[i] for i in range(len(lista) - 1, -1, -1)]}")

# ---- EJERCICIO_P3 ----
def ejercicio_p3():
    print("P3 — Números únicos")
    nums = [1, 3, 2, 3, 4, 1, 5, 2]

    unicos = []
    for x in nums:
        if x not in unicos:
            unicos.append(x)
    print(f"Manual: {unicos}")

    print(f"Python: {list(dict.fromkeys(nums))}")

# ---- EJERCICIO_P4 ----
def ejercicio_p4():
    print("P4 — Segundo mayor")
    nums = [5, 2, 9, 7, 9, 3, 8]

    mayor = nums[0]
    segundo = None
    for x in nums:
        if x > mayor:
            segundo = mayor
            mayor = x
        elif x != mayor and (segundo is None or x > segundo):
            segundo = x
    print(f"Manual: Mayor {mayor} · Segundo {segundo}")

    print(f"Python: Mayor {max(nums)} · Segundo {sorted(set(nums))[-2]}")

# ---- EJERCICIO_P5 ----
def ejercicio_p5():
    print("P5 — Fusionar dos listas ordenadas")
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]

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
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    print(f"Manual: {resultado}")

    print(f"Python: {sorted(a + b)}")

# ======== CATALOGO ========
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

# ---- MENU_EJERCICIOS ----
def menu_ejercicios():
    taller = [e for e in EJERCICIOS if e[2] == "taller"]
    propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]

    while True:
        print("\n--- DESARROLLADOS (taller) ---")
        for e in taller:
            print(f"  {e[0]}. {e[1]}")
        print("--- PROPUESTOS ---")
        for e in propuestos:
            print(f"  {e[0]}. {e[1]}")
        print("  0.  Volver")

        codigo = input("Código: ").strip().upper()
        if codigo == "0":
            break

        encontrados = [e for e in EJERCICIOS if e[0] == codigo]

        if encontrados:
            print()
            encontrados[0][3]()
        else:
            print("  Código no válido")