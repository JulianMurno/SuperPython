import random

def elegir_palabra():
  palabras = ['manzana', 'banana', 'naranja', 'pera', 'uva']
  return random.choice(palabras)

def mostrar_estado(palabra_oculta, letras_adivinadas):
  estado = ""
  for letra in palabra_oculta:
    if letra in letras_adivinadas:
      estado += letra
    else:
      estado += "_"
  print(estado)

def jugar():
  palabra = elegir_palabra()
  letras_adivinadas = []
  vidas = 6

  while vidas > 0:
    mostrar_estado(palabra, letras_adivinadas)
    letra = input("Ingresa una letra: ").lower()

    if letra in palabra:
      letras_adivinadas.append(letra)
      if set(letras_adivinadas) == set(palabra):
        print("¡Felicidades! Has adivinado la palabra:", palabra)
        return
    else:
      vidas -= 1
      print("Letra incorrecta. Te quedan", vidas, "vidas.")

  print("¡Has perdido! La palabra era:", palabra)

jugar()