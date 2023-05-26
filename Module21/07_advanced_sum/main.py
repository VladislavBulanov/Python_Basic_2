def custom_sum(*terms):
    return sum(unfold(terms))


def unfold(source_object):
    result = []
    for element in source_object:
        if isinstance(element, (int, float)):
            result.append(element)
        else:
            result.extend(unfold(element))
    return result


# print(custom_sum([1, 2, [[3]]], [[1], 3]))
# print(custom_sum(1, 2, 3, 4, 5))
# print(custom_sum(1.1, 2.2, 3.3))
