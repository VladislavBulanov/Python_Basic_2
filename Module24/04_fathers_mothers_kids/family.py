class Parent:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.children_list = []


    def show_parent_information(self):
        print('\nИНФОРМАЦИЯ О РОДИТЕЛЕ:\nИмя: {}\nВозраст: {}'
              '\nСписок детей: '.format(
            self.name,
            self.age
        ), end='')
        if self.children_list:
            for child in self.children_list:
                print(child.name, end=' ')
            print()
        else:
            print('нет детей')


    def add_child(self, *children):
        for child in children:
            self.children_list.append(child)


    def calm_down_child(self, child):
        if child in self.children_list:
            child.is_calm = True
        else:
            print('\nУ этого родителя нет такого ребёнка.')


    def feed_child(self, child):
        if child in self.children_list:
            child.is_hungry = False
        else:
            print('\nУ этого родителя нет такого ребёнка.')


class Child:

    def __init__(self, name: str, age: int, is_calm=False, is_hungry=True):
        self.name = name
        self.age = age
        self.is_calm = is_calm
        self.is_hungry = is_hungry


    def show_child_information(self):
        print('\nИНФОРМАЦИЯ О РЕБЁНКЕ:\nИмя: {}\nВозраст: {}'
              '\nСостояние спокойствия: {}\nСостояние голода: {}'.format(
                    self.name,
                    self.age,
                    'спокоен' if self.is_calm else 'плачет',
                    'голоден' if self.is_hungry else 'не голоден'
        ))
