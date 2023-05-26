# Задача 3. Сумма и разность


def sum_of_digits(number):
    string_number = str(number)
    amount = 0
    for digit in string_number:
        amount += int(digit)
    return amount


def count_digits(number):
    count = len(str(number))
    return count


while True:
    number = int(input('\nВведите целое положительное число: '))
    if number > 0:
        break
    else:
        print('Число должно быть больше нуля. Пожалуйста, повторите ввод.')

total_of_digits = sum_of_digits(number)
quantity_digits = count_digits(number)
difference = total_of_digits - quantity_digits

print('\nСумма чисел равна', total_of_digits)
print('Количество цифр в числе равно', quantity_digits)
print('Разность суммы и количества цифр равна', difference)
