# Задача 4. Число наоборот 3


def backwards_number(number):
    versa_integer_part = ''
    versa_fractional_part = ''
    integer = True
    power = 0

    for letter in str(number):
        if letter == '.':
            integer = False
            continue
        if integer:
            versa_integer_part = letter + versa_integer_part
        else:
            versa_fractional_part = letter + versa_fractional_part
            power -= 1

    versa_number = int(versa_integer_part) + (int(versa_fractional_part) * 10 ** power)
    return versa_number


number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число: '))

first_backwards_number = backwards_number(number_1)
second_backwards_number = backwards_number(number_2)

print('\nПервое число наоборот:', first_backwards_number)
print('Второе число наоборот:', second_backwards_number)
print('Сумма:', first_backwards_number + second_backwards_number)
