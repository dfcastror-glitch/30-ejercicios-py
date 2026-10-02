def ejercicio_1():
    print("\n===== EJERCICIO 1: LISTA DE DISPOSITIVOS ESTRUCTURADOS =====")

    dispositivos = [
        {"nombre": "Laptop", "precio": 800},
        {"nombre": "Router", "precio": 120},
        {"nombre": "Monitor", "precio": 300},
        {"nombre": "Mouse", "precio": 25}
    ]

    limite = 200

    print("Dispositivos con precio mayor a", limite)

    for dispositivo in dispositivos:
        if dispositivo["precio"] > limite:
            print(dispositivo["nombre"], dispositivo["precio"])


def ejercicio_2():
    print("\n===== EJERCICIO 2: CONSUMO DE DATOS POR DIA =====")

    ventas = {
        "Lunes": [120, 150, 100],
        "Martes": [200, 180, 160],
        "Miercoles": [90, 110, 130]
    }

    for dia, lista_ventas in ventas.items():
        total = sum(lista_ventas)

        print(dia, "=", total)


def ejercicio_3():
    print("\n===== EJERCICIO 3: SISTEMAS OPERATIVOS UNICOS =====")

    dispositivos = [
        {"nombre": "Laptop", "categoria": "Computadoras"},
        {"nombre": "Router", "categoria": "Redes"},
        {"nombre": "Servidor", "categoria": "Computadoras"},
        {"nombre": "Switch", "categoria": "Redes"},
        {"nombre": "Monitor", "categoria": "Perifericos"}
    ]

    categorias = set()

    for dispositivo in dispositivos:
        categorias.add(dispositivo["categoria"])

    print("Categorias diferentes:")
    print(categorias)


def ejercicio_4():
    print("\n===== EJERCICIO 4: CALIFICACIONES POR ESTUDIANTE =====")

    estudiantes = {
        "Ana": [90, 85, 95],
        "Luis": [80, 75, 90],
        "David": [95, 90, 100]
    }

    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)

        print(nombre, "Promedio:", promedio)


def ejercicio_5():
    print("\n===== EJERCICIO 5: REGISTRO DE SOLICITUDES DE SOPORTE =====")

    pedidos = [
        {
            "cliente": "Carlos",
            "dispositivos": ["Laptop", "Mouse"]
        },
        {
            "cliente": "Ana",
            "dispositivos": ["Router", "Switch", "Monitor"]
        },
        {
            "cliente": "Luis",
            "dispositivos": ["Laptop"]
        }
    ]

    for pedido in pedidos:
        cliente = pedido["cliente"]
        cantidad = len(pedido["dispositivos"])

        print("Cliente:", cliente)
        print("Cantidad de dispositivos:", cantidad)