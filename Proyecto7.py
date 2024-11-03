class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0.0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Cuenta: {self.numero_cuenta}, Balance: ${self.balance:.2f}"

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Has depositado ${monto:.2f}. Balance actual: ${self.balance:.2f}")
        else:
            print("El monto de depósito debe ser positivo.")

    def retirar(self, monto):
        if monto > 0:
            if monto <= self.balance:
                self.balance -= monto
                print(f"Has retirado ${monto:.2f}. Balance actual: ${self.balance:.2f}")
            else:
                print("No puedes retirar más de tu balance actual.")
        else:
            print("El monto de retiro debe ser positivo.")

def ejecutar_operaciones_cliente():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    numero_cuenta = input("Ingresa tu número de cuenta: ")

    cliente = Cliente(nombre, apellido, numero_cuenta)

    print("\n¡Bienvenido!", cliente)

    while True:
        print("\nOpciones:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            cliente.depositar(monto)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            cliente.retirar(monto)
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

ejecutar_operaciones_cliente()
