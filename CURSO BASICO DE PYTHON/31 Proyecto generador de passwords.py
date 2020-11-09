import random

def get_data():
    lowercase, uppercase, simbols, numbers = [], [], [], []
    for number in range(97, 123):
        lowercase.append(chr(number)) 
    for number in range(65, 91):
        uppercase.append(chr(number))
    for number in range(91, 97):
        simbols.append(chr(number))
    for number in range(123, 126):
        simbols.append(chr(number))
    for number in range(0,9):
        numbers.append(number)
    return lowercase, uppercase, simbols, numbers


def get_simple_password():
    password = ''
    lowercase, uppercase, simbols, numbers = get_data()
    while len(password) < 4:
        password += random.choice(lowercase)
    while len(password) < 8:
        password += random.choice(uppercase)
    while len(password) < 12:
        password += random.choice(simbols)
    while len(password) < 16:
        password += str(random.choice(numbers))
    return password


def get_password_no_characters_repeat():
    password = ''
    lowercase, uppercase, simbols, numbers = get_data()
    while len(password) < 4:
        character = random.choice(lowercase)
        if character in password:
            continue
        password += character
    while len(password) < 8:
        character = random.choice(uppercase)
        if character in password:
            continue
        password += character
    while len(password) < 12:
        character = random.choice(simbols)
        if character in password:
            continue
        password += character
    while len(password) < 16:
        character = str(random.choice(numbers))
        if character in password:
            continue
        password += character
    return password

def get_password_no_characters_repeat_mixed():
    password = ''
    lowercase, uppercase, simbols, numbers = get_data()
    characters = lowercase + uppercase + simbols + numbers
    while len(password) < 16:
        character = str(random.choice(characters))
        if character in password:
            continue
        password += character
    return password

def run():
    password = get_simple_password()
    print('Simple password: ' + password)
    password = get_password_no_characters_repeat()
    print('Password no characters repeat: ' + password)
    password = get_password_no_characters_repeat_mixed()
    print('Password no characters repeat mixed: ' + password)

if __name__ == '__main__':
    run()