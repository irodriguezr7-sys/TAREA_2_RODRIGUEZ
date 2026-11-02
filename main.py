from pasajero import Pasajero
from lista_manual import ListaPasajerosManual
from lista_python import ListaPasajerosPython
from ejercicios import menu_ejercicios

lista1 = ListaPasajerosManual(capacidad=10)
lista2 = ListaPasajerosPython()

# ---- LEER_ENTERO ----
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")

# ---- LEER_CEDULA ----
def leer_cedula(mensaje="  Cédula (10 dígitos): "):
    while True:
        cedula = input(mensaje).strip()
        if cedula.isdigit() and len(cedula) == 10:
            return cedula
        print("  La cédula debe tener exactamente 10 dígitos numéricos.")

# ---- LEER_EDAD ----
def leer_edad(mensaje="  Edad: "):
    while True:
        edad = leer_entero(mensaje)
        if 0 <= edad <= 120:
            return edad
        print("  La edad debe estar entre 0 y 120.")

# ---- LEER_PASAJERO ----
def leer_pasajero():
    nombre = input("  Nombre: ").strip()
    while nombre == "":
        print("  El nombre no puede estar vacío.")
        nombre = input("  Nombre: ").strip()
    cedula = leer_cedula()
    edad = leer_edad()
    return Pasajero(nombre, cedula, edad)

# ---- CARGAR_DATOS_PRUEBA ----
def cargar_datos_prueba(lista):
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana",   "0912345678", 28))
    lista.añadir(Pasajero("Luis",  "0987654321", 35))
    lista.añadir(Pasajero("Beto",  "0934567890", 16))
    lista.añadir(Pasajero("Elena", "0901234567", 41))
    print("  5 pasajeros de prueba cargados")

# ---- PASAJERO_EN ----
def pasajero_en(lista, pos):
    if isinstance(lista, ListaPasajerosManual):
        return lista.datos[pos]
    return lista.pasajeros[pos]

# ---- MOSTRAR_MENU_LISTA ----
def mostrar_menu_lista(titulo):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir pasajero (al final)")
    print(" 2. Listar pasajeros")
    print(" 3. Insertar en una posición")
    print(" 4. Buscar por cédula (lineal)")
    print(" 5. Buscar por cédula (binaria)")
    print(" 6. Modificar pasajero")
    print(" 7. Eliminar por posición")
    print(" 8. Eliminar por cédula (valor)")
    print(" 9. Ordenar ascendente (por cédula)")
    print("10. Ordenar descendente (por cédula)")
    print("11. Reversar")
    print("12. Copiar lista")
    print("13. Longitud")
    print("14. Filtrar mayores de edad")
    print("15. Nombres en mayúsculas")
    print(" C. Cargar datos de prueba")
    print(" 0. Volver")

# ---- MENU_LISTA ----
def menu_lista(lista, titulo):
    while True:
        mostrar_menu_lista(titulo)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista.añadir(pasajero):
                print("  Pasajero añadido")

        elif op == "2":
            lista.listar()

        elif op == "3":
            posicion = leer_entero("  Posición donde insertar: ")
            pasajero = leer_pasajero()
            if lista.insertar(posicion, pasajero):
                print("  Insertado")

        elif op == "4":
            cedula = leer_cedula()
            pos = lista.buscar(cedula)
            if pos == -1:
                print("  No existe")
            else:
                print(f"  Encontrado en [{pos}]: {pasajero_en(lista, pos)}")

        elif op == "5":
            print("  (Recuerda ordenar primero con la opción 9)")
            cedula = leer_cedula()
            pos = lista.buscar_binaria(cedula)
            if pos == -1:
                print("  No existe")
            else:
                print(f"  Encontrado en [{pos}]: {pasajero_en(lista, pos)}")

        elif op == "6":
            cedula = leer_cedula()
            nombre = input("  Nuevo nombre: ").strip()
            while nombre == "":
                print("  El nombre no puede estar vacío.")
                nombre = input("  Nuevo nombre: ").strip()
            edad = leer_edad("  Nueva edad: ")
            if lista.modificar(cedula, nombre, edad):
                print("  Modificado")

        elif op == "7":
            posicion = leer_entero("  Posición a eliminar: ")
            quitado = lista.eliminar_por_posicion(posicion)
            if quitado is not None:
                print(f"  Eliminado: {quitado}")

        elif op == "8":
            cedula = leer_cedula()
            if lista.eliminar_por_valor(cedula):
                print("  Eliminado")

        elif op == "9":
            lista.ordenar_asc()
            lista.listar()

        elif op == "10":
            lista.ordenar_desc()
            lista.listar()

        elif op == "11":
            lista.reversar()
            lista.listar()

        elif op == "12":
            copia = lista.copiar()
            copia.reversar()
            print("--- COPIA (reversada) ---")
            copia.listar()
            print("--- ORIGINAL ---")
            lista.listar()

        elif op == "13":
            print(f"  Hay {lista.longitud()} pasajeros")

        elif op == "14":
            mayores = lista.filtrar_mayores_de_edad()
            mayores.listar()

        elif op == "15":
            nombres = lista.nombres_en_mayusculas()
            print(nombres)

        elif op == "C":
            cargar_datos_prueba(lista)

        elif op == "0":
            break

        else:
            print("  Opción no válida")

# ---- MENU_LISTA1 ----
def menu_lista1():
    menu_lista(lista1, "LISTA 1 · desde cero")

# ---- MENU_LISTA2 ----
def menu_lista2():
    menu_lista(lista2, "LISTA 2 · list de Python")

# ---- MAIN ----
def main():
    while True:
        print("\n==================================")
        print("     TAREA LISTAS - PASAJEROS")
        print("==================================")
        print("1. Lista 1 (construida desde cero)")
        print("2. Lista 2 (list de Python)")
        print("3. Listar ejercicios")
        print("4. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            menu_ejercicios()
        elif op == "4":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()