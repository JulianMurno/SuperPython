texto = input("Escribe un texto: ")

texto_analizar = texto.lower()

def encontrar_python():
    if "python" in texto_analizar:
        print("5. La palabra 'Python' se encuentra en el texto")
    else:
        print("5. La palabra 'Python' no se encuentra en el texto")

print(texto)



letras = list(texto_analizar)

print("1. La lista de letras es:", letras)

sub_string = input("Escribe un substring para buscar: ")
contador = texto_analizar.count(sub_string)

print(f"El substring '{sub_string}' aparece {contador} veces en el texto")

print("2. Hay ", len(texto_analizar), "palabras en el texto")
print("3. La primera letra del texto es: ", texto_analizar[0], ". Y la ultima letra del texto es", texto_analizar[-1], ".")
print(f"4. Hay {texto_analizar.split()} palabras en el texto")
print(encontrar_python())
