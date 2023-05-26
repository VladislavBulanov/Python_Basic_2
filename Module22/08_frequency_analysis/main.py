import os

def get_texts_statistics(datafile_path):
    source_file = open(datafile_path, 'r')
    source_text = source_file.read()

    letters_in_text = get_list_of_letters_from_text(source_text)  # List
    letters_amount = get_quantity_of_each_element(letters_in_text)  # Dict
    letters_ratio = get_elements_ratio(letters_amount, len(letters_in_text))  # Dict
    letters_stats = sort_dictionary_by_value(letters_ratio)  # Dict

    source_file.close()
    return letters_stats


def get_list_of_letters_from_text(origin_text):
    return sorted([
        symbol.lower()
        for symbol in origin_text
        if symbol.isalpha()
    ])


def get_quantity_of_each_element(initial_list):
    result_dictionary = dict()
    for element in initial_list:
        if element in result_dictionary:
            result_dictionary[element] += 1
        else:
            result_dictionary[element] = 1
    return result_dictionary


def get_elements_ratio(initial_dictionary, total_quantity):
    result_dictionary = {
        key: value for key, value in initial_dictionary.items()
    }
    return {
        key: round(value / total_quantity, 3)
        for key, value in result_dictionary.items()
    }


def sort_dictionary_by_value(dictionary):
    data_list = [[key, value] for key, value in dictionary.items()]

    for i_index in range(len(data_list)):
        for j_index in range(i_index, len(data_list)):
            if data_list[j_index][1] > data_list[i_index][1]:
                data_list[j_index], data_list[i_index] = \
                data_list[i_index], data_list[j_index]

    return {element[0]: element[1] for element in data_list}


def write_data_to_file(data, result_file_path):
    result_file = open(result_file_path, 'a')
    for key, value in data.items():
        result_file.write(f'{key} {value}\n')
    result_file.close()


path_to_datafile = os.path.abspath('text.txt')
path_to_result_file = os.path.abspath('analysis.txt')
texts_statistics = get_texts_statistics(path_to_datafile)
write_data_to_file(texts_statistics, path_to_result_file)
