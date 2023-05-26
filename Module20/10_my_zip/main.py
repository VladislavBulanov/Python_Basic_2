def custom_zip(object_1, object_2):
    if (not isinstance(object_1, (dict, set))) and (not isinstance(object_2, (dict, set))):
        return ((object_1[index], object_2[index])
                for index in range(find_shortest_length(object_1, object_2)))
    else:
        if isinstance(object_1, dict):
            new_object_1 = [element for element in object_1.keys()]
        elif isinstance(object_1, set):
            new_object_1 = list(object_1)
        else:
            new_object_1 = [element for element in object_1]

        if isinstance(object_2, dict):
            new_object_2 = [element for element in object_2.keys()]
        elif isinstance(object_2, set):
            new_object_2 = list(object_2)
        else:
            new_object_2 = [element for element in object_2]

        return ((new_object_1[index], new_object_2[index])
                for index in range(find_shortest_length(new_object_1, new_object_2)))


def find_shortest_length(source_object_1, source_object_2):
    return min(len(source_object_1), len(source_object_2))


initial_object_1 = 'abcd'
initial_object_2 = (10, 20, 30, 40)

result_zip = custom_zip(initial_object_1, initial_object_2)
print('Результат:\n', result_zip, sep='')
for part in result_zip:
    print(part)
