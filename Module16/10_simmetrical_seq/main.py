def create_list_of_numbers(numbers, quantity):
    for _ in range(quantity):
        numbers.append(int(input('Введите число: ')))


def is_symmetrical(source_list):
    reverse_list = []
    for element in source_list:
        reverse_list.insert(0, element)

    if reverse_list == source_list:
        return True
    else:
        return False


numbers_list = []
side_numbers_list = []
final_numbers_list = []
numbers_quantity = int(input('Введите количество чисел: '))

create_list_of_numbers(numbers_list, numbers_quantity)
print('\nИсходная последовательность:', numbers_list)

# Берём, по сути, срез (срезы в курсе не проходили, поэтому используем
# вспомогательный список) и проверяем, является ли он симметричным.
# Если да, то с помощью ещё одного списка отображаем часть, что мы
# "откинули" и "переворачиваем" её. Если нет, то идём дальше по списку:
for number in range(len(numbers_list)):
    for current_number in range(number, len(numbers_list)):
        side_numbers_list.append(numbers_list[current_number])

    if is_symmetrical(side_numbers_list):
        for index in range(number):
            final_numbers_list.append(numbers_list[index])
        final_numbers_list.reverse()

        # Если список, который нужно добавить, чтобы последовательность
        # стала симметричной, пуст, значит, эта последовательность
        # изначально симметрична:
        if not final_numbers_list:
            print('Приписывать числа не нужно, последовательность симметрична.')
        else:
            print(f'Нужно приписать чисел: {len(final_numbers_list)}')
            print('Сами числа:', final_numbers_list)
        break

    side_numbers_list.clear()
