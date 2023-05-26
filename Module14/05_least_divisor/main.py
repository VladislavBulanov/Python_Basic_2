# Задача 5. Наименьший делитель


def min_divider(number):
    divider = 2

    if number % divider == 0:
        return 2

    divider = 3
    while (number % divider != 0) and (divider ** 2 <= number):
        divider += 2

    if divider ** 2 <= number:
        return divider

    return number


while True:
    number = int(input('\nВведите натуральное число (n > 1): '))
    if number <= 1:
        print('Число не соответствует условию. Пожалуйста, повторите ввод.')
    else:
        break

print(f'\nНаименьший делитель числа {number}, отличный от единицы, равен', end=' ')
print(min_divider(number))
