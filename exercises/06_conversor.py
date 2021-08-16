valorQueQuiereConvertir = input("A que moneda quieres convertir tus soles?: ")

if valorQueQuiereConvertir == "dolar":
    soles = input("Ingresa la cantidad de soles que tienes: ")
    soles = float(soles)

    valorDolar = 3.61
    dolares = soles / valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)

    print("Tienes $" + dolares)

else:
    print("Busca en goole")
