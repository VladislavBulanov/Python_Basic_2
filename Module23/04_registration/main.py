import os

def check_database(database, good_log, bad_log):
    try:
        with open(database, 'r', encoding='utf-8') as data_file, \
             open(good_log, 'w', encoding='utf-8') as good_log_file, \
             open(bad_log, 'w', encoding='utf-8') as bad_log_file:
                for line in data_file:
                    current_line = line.strip().split()

                    try:
                        validate_data(current_line)
                        good_log_file.write(f'{" ".join(current_line)}\n')
                    except (IndexError, NameError, SyntaxError, ValueError) as error:
                        bad_log_file.write(f'{" ".join(current_line)}\t\t{error}\n')

    except FileNotFoundError:
        print('Неверно указан путь к искомому файлу.')


def validate_data(initial_list):
    if len(initial_list) != 3:
        raise IndexError('Не присутствуют все три поля.')

    if not initial_list[0].isalpha():
        raise NameError('Поле "Имя" содержит не только буквы.')

    if '@' not in initial_list[1] or '.' not in initial_list[1]:
        raise  SyntaxError('Поле "Имейл" не содержит @ и . (точку).')

    if not (10 <= int(initial_list[2]) <= 99):
        raise ValueError('Поле "Возраст" не является числом от 10 до 99.')


source_data = os.path.abspath('registrations.txt')
good_registrations_log_file = os.path.abspath('registrations_good.log')
bad_registrations_log_file = os.path.abspath('registrations_bad.log')
check_database(source_data, good_registrations_log_file, bad_registrations_log_file)
