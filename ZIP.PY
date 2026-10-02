def ejercicio_1():
    print("\n===== EJERCICIO 1: ESTUDIANTES Y NOTAS =====")

    estudiantes = ["Ana", "Luis", "Carlos", "David"]
    notas = [90, 85, 78, 95]

    for estudiante, nota in zip(estudiantes, notas):
        print(estudiante, "Nota:", nota)


def ejercicio_2():
    print("\n===== EJERCICIO 2: DISPOSITIVOS Y DIRECCIONES IP =====")

    dispositivos = [
        "Laptop",
        "Router",
        "Servidor",
        "Switch"
    ]

    direcciones_ip = [
        "192.168.1.10",
        "192.168.1.1",
        "192.168.1.20",
        "192.168.1.30"
    ]

    registro = dict(zip(dispositivos, direcciones_ip))

    print("Diccionario dispositivo-IP:")
    print(registro)


def ejercicio_3():
    print("\n===== EJERCICIO 3: DISPOSITIVO, IP Y ESTADO =====")

    nombres = [
        "Equipo 1",
        "Equipo 2",
        "Equipo 3"
    ]

    modelos = [
        "Dell Latitude",
        "ThinkPad T14",
        "HP ProBook"
    ]

    ips = [
        "192.168.1.10",
        "192.168.1.11",
        "192.168.1.12"
    ]

    estados = [
        "Activo",
        "Mantenimiento",
        "Activo"
    ]

    for nombre, modelo, ip, estado in zip(nombres, modelos, ips, estados):
        print("Nombre:", nombre)
        print("Modelo:", modelo)
        print("IP:", ip)
        print("Estado:", estado)
        print()


def ejercicio_4():
    print("\n===== EJERCICIO 4: COMPARACION DE CONSUMO DE DATOS =====")

    semana_1 = [100, 120, 150, 130, 140, 160, 170]
    semana_2 = [110, 100, 160, 120, 150, 180, 165]

    dias = [
        "Lunes",
        "Martes",
        "Miercoles",
        "Jueves",
        "Viernes",
        "Sabado",
        "Domingo"
    ]

    for dia, consumo1, consumo2 in zip(dias, semana_1, semana_2):
        diferencia = consumo2 - consumo1

        print(dia, "Diferencia:", diferencia)


def ejercicio_5():
    print("\n===== EJERCICIO 5: CONSTRUCCION DE REGISTROS DE USUARIOS =====")

    nombres = ["Ana", "Luis", "David"]
    edades = [18, 20, 17]
    ciudades = ["Managua", "Masaya", "Granada"]

    usuarios = []

    for nombre, edad, ciudad in zip(nombres, edades, ciudades):
        usuario = {
            "nombre": nombre,
            "edad": edad,
            "ciudad": ciudad
        }

        usuarios.append(usuario)

    print("Registros de usuarios:")
    print(usuarios)