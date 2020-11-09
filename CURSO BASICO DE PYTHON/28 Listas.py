def run():
    lista = ['uno', 2, True, 4.5]
    print(lista)
    lista.append(False)
    print(lista)
    lista.pop(0)
    print(lista)


if __name__ == '__main__':
    run()