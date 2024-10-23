# Ejercicio 1

def devolver_distintos(num1, num2, num3):

  numeros = [num1, num2, num3]
  suma = sum(numeros)

  if suma > 15:
    return max(numeros)
  elif suma < 10:
    return min(numeros)
  else:
    
    numeros.sort()
    return numeros[1]

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numero_3 = int(input("Ingrese el tercer número: "))

resultado = devolver_distintos(numero_1, numero_2, numero_3)
print(resultado) 
print("-------------------------------------------------------------------")
# Ejercicio 2
def letras_unicas_ordenadas(palabra):

  letras_unicas = set(palabra)
  letras_ordenadas = sorted(list(letras_unicas))

  return letras_ordenadas

palabra = input("Escribe una palabra")
resultado = letras_unicas_ordenadas(palabra)
print(resultado)
print("-------------------------------------------------------------------")
# Ejercicio 3
def ceros_consecutivos(*args):
  for i in range(len(args) - 1):
    if args[i] == 0 and args[i+1] == 0:
      return True
  return False

cantidad = int(input("Cantidad de numeros: "))
numeros = [int(input(f"Numero {i+1}: ")) for i in range(cantidad)]

print(ceros_consecutivos(numeros))
print("-------------------------------------------------------------------")
# Ejercicio 4
def contar_primos(numero):
  """
  Cuenta los números primos desde 0 hasta el número ingresado y los imprime.

  Args:
    numero: El límite superior del rango a buscar números primos.

  Returns:
    La cantidad de números primos encontrados.
  """

  contador_primos = 0
  print("Números primos hasta", numero, ":")
  for num in range(2, numero + 1):
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        es_primo = False
        break
    if es_primo:
      print(num)
      contador_primos += 1
  return contador_primos


limite = int(input("Ingrese un número: "))
cantidad_primos = contar_primos(limite)
print("Se encontraron", cantidad_primos, "números primos.")
