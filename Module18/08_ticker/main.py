def compare_strings(string_1, string_2):
    is_same = False

    for assumed_shift in range(len(string_1)):
        if string_2[assumed_shift:] + string_2[:assumed_shift] == string_1:
            is_same = True
            break

    return is_same


first_string = input('Введите первую строку: ')
second_string = input('Введите вторую строку: ')
is_same_strings = compare_strings(first_string, second_string)

if is_same_strings:
    shift = second_string.index(first_string[0])
    print(f'\nПервая строка получается из второй со сдвигом {shift}.')
else:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
