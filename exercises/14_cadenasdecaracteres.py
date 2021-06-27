nombre = input("¿Cuál es tu nombre?: ")
nombre = nombre.capitalize().strip()

print("Tu nombre capitalizado es "+nombre)

indice = input("Escribe una palabra y te mostrare cual es su indice 2: ")
print("El Indice 2 es '"+indice[2]+"'")

'''
variable.upper() = 'todos los caracteres en MAYÚSCULAS'
variable.capitalize() = 'solo la primera en MAYÚSCULA'
variable.lower() = 'todos los caracteres en minúscula'
variable.strip() = 'eliminar espacios basura del string'
variable.replace('caractera a cambiar', 'caracter por poner') = remplazar caracter
'''

#FUNCIONES BILT IN
'''Aquellas que son propias del lenguaje y que no tenemos que crearlas, solo invocarlas.'''
#len()
#print()
#input()


cadena = "Esta es una cadena de texto larga,bastante larga."
print("La cadena de texto tiene "+str(len(cadena))+" caracteres.")