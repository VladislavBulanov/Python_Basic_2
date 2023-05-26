import os
import zipfile

def unzip_archive(source_archive_path, unzip_archive_path):
    zip_file = zipfile.ZipFile(source_archive_path, 'r')
    zip_file.extractall(unzip_archive_path)


def get_letters_stats(source_text_path):
    source_file = open(source_text_path, 'r', encoding='utf-8')
    result_stats = dict()

    for line in source_file:
        for symbol in line:
            if symbol.isalpha():
                current_value = result_stats.get(symbol, 0)
                result_stats[symbol] = current_value + 1

    sorted_result_stats = sort_dictionary_by_value(result_stats)
    source_file.close()
    return sorted_result_stats


def sort_dictionary_by_value(dictionary):
    data_list = [[key, value] for key, value in dictionary.items()]

    for i_index in range(len(data_list)):
        for j_index in range(i_index, len(data_list)):
            if data_list[j_index][1] > data_list[i_index][1]:
                data_list[j_index], data_list[i_index] = \
                data_list[i_index], data_list[j_index]

    return {element[0]: element[1] for element in data_list}


def write_data_in_file(initial_data, result_file_path):
    result_file = open(result_file_path, 'a', encoding='utf-8')

    result_file.write('Частота букв в тексте (буква - количество):\n\n')
    for key, value in initial_data.items():
        result_file.write('{} - {:3,d}\n'.format(
            key,
            value
        ))
    result_file.close()


path_to_archive = os.path.abspath('voyna-i-mir.zip')
path_to_unzip_archive = os.path.abspath('unzip_file')
unzip_archive(path_to_archive, path_to_unzip_archive)

path_to_text = f'{path_to_unzip_archive}\\{os.listdir(path_to_unzip_archive)[0]}'
letters_stats = get_letters_stats(path_to_text)
write_data_in_file(letters_stats, os.path.abspath('letters_statistics.txt'))
