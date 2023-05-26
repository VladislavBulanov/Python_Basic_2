import os

def encrypt_text(source_text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    length = len(alphabet)

    result_text = ''
    for symbol in source_text:
        if symbol.lower() in alphabet:
            if symbol.islower():
                result_text += alphabet[(alphabet.index(symbol) + shift) % length]
            else:
                result_text += alphabet[(alphabet.index(symbol.lower()) +
                                         shift) % length].upper()
        else:
            result_text += symbol

    return result_text


def encrypt_file(source_path, result_file_name):
    source_file = open(source_path, 'r')
    result_file = open(os.path.abspath(result_file_name), 'a')
    current_shift = 1

    for line in source_file:
        result_file.write(encrypt_text(line, current_shift))
        current_shift += 1
    result_file.write('\n')

    source_file.close()
    result_file.close()


path = os.path.abspath('text.txt')
encrypt_file(path, 'cipher_text.txt')
