def fill_list(elements_quantity):
    result_list = []

    for index in range(elements_quantity):
        input_number = int(input(f'Введите {index + 1}-е число: '))
        result_list.append(input_number)

    return result_list


print('ПЕРВЫЙ СПИСОК')
first_list = fill_list(3)
print('\nВТОРОЙ СПИСОК')
second_list = fill_list(7)
print('\nПервый список:', first_list)
print('Второй список:', second_list)

first_list.extend(second_list)

# Идём по объединённому списку, берём каждое число, проверяем, сколько
# раз оно встречается в списке, и удаляем N-1 раз:
for number in first_list:
    total_number_appears = first_list.count(number)
    for time in range(total_number_appears - 1):
        first_list.remove(number)

print('\nНовый первый список с уникальными элементами:', first_list)
