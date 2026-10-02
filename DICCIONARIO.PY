def ejercicio_1():
    print("\n===== EJERCICIO 1: FICHA DE DISPOSITIVO =====")

    dispositivo = {
        "modelo": "Dell Latitude",
        "ip": "192.168.1.20",
        "estado": "Activo",
        "sistema": "Windows 11",
        "existencia": 10
    }

    print("Modelo:", dispositivo["modelo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
    print("Sistema:", dispositivo["sistema"])
    print("Existencia:", dispositivo["existencia"])

    dispositivo["existencia"] = 8

    print("Nueva existencia:", dispositivo["existencia"])


def ejercicio_2():
    print("\n===== EJERCICIO 2: DIRECTORIO DE USUARIOS =====")

    directorio = {
        "Ana": "8888-1111",
        "Luis": "8888-2222",
        "Carlos": "8888-3333",
        "David": "8888-4444"
    }

    nombre = input("Ingrese el nombre del contacto: ")

    if nombre in directorio:
        print("Telefono:", directorio[nombre])
    else:
        print("Contacto no encontrado")


def ejercicio_3():
    print("\n===== EJERCICIO 3: CONTEO DE ACCESOS =====")

    accesos = [
        "Laptop",
        "Router",
        "Laptop",
        "Servidor",
        "Router",
        "Laptop"
    ]

    conteo = {}

    for dispositivo in accesos:
        if dispositivo not in conteo:
            conteo[dispositivo] = 0

        conteo[dispositivo] = conteo[dispositivo] + 1

    print("Conteo de accesos:")
    print(conteo)


def ejercicio_4():
    print("\n===== EJERCICIO 4: INCIDENTES POR TECNICO =====")

    ventas = {
        "Carlos": 1500,
        "Ana": 2300,
        "Luis": 1900,
        "David": 2500
    }

    mayor_tecnico = ""
    mayor_venta = 0

    for tecnico, total in ventas.items():
        if total > mayor_venta:
            mayor_venta = total
            mayor_tecnico = tecnico

    print("Técnico con mayor venta:", mayor_tecnico)
    print("Total vendido:", mayor_venta)


def ejercicio_5():
    print("\n===== EJERCICIO 5: ACTUALIZACION DE DISPOSITIVOS =====")

    inventario = {
        "Laptop": 10,
        "Router": 8,
        "Mouse": 15
    }

    print("Inventario inicial:")
    print(inventario)

    inventario["Laptop"] = inventario["Laptop"] + 5
    inventario["Router"] = inventario["Router"] - 2
    inventario["Mouse"] = inventario["Mouse"] + 3

    print("Inventario actualizado:")
    print(inventario)