def find_longest_word(words_list):
    max_length_word = words_list[0]

    for word in words_list:
        if len(word) > len(max_length_word):
            max_length_word = word

    return max_length_word


input_text = input('Введите строку: ').split()
longest_word = find_longest_word(input_text)
length = len(longest_word)

print('Самое длинное слово: {0}\nДлина этого слова: {1}'.format(
    longest_word,
    length
))
