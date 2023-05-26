import re


if __name__ == '__main__':
    string_of_numbers = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'"

    cars_pattern = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
    taxi_pattern = r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'

    cars_numbers = re.findall(cars_pattern, string_of_numbers)
    taxi_numbers = re.findall(taxi_pattern, string_of_numbers)

    print('Список номеров частных автомобилей:', cars_numbers)
    print('Список номеров такси:', taxi_numbers)
