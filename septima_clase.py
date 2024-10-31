class Pajaro:
    pass

tucan = Pajaro()
hornero = Pajaro()

print(tucan)
print(type(tucan))
print(hornero)
print(type(hornero))

# Práctica Clases 1
# Crea una clase llamada Personaje y a continuación, crea un objeto a partir de ella, por ejemplo: harry_potter
class Personaje:
    def __init__(self, nombre, edad, habilidad):
        self.nombre = nombre
        self.edad = edad
        self.habilidad = habilidad        

harry_potter = Personaje("Harry Potter", 17, "Magia")
print(harry_potter.nombre)




# Práctica Clases 2
# Crea una clase llamada Dinosaurio, y tres instancias a partir de ella: velociraptor, tiranosaurio_rex y braquiosaurio .
class Dinosaurio:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        def __str__(self):
            return f"Nombre: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}"
    

velociraptor = Dinosaurio("Velociraptor", 30, "Carnívoro")
tiranosaurio_rex = Dinosaurio("Tiranosaurio Rex", 40 , "Carnívoro")
braquiosaurio = Dinosaurio("Braquiosaurio", 50,  "Herbívoro")


# Práctica Clases 3
# Crea una clase llamada PlataformaStreaming y crea los siguientes objetos a partir de ella: netflix, hbo_max, amazon_prime_video
class PlataformaStreaming:
    def __init__(self, nombre, contenido, precio):
        self.nombre = nombre
        self.contenido = contenido
        self.precio = precio
        def __str__(self):
            return f"Nombre: {self.nombre}, Contenido: {self.contenido}, Precio: {self.precio}"

# Crear los objetos
netflix = PlataformaStreaming("Netflix", "Películas y series", 8.99)
hbo_max = PlataformaStreaming("HBO Max", "Películas y series",  14.99)
amazon_prime_video = PlataformaStreaming("Amazon Prime Video", "Películas y series",  12.99)


#-----------------------------------------------------------------------------------
#Atributos

class Pajaro():

    alas = True
    def __init__(self, color, especie):
        self.color=color
        self.especie=especie

mi_pajaro = Pajaro("negro","tucan")

print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")


# Práctica Atributos 1
# Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.
class Casa:
    color = "Blanco"
    cantidad_pisos = 2
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos






# Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.
mi_casa = Casa("Blanco", 4)
print(f"Mi casa es de color {mi_casa.color} y tiene {mi_casa.cantidad_pisos} pisos")

# Práctica Atributos 2
# Crea una clase llamada Cubo, y asígnale el atributo de clase:

# caras = 6

# y el atributo de instancia:

# color
class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color


# Crea una instancia cubo_rojo, de dicho color.
mi_cubo = Cubo("Rojo")
print(f"Mi cubo tiene {mi_cubo.caras} caras y es de color {mi_cubo.color}")

        



# Práctica Atributos 3
# Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:

# real = False

# Crea una instancia llamada harry_potter con los siguientes atributos de instancia:

# especie = "Humano"

# magico = True

# edad = 17

class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

mi_personaje = Personaje("Humano", True, 17)
print(f"Mi personaje es {mi_personaje.especie}, es {mi_personaje .magico} y tiene {mi_personaje.edad} años")

#---------------------------------------------------------------------------------------

#metodos


class Pajaro():

    alas = True
    def __init__(self, color, especie):
        self.color=color
        self.especie=especie

    def piar(self):
        print('pio')
    
    def volar(self, metros):
        print(f"El pajaro {self.especie} ha volado {metros} metros")
    
    


mi_pajaro = Pajaro("negro","tucan")

print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

mi_pajaro.piar()
mi_pajaro.volar(500)



# Práctica Métodos 1
# Crea una clase Perro. Dicho perro debe poder ladrar.
# Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    def ladrar(self):
        print("Guau!")

mi_perro = Perro("Simon", "Golden Retriever")
mi_perro.ladrar()


# Práctica Métodos 2
# Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").
# Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.
class Mago:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
merlin = Mago("Merlin", "Mágico")
merlin.lanzar_hechizo()


# Práctica Métodos 3
# Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje
# "La alarma ha sido pospuesta {cantidad_minutos} minutos"
class Alarma:
    def __init__(self, hora, minutos):
        self.hora = hora
        self.minutos = minutos
    def postergar(self, cantidad_minutos):
        self.minutos += cantidad_minutos
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
mi_alarma = Alarma(10, 30)
mi_alarma.postergar(10)



class Pajaro():

    alas = True
    def __init__(self, color, especie):
        self.color=color
        self.especie=especie

    def piar(self):
        print('pio')
    
    def volar(self, metros):
        print(f"El pajaro {self.especie} ha volado {metros} metros")
        self.piar()

    def pintar_pajaro(self):
        self.color="verde"
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Poner {cantidad} huevos")
        cls.alas=False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira ")

mi_pajaro = Pajaro("negro","tucan")

print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

mi_pajaro.piar()
mi_pajaro.volar(500)

mi_pajaro.alas =False
print(mi_pajaro.alas)

Pajaro.poner_huevos(2)
Pajaro.mirar()



# Práctica Tipos de Métodos 1
# Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"

class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


# Práctica Tipos de Métodos 2
# Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado.
# El valor predeterminado del atributo vivo, debe ser False.

class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True


# Práctica Tipos de Métodos 3
# Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, 
# que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1


# Práctica Herencia 1
# Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. 
# Crea otra clase, Alumno, que herede de la primera estos atributos.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass


# Práctica Herencia 2
# Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas.
# Crea otra clase, Perro, que herede de la primera sus atributos

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass


# Práctica Herencia 3
# Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los métodos en blanco con pass).
# Crea una clase llamada Automovil que herede estos métodos de Vehiculo.

class Vehiculo:
    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass


# Práctica Herencia Extendida 1
# Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, 
# y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita a esta clase heredar correctamente de Padre y Madre.

class Padre:
    def reir(self):
        print("Ja ja")

class Madre:
    def vocacion(self):
        print("Vocación de la madre")

class Hija(Padre, Madre):
    pass


# Práctica Herencia Extendida 2
# Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, 
# tal que "construyas" un animal que tiene los siguientes métodos y atributos.

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass


# Práctica Herencia Extendida 3
# Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. 
# Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo el método hobby().

class Padre:
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    
    def reir(self):
        return "Jajaja"
    
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    
    def caminar(self):
        return "Caminando con pasos largos y rápidos"

class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"


# Práctica Polimorfismo 1
# Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla su longitud con la función len().

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

objetos = [palabra, lista, tupla]
for objeto in objetos:
    print(len(objeto))


# Práctica Polimorfismo 2
# Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai.

class Mago:
    def atacar(self):
        print("Ataque mágico")

class Arquero:
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai:
    def atacar(self):
        print("Ataque con katana")

personajes = [Arquero(), Mago(), Samurai()]
for personaje in personajes:
    personaje.atacar()


# Práctica Polimorfismo 3
# Crea una función llamada personaje_defender() que reciba un objeto y ejecute su método defender().

class Mago:
    def defender(self):
        print("Escudo mágico")

class Arquero:
    def defender(self):
        print("Esconderse")

class Samurai:
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()


# Práctica Métodos Especiales 1
# Dada la clase Libro, implementa el método especial __str__.

class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'


# Práctica Métodos Especiales 2
# Implementa el método especial __len__.

class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas


# Práctica Métodos Especiales 3
# Implementa el método especial __del__ para que el usuario sea informado con el mensaje "Libro eliminado".

class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    
    def __del__(self):
        print("Libro eliminado")
