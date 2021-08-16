import random

is_game = True


def conversacion(mensaje):
    if mensaje == "piedra":
        return 1
    elif mensaje == "papel":
        return 2
    elif mensaje == "tijera":
        return 3
    else:
        return 0


def quien_gano(oponente, ususario):
    if oponente == 1 and usuario == 2:
        return "Ganaste B)"
    elif oponente == 2 and usuario == 1:
        return "Perdiste,vuelve a intentarlo"
    elif oponente == 1 and usuario == 3:
        return "Perdiste,vuelve a intentarlo"
    elif oponente == 3 and usuario == 1:
        return "Ganaste B)"
    elif oponente == 2 and usuario == 3:
        return "Ganaste B)"
    elif oponente == 3 and usuario == 1:
        return "Perdiste,vuelve a intentarlo"
    elif oponente == usuario:
        return "Empate, salu2"
    elif oponente == 0 or usuario == 0:
        return "Esa no es una opcion valida,recuerda que tienes que poner las opciones en minusculas"
    else:
        return "Esa no es una opcion valida,recuerda que tienes que poner las opciones en minusculas"


def seguir_jugando(respuesta):
    if respuesta == "si":
        return True
    else:
        return False


bienvenida = """ 
██████╗ ██╗███████╗██████╗ ██████╗  █████╗ 
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
██████╔╝██║█████╗  ██║  ██║██████╔╝███████║
██╔═══╝ ██║██╔══╝  ██║  ██║██╔══██╗██╔══██║
██║     ██║███████╗██████╔╝██║  ██║██║  ██║
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

  ██████╗  █████╗ ██████╗ ███████╗██╗     
  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║     
  ██████╔╝███████║██████╔╝█████╗  ██║     
  ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██║     
  ██║     ██║  ██║██║     ███████╗███████╗
  ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝

                   ██████╗ 
                  ██╔═══██╗
                  ██║   ██║
                  ██║   ██║
                  ╚██████╔╝

████████╗██╗     ██╗███████╗██████╗  █████╗ 
╚══██╔══╝██║     ██║██╔════╝██╔══██╗██╔══██╗
   ██║   ██║     ██║█████╗  ██████╔╝███████║
   ██║   ██║██   ██║██╔══╝  ██╔══██╗██╔══██║
   ██║   ██║╚█████╔╝███████╗██║  ██║██║  ██║
   ╚═╝   ╚═╝ ╚════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
___________________________________________

"""

print(bienvenida)

while is_game:
    oponente = random.randint(1, 3)
    usuario = conversacion(
        input("Escribe piedra, papel o tijera segun lo que hayas escogido: ")
    )

    print(quien_gano(oponente, usuario))
    is_game = seguir_jugando(input("Quieres seguir jugando? "))
