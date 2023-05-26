from typing import List
from functools import reduce


if __name__ == '__main__':
    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

    new_list_1 = list(map(lambda number: round(number ** 3, 3), floats))
    print(new_list_1)

    new_list_2 = list(filter(lambda name: len(name) >= 5, names))
    print(new_list_2)

    # По ТЗ требуется список, хотя в результате получается число:
    new_list_3 = [reduce(lambda num_1, num_2: num_1 * num_2, numbers)]
    print(new_list_3)
