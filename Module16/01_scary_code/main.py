def extend_list(input_list, additional_list):
    output_list = [element for element in input_list]
    output_list.extend(additional_list)
    return output_list


def count_digit(initial_list, number):
    return initial_list.count(number)


def delete_digit(source_list, digit):
    result_list = [element for element in source_list]

    for _ in range(result_list.count(digit)):
        result_list.remove(digit)

    return result_list


prime_list = [1, 5, 3]
side_list_1 = [1, 5, 1, 5]
side_list_2 = [1, 3, 1, 5, 3, 3]

prime_list = extend_list(prime_list, side_list_1)
print(f'Количество цифр 5 при первом объединении: {count_digit(prime_list, 5)}')
prime_list = delete_digit(prime_list, 5)

prime_list = extend_list(prime_list, side_list_2)
print(f'Количество цифр 3 при втором объединении: {count_digit(prime_list, 3)}')

print('Итоговый список:', prime_list)
