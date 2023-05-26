def generate_pedigree(members_quantity):
    result_pedigree = dict()

    for index in range(members_quantity - 1):
        child, parent = input(f'{index + 1}-я пара: ').split()
        result_pedigree[child] = parent

    return result_pedigree


def get_depth_information(source_pedigree):
    result_depth = dict()

    for child, parent in source_pedigree.items():
        result_depth[child], result_depth[parent] = 0, 0

    for human in source_pedigree:
        current_human = human
        # Если человек есть в родословной в качестве
        # потомка (ключа словаря), мы берём его родителя и
        # рассматриваем уже его в качестве потомка:
        while current_human in source_pedigree:
            current_human = source_pedigree[current_human]
            result_depth[human] += 1

    return result_depth


humans_quantity = int(input('Введите количество человек: '))
pedigree = generate_pedigree(humans_quantity)
depth = get_depth_information(pedigree)

print('\n"Высота" каждого члена семьи:')
for man in sorted(depth):
    print(man, depth[man])
