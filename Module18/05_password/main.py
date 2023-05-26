def check_length(initial_string, limit_length):
    length = len(initial_string)
    return True if length >= limit_length else False


def check_register(input_string):
    return False if input_string.islower() else True


def count_digits(source_string, required_count):
    count = 0

    for symbol in source_string:
        if symbol.isdigit():
            count += 1

    return True if count >= required_count else False


while True:
    password = input('Придумайте пароль: ')
    error_message = 'Пароль ненадёжный. Попробуйте ещё раз.\n'

    if not check_length(password, 8):
        print(error_message)
    elif not check_register(password):
        print(error_message)
    elif not count_digits(password, 3):
        print(error_message)
    else:
        print('Это надёжный пароль!')
        break
