import random

def run():
    input('Hola, juguemos un juego, adivina el número que tengo en la mente.')
    number = random.randint(0,100)
    user_value = -1
    while number != user_value:
        user_value = int(input('del 0 al 100 ¿en qué número estoy pensando? Respuesta: '))
        if user_value > number:
            print('El número que pienso es más pequeño')
        elif user_value < number:
            print('El número que pienso es más grande')
    print('Fin del juego, adivinaste! te ganaste una palmadita en la espalda :)')  

if __name__ == '__main__':
    run()