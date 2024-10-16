nombre = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
edades = [65,29,25]
ciudades = ['lima','madrid','mexico']

combinados = list(zip(nombre, edades, ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")


# Práctica Zip 1
# Mostrar frases como "La capital de Alemania es Berlín"
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinacion = list(zip(paises, capitales))
for pais, capital in combinacion:
    print(f"La capital de {pais} es {capital}")


# Práctica Zip 2
# Zip entre marcas y productos
marcas = ["ford", "chevrolet", "lancia", "audi", "fiat", "volkswagen", "IKA"]
productos = ["mustang", "corvette", "delta integrale", "S4", "125 bialbero", "gol power", "torino tsx"]

mi_zip = list(zip(marcas, productos))
print(mi_zip)


# Práctica Zip 3
# Zip con números en español, portugués e inglés
numeros_espaniol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
numeros_portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
numeros_ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(numeros_espaniol, numeros_portugues, numeros_ingles))
print(numeros)


# Práctica Min y Max 1
# Valor máximo de la lista
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(f"El valor máximo es: {valor_maximo}")


# Práctica Min y Max 2
# Diferencia entre valor máximo y mínimo
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)
print(f"La diferencia entre el máximo y el mínimo es: {rango}")


# Práctica Min y Max 3
# Mínimo valor y último nombre en orden alfabético
diccionario_edades = {"Carlos": 55, "María": 42, "Mabel": 78, "José": 44, "Lucas": 24, "Rocío": 35, "Sebastián": 19, "Catalina": 2, "Darío": 49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(f"La edad mínima es: {edad_minima}")
print(f"El último nombre en orden alfabético es: {ultimo_nombre}")


# Práctica Random 1
# Generar un número aleatorio entre 1 y 10
aleatorio = randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {aleatorio}")


# Práctica Random 2
# Generar un número decimal entre 0 y 1
aleatorio = random()
print(f"Número decimal entre 0 y 1: {aleatorio}")


# Práctica Random 3
# Seleccionar un nombre al azar de la lista
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(f"Nombre seleccionado al azar: {sorteo}")
