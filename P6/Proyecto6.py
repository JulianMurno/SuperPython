import os
import shutil

def main():
    ruta_recetas = os.path.join(os.getcwd(), "Recetas")
    
    print("¡Bienvenido al sistema de gestión de recetas!")
    print(f"La ruta de acceso a la carpeta de recetas es: {ruta_recetas}")
    
    total_recetas = sum([len(files) for r, d, files in os.walk(ruta_recetas)])
    print(f"Actualmente, tienes un total de {total_recetas} recetas.\n")

    while True:
        print("Por favor, elige una opción:")
        print("1. Leer una receta")
        print("2. Crear una nueva receta")
        print("3. Crear una nueva categoría")
        print("4. Eliminar una receta")
        print("5. Eliminar una categoría")
        print("6. Salir")
        
        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == "1":
            categoria = elegir_categoria(ruta_recetas)
            if categoria:
                receta = elegir_receta(categoria)
                if receta:
                    mostrar_receta(receta)

        elif opcion == "2":
            categoria = elegir_categoria(ruta_recetas)
            if categoria:
                crear_receta(categoria)

        elif opcion == "3":
            crear_categoria(ruta_recetas)

        elif opcion == "4":
            categoria = elegir_categoria(ruta_recetas)
            if categoria:
                receta = elegir_receta(categoria)
                if receta:
                    eliminar_receta(receta)

        elif opcion == "5":
            eliminar_categoria(ruta_recetas)

        elif opcion == "6":
            print("Gracias por utilizar el sistema de gestión de recetas. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

def elegir_categoria(ruta_recetas):
    categorias = [f for f in os.listdir(ruta_recetas) if os.path.isdir(os.path.join(ruta_recetas, f))]
    if not categorias:
        print("No hay categorías disponibles.")
        return None
    
    print("\nCategorías disponibles:")
    for idx, cat in enumerate(categorias, 1):
        print(f"{idx}. {cat}")
    
    opcion = int(input("Elige el número de la categoría: "))
    if 1 <= opcion <= len(categorias):
        return os.path.join(ruta_recetas, categorias[opcion - 1])
    else:
        print("Opción no válida.")
        return None

def elegir_receta(categoria):
    recetas = [f for f in os.listdir(categoria) if os.path.isfile(os.path.join(categoria, f))]
    if not recetas:
        print("No hay recetas disponibles en esta categoría.")
        return None

    print("\nRecetas disponibles:")
    for idx, rec in enumerate(recetas, 1):
        print(f"{idx}. {rec}")

    opcion = int(input("Elige el número de la receta: "))
    if 1 <= opcion <= len(recetas):
        return os.path.join(categoria, recetas[opcion - 1])
    else:
        print("Opción no válida.")
        return None

def mostrar_receta(ruta_receta):
    with open(ruta_receta, "r") as receta:
        print("\nContenido de la receta:")
        print(receta.read())

def crear_receta(categoria):
    nombre_receta = input("Ingresa el nombre de la nueva receta: ") + ".txt"
    contenido_receta = input("Escribe el contenido de la receta:\n")

    ruta_receta = os.path.join(categoria, nombre_receta)
    with open(ruta_receta, "w") as receta:
        receta.write(contenido_receta)
    
    print(f"Receta '{nombre_receta}' creada exitosamente en la categoría.")

def crear_categoria(ruta_recetas):
    nombre_categoria = input("Ingresa el nombre de la nueva categoría: ")
    ruta_categoria = os.path.join(ruta_recetas, nombre_categoria)
    if not os.path.exists(ruta_categoria):
        os.makedirs(ruta_categoria)
        print(f"Categoría '{nombre_categoria}' creada exitosamente.")
    else:
        print("La categoría ya existe.")

def eliminar_receta(ruta_receta):
    os.remove(ruta_receta)
    print("Receta eliminada exitosamente.")

def eliminar_categoria(ruta_recetas):
    categoria = elegir_categoria(ruta_recetas)
    if categoria:
        shutil.rmtree(categoria)
        print("Categoría eliminada exitosamente.")

if __name__ == "__main__":
    main()
