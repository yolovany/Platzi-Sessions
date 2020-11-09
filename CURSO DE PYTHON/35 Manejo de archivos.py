# -*- coding: utf-8 -*-

def run():
    _file = open('numeros.txt', 'w')
    for i in range(0, 10):
        _file.write(str(i))
    _file.close()


if __name__ == '__main__':
    run()