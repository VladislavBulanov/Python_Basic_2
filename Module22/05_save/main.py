import os

def get_path():
    while True:
        inputted_path = input('\nВведите путь, куда желаете сохранить '
                              'документ:\n(введите последовательность '
                              'папок через пробел)\n').replace(' ', '\\')
        result_path = os.path.abspath(os.path.sep) + inputted_path

        if os.path.exists(result_path):
            return result_path
        else:
            print('Такого пути не существует. Пожалуйста, повторите ввод.')


def write_text_in_file(source_text, source_path):
    filename = input('\nВведите название файла: ')
    path_to_file = f'{source_path}\\{filename}.txt'

    if os.path.exists(path_to_file):
        user_choice = input('Вы действительно хотите перезаписать '
                            'файл? (да/нет): ').lower()
        if user_choice == 'да':
            file = open(path_to_file, 'w')
            file.write(source_text)
            file.close()
            print('Файл успешно перезаписан!')
    else:
        file = open(path_to_file, 'w')
        file.write(source_text)
        file.close()
        print('Файл успешно сохранён!')


text = input('Введите строку: ')
path = get_path()
write_text_in_file(text, path)
