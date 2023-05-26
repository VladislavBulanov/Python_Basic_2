def sort_list(source_list):
    length = len(source_list)

    for start_element in range(length):
        for current_element in range(start_element, length):
            if source_list[current_element] < source_list[start_element]:
                source_list[current_element], source_list[start_element] = (source_list[start_element],
                                                                            source_list[current_element])


group_one = list(range(160, 177, 2))
group_two = list(range(162, 181, 3))

group_one.extend(group_two)
sort_list(group_one)

print('Отсортированный список учеников:', group_one)
