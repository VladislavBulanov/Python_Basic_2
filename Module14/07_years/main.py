# Задача 7. Годы


def count_same_digits(number):
    for digit in str(number):
        if str(number).count(digit) == 3:
            print(number)
            break


while True:
    first_year = int(input('Введите первый год: '))
    second_year = int(input('Введите второй год: '))
    if first_year > second_year:
        print('Неверный ввод: первый год должен быть меньше второго.\n')
    else:
        break

print(f'\nГоды с {first_year} по {second_year} с тремя одинаковыми цифрами:')
for year in range(first_year, second_year + 1):
    count_same_digits(year)
