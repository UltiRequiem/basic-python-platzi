def tablas(numero):
    print('Esta es la tabla del ' + str(numero) + ':')
    for i in range(1,13):
        print(i*numero)

menu = """
Las tablas de Multiplicar del  al 12 

1 - Tabla del 1
2 - Tabla del 2
3 - Tabla del 3
4 - Tabla del 4
5 - Tabla del 5
6 - Tabla del 6
7 - Tabla del 7
8 - Tabla del 8
9 - Tabla del 9
10 - Tabla del 10
11 - Tabla del 11
12 - Tabla del 12

Escoge que tabla deseas ver:
"""
user_input = str(input(menu))

if user_input == '1':
    tablas(1)
elif user_input == '2':
    tablas(2)
elif user_input == '3':
    tablas(3)
elif user_input == '4':
    tablas(4)
elif user_input == '5':
    tablas(5)
elif user_input == '6':
    tablas(6)
elif user_input == '7':
    tablas(7)
elif user_input == '8':
    tablas(8)
elif user_input == '9':
    tablas(9)
elif user_input == '10':
    tablas(10)
elif user_input == '11':
    tablas(11)
elif user_input == '12':
    tablas(12)


