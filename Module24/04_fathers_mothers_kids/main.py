from family import Parent, Child


def create_parent():
    parent_name = input('\nВведите имя родителя: ')
    parent_age = int(input('Введите возраст родителя: '))
    return Parent(parent_name, parent_age)


def create_child():
    child_name = input('\nВведите имя ребёнка: ')
    child_age = int(input('Введите возраст ребёнка: '))
    return Child(child_name, child_age)


def main():
    # Tests:
    # parent = create_parent()
    # parent.show_parent_information()
    #
    # child_1 = create_child()
    # child_1.show_child_information()
    # child_2 = create_child()
    # child_2.show_child_information()
    #
    # parent.add_child(child_1, child_2)
    # parent.show_parent_information()
    #
    # parent.calm_down_child(child_1)
    # parent.feed_child(child_2)
    # child_1.show_child_information()
    # child_2.show_child_information()
    pass


if __name__ == '__main__':
    main()
