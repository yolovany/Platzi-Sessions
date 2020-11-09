def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    otra_palabra = palabra[::-1]
    return palabra == otra_palabra

def run():
    palabra = input('Escribe una palabra: ')
    if palindromo(palabra):
        print('Es palindromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()