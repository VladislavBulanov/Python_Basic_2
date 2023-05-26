def custom_zip(*objects):
    # Создаём список итераторов:
    list_of_iterators = [iter(element) for element in objects]
    return [tuple(map(next, list_of_iterators)) for _ in range(find_shortest_length(objects))]


def find_shortest_length(initial_objects):
    lengths = []
    for current_element in initial_objects:
        lengths.append(len(current_element))
    return min(lengths)


# a = [{"x": 4}, "b", "z", "d"]
# b = (10, {20}, [30], "z")
# print(custom_zip(a, b))

# a = [1, 2, 3, 4, 5]
# b = {1: "s", 2: "q", 3: 4}
# x = (1, 2, 3, 4, 5)
# print(custom_zip(a, b, x))
