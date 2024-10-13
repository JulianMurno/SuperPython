import re

# Validación de nombres
def validar_nombre(nombre):
    patron = "^[A-Za-záéíóúÁÉÍÓÚüÜñÑ ]+$"

    coincidencia = re.match(patron, nombre)
    if coincidencia:
        return True
    else:
        return False

# Ingresar nombres
def ingresar_nombres():
    nombres = []
    while True:
        nombre = input("Ingrese un nombre o 'FIN' para terminar, 'REPETIR' para ver nombres: ")
        if nombre.upper() == "FIN":
            break
        elif nombre.upper() == "REPETIR":
            print("Nombres ingresados hasta ahora:", nombres)
        elif validar_nombre(nombre):
            nombres.append(nombre)
        else:
            print("Nombre inválido. Debe ser solo letras y no estar vacío.")
    return nombres

# Menú de opciones
def mostrar_menu():
    print("""
        1. Mostrar nombres ingresados.
        2. Ordenar los nombres.
        3. Análisis de longitud de los nombres.
        4. Contar vocales y consonantes.
        5. Contar palabras en cada nombre.
        6. Invertir los nombres.
        7. Mostrar solo los nombres que empiezan con una letra en particular.
        8. Buscar si un nombre está en la lista.
        0. Salir.
    """)

# Mostrar nombres ingresados
def mostrar_nombres(nombres):
    print("Nombres ingresados:", nombres)

# Ordenar nombres
def ordenar_nombres(nombres):
    nombres_ordenados = nombres.sort()
    print("Nombres ordenados alfabéticamente:", nombres_ordenados)

# Análisis de longitud
def analisis_longitud(nombres):
    if nombres:
        nombre_largo = max(nombres, key=len)
        nombre_corto = min(nombres, key=len)
        print(f"Nombre más largo: {nombre_largo} ({len(nombre_largo)} letras).")
        print(f"Nombre más corto: {nombre_corto} ({len(nombre_corto)} letras).")

# Contar vocales y consonantes
def contar_vocales_consonantes(nombres):
    vocales = 0
    consonantes = 0

    vocales_set = set("aeiouáéíóú")

    for nombre in nombres:
        nombre_minusculas = nombre.lower()
        
        for letra in nombre_minusculas:
            if letra.isalpha(): 
                if letra in vocales_set:
                    vocales += 1
                else: 
                    consonantes += 1

    print(f"Total de vocales: {vocales}, Total de consonantes: {consonantes}")

# Contar palabras en cada nombre
def contar_palabras(nombres):
    for nombre in nombres:
        print(f"El nombre '{nombre}' tiene {len(nombre.split())} palabra/s.")

# Invertir nombres
def invertir_nombres(nombres):
    nombres_invertidos = [nombre[::-1] for nombre in nombres]
    print("Nombres invertidos:", nombres_invertidos)

# Mostrar nombres que empiezan con una letra
def nombres_por_letra(nombres):
    letra = input("Ingrese la letra por la que deben empezar los nombres: ").lower()
    nombres_filtrados = [nombre for nombre in nombres if nombre.lower().startswith(letra)]
    print(f"Nombres que empiezan con '{letra.upper()}':", nombres_filtrados)

# Buscar un nombre en la lista
def buscar_nombre(nombres):
    nombre_buscado = input("Ingrese el nombre que desea buscar: ")
    nombre_buscado_min  = nombre_buscado.lower()
    if nombre_buscado_min in [nombre.lower() for nombre in nombres]:
        print(f"El nombre '{nombre_buscado}' está en la lista.")
    else:
        print(f"El nombre '{nombre_buscado}' no está en la lista.")

       

# Ingreso y ciclo del menú principal
nombres = ingresar_nombres()
while True:
    mostrar_menu()
    opcion = input("Ingrese la opción que desee: ")
    
    if opcion == "1":
        mostrar_nombres(nombres)
    elif opcion == "2":
        ordenar_nombres(nombres)
    elif opcion == "3":
        analisis_longitud(nombres)
    elif opcion == "4":
        contar_vocales_consonantes(nombres)
    elif opcion == "5":
        contar_palabras(nombres)
    elif opcion == "6":
        invertir_nombres(nombres)
    elif opcion == "7":
        nombres_por_letra(nombres)
    elif opcion == "8":
        buscar_nombre(nombres)
    elif opcion == "0":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
