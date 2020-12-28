import random 


def  generate_password():
    mayusculas  = ['A','B','C','D','E']
    minusculas = ['a','b','c','d','e','i','o','u']
    simbolos = ['!','"','#','$','%','&','/']
    numeros = ['1','2','3','4','5','6','7','8','9','10']

    caracters = mayusculas + minusculas + simbolos + numeros

    password = []
    for i in range(15):
        caracter_random = random.choice(caracters)
        password.append(caracter_random)

    password = "".join(password)
    return password 



def run():
    password = generate_password()
    print('Your new password is: ' + password)


if __name__ == '__main__':
    run()
