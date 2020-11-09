from random import choice
from os import system

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [
    'DANIEL', 
    'ROMULO', 
    'DIEGO', 
    'ISRAEL', 
    'ALMA', 
    'RAFAEL', 
    'ARISAI', 
    'GERMAN', 
    'RAMON', 
    'ANTONIO', 
    'RUBEN', 
    'FABIOLA', 
    'MELISA', 
    'GISELA',
    'ROBERTO',
    'ALEJANDRO',
    'CARLOS',
    'DAVID',
    'SERGIO',
]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)

def get_index(word, letter, indexes):
    for index in range(0, len(word)):
        if word[index] == letter and index not in indexes:
            indexes.append(index)
            break
        else:
            index = -1
    return index

def run():
    input('B I E N V E N I D O  A L  H I M A L A Y A :)')
    tries = 0
    word = choice(WORDS)
    word_aux = list(word)
    hidden_word = ['---'] * len(word)
    indexes = []
    while True:
        system('cls')
        display_board(hidden_word, tries)
        print('')
        if len(word_aux) == 0:
            print('FIN DEL JUEGO: GANASTE! :)')
            break
        elif (tries < len(IMAGES) - 1):
            
            letter = input('Elige una letra: ').upper()
        else:
            input('FIN DEL JUEGO: PERDISTE! LA PALABRA CORRECTA ERA: ' + word)
            break
        
        index = get_index(word, letter, indexes)
        if index >= 0:
            hidden_word[index] = letter
            index = word_aux.index(letter)
            word_aux.pop(index)
        else:
            tries += 1

if __name__ == '__main__':
    run()