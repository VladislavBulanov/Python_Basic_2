def generate_data_list(elements_quantity):
    return [input(f'{index + 1}-я страна '
            '(введите страну и её города через пробел):\n').split()
            for index in range(elements_quantity)]


def generate_countries_navigator(inputted_data_list):
    return {item[0]: item[1:] for item in inputted_data_list}


def find_country(navigator, input_city):
    for key, value in navigator.items():
        if input_city in value:
            return key
    else:
        return False


country_quantity = int(input('Введите количество стран: '))
data_list = generate_data_list(country_quantity)
countries_navigator = generate_countries_navigator(data_list)

for number in range(3):
    city = input(f'\n{number + 1}-й город: ')
    found_country = find_country(countries_navigator, city)

    if found_country:
        print(f'Город {city} расположен в стране {found_country}.')
    else:
        print(f'По городу {city} данных нет.')
