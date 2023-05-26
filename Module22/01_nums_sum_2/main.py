import os

def find_sum_of_numbers(source_path, result_file_name='answer.txt'):
    source_file = open(source_path, 'r')
    result_file = open(result_file_name, 'w')

    numbers_list = []

    for line in source_file:
        numbers = [
            int(number) for number in line.strip('\n').split()
            if number.isdigit()
        ]
        numbers_list.extend(numbers)

    sum_of_numbers = sum(numbers_list)
    result_file.write(str(sum_of_numbers))

    source_file.close()
    result_file.close()


path = os.path.abspath('numbers.txt')
find_sum_of_numbers(path)
