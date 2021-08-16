def currency_converter(currency_type, exchange_rate):
    currency = float(input("Cuantos " + currency_type + " tienes?"))
    dollars = currency / exchange_rate
    dollars = str(round(dollars, 2))
    print("Tienes $" + dollars)


menu = """
Conversor Facha por Zero
Coloca un numero de acuerdo a la moneda que tengas:

1 - Pesos bolivianos
2 - Pesos Mexicanos
3 - Pesos Argentinos
4 - Soles

Escoge una opcion:
"""
user_input = float(input(menu))
if user_input == 1:
    currency_converter("bolivianos", 6.86)
elif user_input == 2:
    currency_converter("pesos mexicanos", 23.38)
elif user_input == 3:
    currency_converter("pesos argentinos", 73.04)
elif user_input == 4:
    currency_converter("soles", 3.5)
else:
    print("Esa no es una opcion valida.")
    print("Salu2")
