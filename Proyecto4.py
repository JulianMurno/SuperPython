# La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número”.
from random import *
vidas =  8
nombre = input("Hola! Como te llamas: ")

# Obtener numero random entre 1 y 100
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")
numero = randint(1, 100)

# print(numero)

while  vidas > 0:
    elegir = int(input("Elige un numero entre  1 y 100: "))
    if elegir == numero:
        print("¡Lo has adivinado! El número era " + str(numero))
        print("Te han quedado  " + str(vidas) + " vidas")
        vidas  = 0
        break
    else:
        vidas = vidas - 1
        print('-----------------------------------------------')
        print("Ups! No adivinaste esta vez.")
        print("Te quedan " + str(vidas) + " vidas")
        print('-----------------------------------------------')
print("El número a adivinar " + str(numero))
print('-----------------------------------------------')
