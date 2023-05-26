def encrypt_message(message, offset):
    """
    :param message: source message for encrypt
    :type message: str
    :param offset: the value of shift
    :type offset: int
    :returns: encrypted message
    :rtype: List[str]
    """

    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result_message = [russian_alphabet[(russian_alphabet.index(symbol) + offset) %
                      len(russian_alphabet)]
                      if symbol in russian_alphabet else symbol
                      for symbol in message]
    return result_message


input_message = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

encrypted_message = encrypt_message(input_message, shift)
print('Зашифрованное сообщение:', "".join(encrypted_message))
