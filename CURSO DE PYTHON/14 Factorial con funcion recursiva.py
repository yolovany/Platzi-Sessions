# -*- coding: utf-8 -*-


def get_factorial(number):
    factorial = 1
    if(number != 0):
        factorial = number * get_factorial(number - 1)
    return factorial


def run():
    entry = input('Ingrese un número entero: ')
    factorial = get_factorial(int(entry))
    print('El factorial de ' + entry + ' es ' + str(factorial))


if __name__ == '__main__':
    run()