# -*- coding: utf-8 -*-

def search(numbers, number, init_index, end_index):
    if init_index > end_index:
        return False
    
    middle = (init_index + end_index) // 2
    aux = numbers[middle]

    if aux == number:
        return True

    elif aux > number:
        return search(numbers, number, init_index, middle - 1)
    else:
        return search(numbers, number, middle + 1, end_index)
    

def run():
    numbers = []
    for i in range(1, 101):
        print('Generando lista, por favor espere')
        numbers.append(i)
    number = input('Elija un número a buscar: ')
    number = int(number)
    if search(numbers, number, 0, len(numbers) - 1):
        print('El número ' + str(number) + ' está en la lista :)')
    else:
        print('El número ' + str(number) + ' no está en la lista :(')

if __name__ == '__main__':
    run()