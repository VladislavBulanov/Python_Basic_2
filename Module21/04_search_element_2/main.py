def find_key(dictionary, source_key, depth=-1):
    """
    Recursive search in nested dictionaries.
    If depth=-1 - search at all levels of source dictionary.

    :returns: list of value(s) by source key or empty list
    if source key is not in source dictionary
    :rtype: list
    """

    if depth == -1:
        result = []
        for key in dictionary.keys():
            if key == source_key:
                result += [dictionary[key]]
            if type(dictionary[key]) is dict:
                result += find_key(dictionary[key], source_key)
        return result
    else:
        if depth == 0:
            return []
        else:
            result = []
            for key in dictionary.keys():
                if key == source_key:
                    result += [dictionary[key]]
                if type(dictionary[key]) is dict:
                    result += find_key(dictionary[key], source_key, depth - 1)
            return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

origin_key = input('Введите искомый ключ: ')
depth_choice = input('Хотите ввести максимальную глубину? Y/N: ').lower()

if depth_choice == 'y':
    maximum_depth = int(input('Введите максимальную глубину: '))
    result_value = find_key(site, origin_key, maximum_depth)
else:
    result_value = find_key(site, origin_key)

print('\nЗначение ключа:', end=' ')
if result_value:
    print(*result_value)
else:
    print(None)
