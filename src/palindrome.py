
def is_palindrome(text):

    newText = ''.join(c.lower() for c in text if c.isalnum())

    return newText == newText[::-1]


if __name__ == "__main__":
    while True:
        entrada = input("Ingrese una palabra o frase: ")
        if is_palindrome(entrada):
            print(f'"{entrada}" es un palindromo ')
        else:
            print(f'"{entrada}" no es un palindromo ')
