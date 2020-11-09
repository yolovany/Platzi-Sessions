def run():
    dictionary = {
        'key1': 1,
        'key2': 2,
        'key3': 3,
    }
    
    print(dictionary)
    print(dictionary['key2'])
    print(dictionary['key1'])
    print(dictionary['key3'])

    countries = {
        'Argentina': 11111,
        'Brasil': 22222,
        'Colombia': 33333,
    }

    for country in countries.keys():
        print(country)
    for value in countries.values():
        print(str(value))
    for country, population in countries.items():
        print('En ' + country + ' hay ' + str(population) + ' habitantes')

if __name__ == '__main__':
    run()