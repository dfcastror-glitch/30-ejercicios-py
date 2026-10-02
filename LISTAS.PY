def ejercicio_1():
    print("\n===== EJERCICIO 1: INVENTARIO DE DISPOSITIVOS =====")

    dispositivos = [
        "Laptop",
        "Router",
        "Switch",
        "Servidor",
        "Monitor",
        "Teclado",
        "Mouse",
        "Impresora"
    ]

    print("Inventario original:")
    print(dispositivos)

    nuevo_dispositivo = input("Ingrese un nuevo dispositivo: ")
    dispositivos.append(nuevo_dispositivo)

    posicion = int(input("Ingrese la posicion que desea modificar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre: ")

    dispositivos[posicion] = nuevo_nombre

    print("Inventario final:")
    print(dispositivos)


def ejercicio_2():
    print("\n===== EJERCICIO 2: VENTAS SEMANALES =====")

    ventas = []

    for i in range(7):
        venta = float(input("Ingrese la venta del dia " + str(i + 1) + ": "))
        ventas.append(venta)

    total = sum(ventas)
    promedio = total / len(ventas)
    venta_maxima = max(ventas)
    dia_maximo = ventas.index(venta_maxima) + 1

    print("Total vendido:", total)
    print("Promedio:", promedio)
    print("Venta mas alta:", venta_maxima)
    print("Dia con mayor venta:", dia_maximo)


def ejercicio_3():
    print("\n===== EJERCICIO 3: TEMPERATURAS DE MANAGUA =====")

    temperaturas = []
    mayores_30 = []

    for i in range(7):
        temperatura = float(input("Ingrese la temperatura del dia " + str(i + 1) + ": "))
        temperaturas.append(temperatura)

    for temperatura in temperaturas:
        if temperatura > 30:
            mayores_30.append(temperatura)

    print("Temperaturas registradas:")
    print(temperaturas)

    print("Temperaturas mayores a 30 grados:")
    print(mayores_30)


def ejercicio_4():
    print("\n===== EJERCICIO 4: DISPOSITIVOS SIN CONEXION =====")

    existencias = [5, 0, 8, 0, 3, 6, 0, 4]

    agotados = 0

    for posicion, existencia in enumerate(existencias):
        if existencia == 0:
            print("Dispositivo sin existencia en posicion:", posicion)
            agotados = agotados + 1

    print("Cantidad de dispositivos agotados:", agotados)


def ejercicio_5():
    print("\n===== EJERCICIO 5: ORDENAMIENTO DE LATENCIAS =====")

    latencias = []

    for i in range(10):
        latencia = float(input("Ingrese la latencia " + str(i + 1) + ": "))
        latencias.append(latencia)

    latencias.sort()

    print("De menor a mayor:")
    print(latencias)

    latencias.sort(reverse=True)

    print("De mayor a menor:")
    print(latencias)