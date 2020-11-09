# un número primo es un número mayor a 1  que sólo tiene dos números que lo dividen con resultado entero: el 1 y a sí mismo.

def es_primo(number):
    number = int(number)
    if number == 1:
        return False
    else:
        count = 0
        for i in range(1,number + 1):
            if i == 1 or i == number:
                continue
            if number % i == 0:
                count += 1
        return count == 0


def run():
    number = input('Escribe un número: ')
    if es_primo(number):
        print('El número ' + str(number) + ' es primo')
    else:
        print('El número ' + str(number) + ' no es primo')
    run()


if __name__ == '__main__':
    run()