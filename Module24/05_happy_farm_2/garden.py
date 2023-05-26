class Potato:

    states = {
        0: 'отсутствует',
        1: 'росток',
        2: 'зелёная',
        3: 'зрелая'
    }


    def __init__(self, index):
        self.index = index
        self.state = 0


    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_potato_state()


    def is_ripe(self):
        if self.state == 3:
            return True
        return False


    def print_potato_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index,
            Potato.states[self.state]
        ))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index + 1) for index in range(count)]


    def grow_all(self):
        print('Картошка прорастает!')
        for potato in self.potatoes:
            potato.grow()


    def are_all_ripe(self):
        if all([potato.state == 3 for potato in self.potatoes]):
            return True
        return False


    def print_potatoes_state(self):
        for potato in self.potatoes:
            potato.print_potato_state()


class Gardener:

    collected_harvest = []

    def __init__(self, name, potato_garden):
        self.name = name
        self.potato_garden = potato_garden


    def take_care(self):
        if self.potato_garden.are_all_ripe():
            print('\nВся картошка созрела, можно собирать урожай!')
        else:
            print('\nСадовник ухаживает за грядкой...')
            self.potato_garden.grow_all()


    def collect_harvest(self):
        if self.potato_garden.are_all_ripe():
            for potato in self.potato_garden.potatoes:
                potato.state = 0
            self.collected_harvest.append(len(self.potato_garden.potatoes))
            print('УРОЖАЙ СОБРАН!')
        else:
            print('Картошка ещё не созрела, необходимо за ней поухаживать.')


    def show_collected_harvest(self):
        if not self.collected_harvest:
            print('Садовник пока не собрал ни одного урожая.')
        else:
            for index, harvest in enumerate(self.collected_harvest):
                print('{}-й урожай: {} ед. картофеля'.format(
                    index + 1,
                    harvest
                ))
