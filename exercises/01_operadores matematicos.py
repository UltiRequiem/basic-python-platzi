import math


def impresion():
    # Hacer una suma:
    print(5 + 6 + 9 + 87)

    # Hacer una resta:
    print(46546 - 544)

    # Hacer una división:
    print(45645456 / 30)

    # Division sin decimales
    print(456 // 3)

    # Resto de la division:
    print(21 % 5)

    # Hacer una potencia
    print(2 ** 2)

    # Hacer una Raiz:
    print(9 ** 0.5)

    math.sqrt(9)


if __name__ == "__main__":
    impresion()

"""
Python respeta la separación de términos, 
por lo que si escribimos 5 + 5 * 2 multiplicará primero 5 x 2. 
En el caso de que quisiéramos que primero sume 5 + 5 ponemos paréntesis: 
(5 + 5) * 2.
"""
