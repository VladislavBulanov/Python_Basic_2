import os

def run_text_calculator(data_file_path):
    total_sum = 0
    try:
        with open(data_file_path, 'r') as data_file:
            for line in data_file:
                current_line = line.strip().split()

                try:
                    validate_data(current_line)
                    total_sum += calculate_expression(current_line[0],
                                                      current_line[1],
                                                      current_line[2])
                except (SyntaxError, ValueError, ZeroDivisionError) as error:
                    print(f'\nОбнаружена следующая ошибка в строке <{" ".join(current_line)}>:')
                    print(error)
                    changed_line = change_line()
                    if changed_line:
                        total_sum += calculate_expression(changed_line[0],
                                                          changed_line[1],
                                                          changed_line[2])

        print('\nСумма результатов:', total_sum)

    except FileNotFoundError:
        print('Неверно указан путь к исходному файлу.')


def validate_data(data_list: list):
    """
    :param data_list: expected list: [number_1, operation, number_2]
    :return: None, if errors have not been raised
    :raises SyntaxError, ValueError, ZeroDivisionError
    """
    if len(data_list) != 3:
        raise SyntaxError('\tне соблюдена схема <ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2>')
    if data_list[1] not in ('+', '-', '*', '/', '//', '%', '**'):
        raise SyntaxError(f'\tнекорректная операция: {data_list[1]}')
    if (not data_list[0].isdigit()) or (not data_list[2].isdigit()):
        raise ValueError('\tоперанд не является целым числом')
    if (data_list[1] in ('/', '//', '%')) and (int(data_list[2]) == 0):
        raise ZeroDivisionError('\tделение на ноль запрещено')


def calculate_expression(number_1, operation, number_2):
    """
    :type number_1: str
    :type operation: str
    :type number_2: str
    :rtype int or float
    :raise: ZeroDivisionError
    """
    if operation == '+':
        return int(number_1) + int(number_2)
    elif operation == '-':
        return int(number_1) - int(number_2)
    elif operation == '*':
        return int(number_1) * int(number_2)
    elif operation == '/':
        return int(number_1) / int(number_2)
    elif operation == '//':
        return int(number_1) // int(number_2)
    elif operation == '%':
        return int(number_1) % int(number_2)
    elif operation == '**':
        return int(number_1) ** int(number_2)


def change_line():
    """
    :return: None, if user doesn't want to change wrong line,
             and correct line, if he does.
    :rtype: list
    """
    user_choice = input('Хотите исправить ошибку? (Y/N): ').lower()
    if user_choice == 'n':
        return None
    elif user_choice == 'y':
        while True:
            right_line = input('\nВведите исправленную строку: ').strip().split()
            try:
                validate_data(right_line)
            except (SyntaxError, ValueError, ZeroDivisionError) as error:
                print(f'Некорректный ввод: {error}')
                print('Пожалуйста, повторите ввод.')
            else:
                return right_line


path_to_data_file = os.path.abspath('calc.txt')
run_text_calculator(path_to_data_file)
