import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busaca un numero mas grande")

        elif numero_elegido > 100:
            print("¡Elige un número del 1 al 100!")

        else:
            print("Busca un numero mas pequeño")
        numero_elegido = int(input("Elige otro número: "))
    print("Ganaste!")


if __name__ == "__main__":
    run()
