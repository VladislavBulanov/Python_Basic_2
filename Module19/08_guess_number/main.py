import random

limit_number = int(input('Введите максимальное число: '))
guess_number = random.randint(1, limit_number)
potential_right_numbers = set()
wrong_numbers = set()

while (inputted_guess_numbers := input('\nНужное число '
       'есть среди этих чисел: ')) != 'Помогите!':

    numbers = {int(number) for number in inputted_guess_numbers.split()}
    for current_number in numbers:
        if current_number == guess_number:
            print('Ответ Артёма: Да')
            potential_right_numbers.update(numbers - wrong_numbers)
            break
    else:
        print('Ответ Артёма: Нет')
        potential_right_numbers.difference_update(numbers)
        wrong_numbers.update(numbers)

print('\nАртём мог загадать следующие числа:', *potential_right_numbers)
