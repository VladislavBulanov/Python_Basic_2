def unfold(origin_list):
    result = []
    for element in origin_list:
        if isinstance(element, (int, float, str)):
            result.append(element)
        else:
            result.extend(unfold(element))
    return result


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
print('Ответ: ', unfold(nice_list))
