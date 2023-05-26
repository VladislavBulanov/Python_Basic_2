def count_frequency(text):
    dictionary = dict()

    for symbols in text:
        if symbols in dictionary:
            dictionary[symbols] += 1
        else:
            dictionary[symbols] = 1

    return dictionary


def invert_dictionary(source_dictionary):
    inverted_dictionary = dict()

    for current_key, current_value in source_dictionary.items():
        if current_value in inverted_dictionary:
            inverted_dictionary[current_value].append(current_key)
        else:
            inverted_dictionary[current_value] = [current_key]

    return inverted_dictionary


source_text = input('Введите текст: ')
symbols_frequency = count_frequency(source_text)
inverted_symbols_frequency = invert_dictionary(symbols_frequency)

print('\nОригинальный словарь частот:')
for key, value in symbols_frequency.items():
    print(f'{key} : {value}')

print('\nИнвертированный словарь частот:')
for key, value in inverted_symbols_frequency.items():
    print(f'{key} : {value}')
