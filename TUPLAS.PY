def ejercicio_1():
    print("\n===== EJERCICIO 1: COORDENADAS DE UN LOCAL =====")

    coordenada = (12.1364, -86.2514)

    latitud, longitud = coordenada

    print("Latitud:", latitud)
    print("Longitud:", longitud)


def ejercicio_2():
    print("\n===== EJERCICIO 2: DIMENSIONES DE UNA CAJA =====")

    dimensiones = (10, 5, 4)

    ancho, alto, profundidad = dimensiones

    volumen = ancho * alto * profundidad

    print("Ancho:", ancho)
    print("Alto:", alto)
    print("Profundidad:", profundidad)
    print("Volumen:", volumen)


def ejercicio_3():
    print("\n===== EJERCICIO 3: REGISTRO DE ESTUDIANTE =====")

    estudiante = ("David Castro", 17, 90)

    for dato in estudiante:
        print(dato)


def ejercicio_4():
    print("\n===== EJERCICIO 4: PUNTOS DE UNA RUTA =====")

    puntos = [
        (12.13, -86.25),
        (12.14, -86.26),
        (12.15, -86.27),
        (12.16, -86.28)
    ]

    for latitud, longitud in puntos:
        print("Latitud:", latitud, "Longitud:", longitud)


def ejercicio_5():
    print("\n===== EJERCICIO 5: RETORNO MULTIPLE =====")

    ventas = [120, 150, 200, 180, 250]

    total = sum(ventas)
    promedio = total / len(ventas)
    maxima = max(ventas)

    resultado = (total, promedio, maxima)

    print("Total:", resultado[0])
    print("Promedio:", resultado[1])
    print("Venta maxima:", resultado[2])