def print_numbers(number):
    if number == 1:
        print(number)
        return number
    else:
        result = print_numbers(number - 1) + 1
        print(result)
        return result


print_numbers(int(input('Введите число: ')))
