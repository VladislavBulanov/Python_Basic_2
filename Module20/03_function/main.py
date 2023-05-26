def slicer(source_tuple, source_element):
    if quantity := source_tuple.count(source_element):
        list_of_indexes = [index for index, element in enumerate(source_tuple)
                           if element == source_element]

        if quantity == 1:
            return source_tuple[list_of_indexes[0]:]
        else:
            return source_tuple[list_of_indexes[0]:list_of_indexes[1] + 1]

    else:
        return ()


# initial_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
# inputted_element = int(input('Введите целое число: '))
# print(slicer(initial_tuple, inputted_element))
