import os

def get_letters_count(source_path):
    if os.path.exists(source_path):
        data_file = open(source_path, 'r')
        letters_quantity = 0

        for line in data_file:
            for symbol in line:
                if symbol.isalpha():
                    letters_quantity += 1

        data_file.close()
        return letters_quantity


def get_words_count(source_path):
    if os.path.exists(source_path):
        data_file = open(source_path, 'r')
        text = data_file.read().replace('\n', ' ')

        words_string = ''
        for symbol in text:
            if symbol.isalpha() or symbol in ("'", " "):
                words_string += symbol

        words_list = words_string.split()
        data_file.close()
        return len(words_list)


def get_strings_count(source_path):
    if os.path.exists(source_path):
        data_file = open(source_path, 'r')
        text = data_file.read()
        data_file.close()
        return text.count('\n') + 1


def get_rarest_letter(source_path):
    if os.path.exists(source_path):
        data_file = open(source_path, 'r')
        text = data_file.read().lower()

        letters_dictionary = dict()
        for symbol in text:
            if symbol.isalpha():
                if symbol in letters_dictionary:
                    letters_dictionary[symbol] += 1
                else:
                    letters_dictionary[symbol] = 1

        sorted_letters_dictionary = sort_dictionary_by_value(letters_dictionary)
        rarest_letter = list(sorted_letters_dictionary.keys())[0]
        data_file.close()
        return rarest_letter


def sort_dictionary_by_value(dictionary):
    inverted_dictionary = {value: key for key, value in dictionary.items()}
    keys_list = list(inverted_dictionary.keys())
    sorted_dictionary = {
        inverted_dictionary[key]: key for key in sorted(keys_list)
    }
    return sorted_dictionary


path = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
print('Количество букв в файле:', get_letters_count(path))
print('Количество слов в файле:', get_words_count(path))
print('Количество строк в файле:', get_strings_count(path))
print('Наиболее редкая буква:', get_rarest_letter(path))
