def run():
    init = 1000
    limit = init
    while limit >= 0:
        pow = init-limit
        print('2 elevado a ' + str(pow) + ' es igual a ' + str(2**pow))
        limit = limit - 1

if __name__ == '__main__':
    run()