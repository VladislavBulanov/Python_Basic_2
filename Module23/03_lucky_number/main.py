import random

def get_input(input_message):
    while True:
        try:
            return int(input(input_message))
        except ValueError:
            print('Некорректный ввод, попробуйте ещё раз.\n')

def write_number_to_file(source_number, source_file):
    source_file.write(str(source_number) + '\n')

def main():
    with open('out_file.txt', 'w') as file:
        total_sum = 0
        while total_sum < 777:
            try:
                number = get_input('Введите число: ')
                total_sum += number
                if random.randint(1, 13) == 1:
                    raise Exception('Вас постигла неудача!')
                write_number_to_file(number, file)

            except Exception as error:
                print(error)
                break

        if total_sum >= 777:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')

if __name__ == '__main__':
    main()
