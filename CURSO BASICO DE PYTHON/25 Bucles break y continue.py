def run():
    for count in range(1000):
        if count == 0:
            continue
        print(str(count))
    
    text = input('Escribe algo interesante: ')
    for letter in text:
        if letter == 'u':
            break
        print(letter.upper())

if __name__ == '__main__':
    run()