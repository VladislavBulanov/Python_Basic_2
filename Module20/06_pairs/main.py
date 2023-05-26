import random

def generate_numbers_list(numbers_quantity):
    return [random.randint(0, 9) for _ in range(numbers_quantity)]


# Вариант №1:
def get_list_of_pairs(source_list):
    return list(zip(source_list[::2], source_list[1::2]))


# Вариант №2:
# def get_list_of_pairs(source_list):
#     return [(number, source_list[index + 1])
#             for index, number in enumerate(source_list)
#             if index % 2 == 0]


numbers_list = generate_numbers_list(10)
list_of_pairs = get_list_of_pairs(numbers_list)

print('Оригинальный список:', numbers_list)
print('Новый список:', list_of_pairs)
