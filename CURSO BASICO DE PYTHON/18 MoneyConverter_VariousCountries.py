def Init():
    menu = """
Bienvenido al conversor de monedas (pesos a dolares) :)

    1 - Pesos colombianos.
    2 - Pesos argentinos.
    3 - Pesos mexicanos

        Elige una opción """
    option = input(menu)
    if option == '1':
        ToDollarsConverter('colombia')
    elif option == '2':
        ToDollarsConverter('argentina')
    elif option == '3':
        ToDollarsConverter('mexico')
    else:
        print('Seleccione una opción para continuar')

def ToDollarsConverter(country):
    if country == 'colombia':
        keyboardInput = float(input("           ¿Cuántos pesos colombianos tienes? "))
        value = 3000
    elif country == 'argentina':
        keyboardInput = float(input("           ¿Cuántos pesos argentinos tienes? "))
        value = 65
    elif country == 'mexico':
        keyboardInput = float(input("           ¿Cuántos pesos mexicanos tienes? "))
        value = 24
                
    dollars = keyboardInput / value
    print("             Conversión: $" + str(dollars) + " dolares.")

Init()