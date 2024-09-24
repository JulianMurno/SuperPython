#1) Práctica Método Index() 1
# Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
palabra = "ordenador"
resultado = palabra[5]

#2) Práctica Método Index() 2
# Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))
#3) Práctica Método Index() 3
# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex("práctica"))

# Práctica Métodos de String 1
# Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
texto  = "hola mundo"
print(texto.upper())



# Práctica Métodos de String 2
# Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
print(" ".join(lista_palabras))



# Práctica Métodos de String 3
# Reemplaza en la siguiente frase:
# "Si la implementación es difícil de explicar, puede que sea una mala idea."
# los siguientes pares de palabras:
# "difícil" --> "fácil"
# "mala" --> "buena"
# y muestra en pantalla la frase con ambas palabras modificadas.
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase = frase.replace("difícil", "fácil")
frase = frase.replace("mala", "buena")

# Práctica Sub-Strings 1
# Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
# "Controlar la complejidad es la esencia de la programación"
frase = "Controlar la complejidad es la esencia de la programación"
print(frase[:10])


# Práctica Sub-Strings 2
# Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
# "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])



# Práctica Sub-Strings 3
# Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
# "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[::-1])