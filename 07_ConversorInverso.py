def exchanges(moneda,cantidad):
    result = 0
    # Moneda chilena
    if moneda == 1:
        result = cantidad * 0.0013
        result = round(result, 2)
        print(f'Los {cantidad} pesos chilenos equivalen a {result} dólares')
    # Moneda colombiana
    elif moneda == 2:
        result = cantidad * 0.00027
        result = round(result, 2)
        print(f'Los {cantidad} pesos colombianos equivalen a {result} dólares')
    # Moneda Argentina
    elif moneda == 3:
        result = cantidad * 0.014
        result = round(result, 2)
        print(f'Los {cantidad} pesos argentinos equivalen a {result} dólares')
    # Moneda mexicana
    elif moneda == 4:
        result = cantidad * 0.044
        result = round(result, 2)
        print(f'Los {cantidad} pesos mexicanos equivalen a {result} dólares')
    #Moneda Peruana Cara Fachera
    elif moneda == 5:
        result = cantidad * 0.28
        result = round(result, 2)
        print(f'La {cantidad} soles equivalen a {result} dólares')
    # Otro
    else:
        print('Ingresa solo un numero de la lista')


if __name__ == '__main__':
    try:
        moneda = int(input('''
        Ingresa el indice de la moneda que quieres convertira  dolar:
            [1] Moneda chilena(pesos) a Dólar
            [2] Moneda colombiana(pesos) a Dólar
            [3] Moneda argentida(pesos) a Dólar
            [4] Moneda mexicana(pesos) a Dólar
            [5] Moneda peruana(soles) a Dólar
        Selecciona: '''))
        print('********************************')
        cantidad = int(input('Ingresa la cantidad que quieres convertir: '))
        exchanges(moneda,cantidad)
    except:
        print('* * * * * * E R R O R * * * * * *')
        print('Por favor, Ingresa solo valores numericos')
