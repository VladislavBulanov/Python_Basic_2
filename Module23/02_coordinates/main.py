import os
import random
import copy

def get_results_data(source_file_path):
    result_data = []
    current_values = []

    try:
        with open(source_file_path, 'r') as source_file:
            for line in source_file:
                line = line.strip('\n').split()
                x = float(line[0])
                y = float(line[1])

                try:
                    function_result = function_1(x, y)
                    current_values.append(function_result)

                    try:
                        function_result = function_2(x, y)
                        current_values.append(function_result)
                    except ZeroDivisionError:
                        print('Ошибка второй функции: на ноль делить нельзя.')

                except ZeroDivisionError:
                    print('Ошибка первой функции: на ноль делить нельзя.')

                random_number = random.randint(0, 100)
                current_values.append(random_number)

                result_data.append(copy.copy(current_values))
                current_values.clear()

        return result_data

    except FileNotFoundError:
        print('Неверно указан путь к исходному файлу.')


def write_data_to_file(result_file_path, source_data):
    with open(result_file_path, 'a', encoding='utf-8') as result_file:
        for element in source_data:
            if len(element) == 3:
                result_string = [
                    str(number) for number in sorted(element)
                ]
                result_file.write(', '.join(result_string) + '\n')
            else:
                result_file.write('Ошибка функции: деление на ноль.\n')


def function_1(initial_x, initial_y):
    initial_x += random.randint(0, 10)
    initial_y += random.randint(0, 5)
    return initial_x / initial_y


def function_2(initial_x, initial_y):
    initial_x -= random.randint(0, 10)
    initial_y -= random.randint(0, 5)
    return initial_y / initial_x


path_to_source_file = os.path.abspath('coordinates.txt')
path_to_result_file = os.path.abspath('result.txt')
data = get_results_data(path_to_source_file)
write_data_to_file(path_to_result_file, data)
