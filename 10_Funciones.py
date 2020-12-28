def mensajeEspecial():
    print('Mensaje Especial!')
    print('Estoy Aprendiendo Python!')

#mensaje()

def conversacion(mensaje):
    print('Hola!')
    print('Cómo estas?')
    print(mensaje)
    print('Adios')

opcion =  int(input('Elige una opcion (1, 2, 3,): '))
if opcion == 1:
    conversacion('Elegiste la Opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
elif opcion == 3:
    conversacion('Elegiste la opción 3')
else:
    print('No sabes leer?Solo 1, 2 o 3.')

