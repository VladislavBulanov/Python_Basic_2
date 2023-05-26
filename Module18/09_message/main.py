def encrypt_message(source_message):
    """
    :param source_message: inputted text to encrypt
    :type source_message: str
    :returns: encrypted message
    :rtype: str
    """

    current_encrypted_word = ''
    encrypted_list = []

    for symbol in source_message:
        if symbol.isalpha():
            current_encrypted_word = symbol + current_encrypted_word
        else:
            encrypted_list.append(current_encrypted_word)
            current_encrypted_word = ''
            encrypted_list.append(symbol)

    return "".join(encrypted_list)


input_message = input('Введите сообщение: ')
encrypted_message = encrypt_message(input_message)
print('Новое сообщение:', encrypted_message)
