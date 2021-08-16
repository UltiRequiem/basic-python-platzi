def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return True if (palabra == palabra[::-1]) else False


def main():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__":
    main()
