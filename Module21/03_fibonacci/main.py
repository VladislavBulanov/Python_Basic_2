def get_fibonacci_number(number):
    if number <= 1:
        return number
    else:
        return (get_fibonacci_number(number - 1) +
               get_fibonacci_number(number - 2))


position = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(get_fibonacci_number(position))
