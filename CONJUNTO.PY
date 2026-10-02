def ejercicio_1():
    print("\n===== EJERCICIO 1: USUARIOS UNICOS =====")

    clientes = [
        "Ana",
        "Luis",
        "Carlos",
        "Ana",
        "Marta",
        "Luis",
        "David"
    ]

    clientes_unicos = set(clientes)

    print("Clientes diferentes:")
    print(clientes_unicos)

    print("Cantidad de clientes diferentes:", len(clientes_unicos))


def ejercicio_2():
    print("\n===== EJERCICIO 2: APLICACIONES COMPARTIDAS =====")

    proveedor_a = {"Laptop", "Router", "Monitor", "Mouse"}
    proveedor_b = {"Laptop", "Tablet", "Router", "Teclado"}

    compartidos = proveedor_a & proveedor_b

    print("Dispositivos que aparecen en ambos catalogos:")
    print(compartidos)


def ejercicio_3():
    print("\n===== EJERCICIO 3: APLICACIONES EXCLUSIVAS =====")

    proveedor_a = {"Laptop", "Router", "Monitor", "Mouse"}
    proveedor_b = {"Laptop", "Tablet", "Router", "Teclado"}

    exclusivos = proveedor_a - proveedor_b

    print("Dispositivos exclusivos del proveedor A:")
    print(exclusivos)


def ejercicio_4():
    print("\n===== EJERCICIO 4: CATALOGO TECNOLOGICO CONSOLIDADO =====")

    proveedor_a = {"Laptop", "Router", "Monitor", "Mouse"}
    proveedor_b = {"Laptop", "Tablet", "Router", "Teclado"}

    catalogo = proveedor_a | proveedor_b

    print("Catalogo final:")
    print(catalogo)


def ejercicio_5():
    print("\n===== EJERCICIO 5: USUARIOS DE PLATAFORMAS =====")

    evento_1 = ["Ana", "Luis", "David", "Marta", "Carlos"]
    evento_2 = ["Luis", "David", "Jose", "Marta"]

    grupo_1 = set(evento_1)
    grupo_2 = set(evento_2)

    ambos = grupo_1 & grupo_2
    solo_primero = grupo_1 - grupo_2

    print("Asistieron a ambos eventos:")
    print(ambos)

    print("Asistieron solo al primer evento:")
    print(solo_primero)