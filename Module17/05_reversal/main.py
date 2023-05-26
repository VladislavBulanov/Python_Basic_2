def reverse_string(source_string):
    return source_string[::-1]


input_string = input('Введите строку: ')

first_index = input_string.index('h')
# Обратная индексация начинается с -1:
last_index = -(reverse_string(input_string).index('h') + 1)

slice_between_letters = input_string[(first_index + 1):last_index]
if slice_between_letters:
    print('Развёрнутая последовательность между первым и последним h:', end=' ')
    print(reverse_string(slice_between_letters))
else:
    print('Между первым и последним h в строке нет символов.')
