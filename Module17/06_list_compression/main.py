import random

def generate_numbers(quantity):
    return [random.randint(0, 2) for _ in range(quantity)]


def delete_number(source_list, chosen_number):
    result_list = [number for number in source_list if number != chosen_number]
    return result_list


numbers_quantity = int(input('Введите количество чисел в списке: '))
numbers_list = generate_numbers(numbers_quantity)
print('Список до сжатия:', numbers_list)
print('Список после сжатия:', delete_number(numbers_list, 0))
