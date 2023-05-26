import os

def get_symbols_sum(file_path, log_file_path):
    symbols_sum = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as source_file:
            line_number = 1
            for line in source_file:
                line = line.strip('\n')
                symbols_sum += len(line)

                try:
                    if len(line) < 3:
                        raise ValueError(f'Ошибка: менее трех символов в строке {line_number}')
                except ValueError as error:
                    print(error)
                    write_error_to_log_file(error, log_file_path)

                line_number += 1

        print(f'Общее количество символов: {symbols_sum}')

    except FileNotFoundError:
        print('Неверно указан путь к исходному файлу.')


def write_error_to_log_file(origin_error, path):
    with open(path, 'a', encoding='utf-8') as log_file:
        log_file.write(f'{origin_error}\n')


path_to_source_file = os.path.abspath('people.txt')
path_to_log_file = os.path.abspath('errors.log')
get_symbols_sum(path_to_source_file, path_to_log_file)
