def compress_string(source_string):
    encrypted_list = []
    current_letter = source_string[0]
    count = 1

    for index in range(1, len(source_string)):
        if source_string[index] == current_letter:
            count += 1
        else:
            encrypted_list.append(current_letter)
            encrypted_list.append(str(count))
            current_letter = source_string[index]
            count = 1

    encrypted_list.append(current_letter)
    encrypted_list.append(str(count))
    return ''.join(encrypted_list)


input_string = input('Введите строку: ')
compressed_string = compress_string(input_string)
print('\nЗакодированная строка:', compressed_string)
