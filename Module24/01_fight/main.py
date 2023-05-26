from random import randint


class Warrior:

    def __init__(self, health=100):
        self.health = health

    def loose_health(self, damage):
        if isinstance(self, Warrior):
            self.health -= damage
        else:
            print('Атакуемый объект не является воином.')


def start_fight(unit_1, unit_2):
    print('ДРАКА НАЧАЛАСЬ!')
    while unit_1.health > 0 and unit_2.health > 0:
        who_beats = randint(1, 2)
        print('\nБьёт воин №{}:'.format(who_beats))

        if who_beats == 1:
            unit_2.loose_health(20)
            print('У воина №2 осталось {} очков здоровья.'.format(unit_2.health))
        elif who_beats == 2:
            unit_1.loose_health(20)
            print('У воина №1 осталось {} очков здоровья.'.format(unit_1.health))

    if unit_1.health <= 0:
        print('\nПОБЕДУ ОДЕРЖАЛ ВОИН №2!')
    elif unit_2.health <= 0:
        print('\nПОБЕДУ ОДЕРЖАЛ ВОИН №1!')


warrior_1 = Warrior()
warrior_2 = Warrior()
start_fight(warrior_1, warrior_2)
