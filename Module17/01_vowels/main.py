def list_of_vowel_letters(source_text):
    """
    :param: inputted text from the console
    :returns: the list of russian vowel letters in this text
    """
    existing_vowel_letters = ['а', 'я', 'у', 'ю', 'ы', 'и', 'э', 'е', 'о', 'ё']
    result_list = [letter for letter in source_text
                    if letter in existing_vowel_letters]
    return result_list


text = input('Введите текст: ').lower()
vowel_letters = list_of_vowel_letters(text)
print('\nСписок гласных букв в данном тексте:', vowel_letters)
print('Длина списка:', len(vowel_letters))
