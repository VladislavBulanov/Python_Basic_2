def sort_tuple(initial_tuple):
    for number in initial_tuple:
        if not isinstance(number, int):
            return initial_tuple
    else:
        return tuple(sorted(list(initial_tuple)))


source_tuple = (6, 3, -1, 8, 4, 10, -5)
print(sort_tuple(source_tuple))
