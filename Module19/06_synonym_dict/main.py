def generate_synonyms_dictionary(quantity):
    result_dictionary = dict()

    for index in range(quantity):
        pair = input(f'Введите {index + 1}-ю пару через дефис: ').lower()
        current_key, current_value = pair.split('-')
        result_dictionary[current_key] = current_value

    return result_dictionary


def find_synonym(current_word, source_dictionary):
    for key, value in source_dictionary.items():
        if current_word == key:
            return value
        elif current_word == value:
            return key
    else:
        return False


pairs_quantity = int(input('Введите количество пар слов: '))
synonyms_dictionary = generate_synonyms_dictionary(pairs_quantity)

while True:
    word = input('\nВведите слово: ').lower()
    found_synonym = find_synonym(word, synonyms_dictionary)

    if found_synonym:
        print('Синоним:', found_synonym)
        break
    else:
        print('Такого слова в словаре нет. Пожалуйста, повторите ввод.')
