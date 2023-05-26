from life import Human, House
from random import randint


def do_action(character):
    action_points = randint(1, 6)
    if character.satiety < 20:
        character.eat(action_points)
    elif character.house.food < 10:
        character.go_to_store(action_points)
    elif character.house.money < 50:
        character.go_work(action_points)
    elif action_points == 1:
        character.go_work(action_points)
    elif action_points == 2:
        character.eat(action_points)
    else:
        character.play(action_points)


def start_life(man_1, man_2):
    for day in range(1, 366):
        if (man_1.satiety >= 0) and (man_2.satiety >= 0):
            print('\nДЕНЬ {}'.format(day))
            do_action(man_1)
            do_action(man_2)
        elif man_1.satiety < 0:
            print('\n{} умер с голода...'.format(man_1.name))
        elif man_2.satiety < 0:
            print('\n{} умер с голода...'.format(man_2.name))
    else:
        print('\n{} И {} СМОГЛИ ПРОЖИТЬ ВМЕСТЕ ЦЕЛЫЙ ГОД!'.format(
            man_1.name.upper(),
            man_2.name.upper()
        ))


def main():
    print('======= СИМУЛЯТОР СОВМЕСТНОГО ПРОЖИВАНИЯ =======\n')
    house = House()
    human_1 = Human(input('Введите имя первого человека: '), house)
    human_2 = Human(input('Введите имя второго человека: '), house)
    start_life(human_1, human_2)


if __name__ == '__main__':
    main()
