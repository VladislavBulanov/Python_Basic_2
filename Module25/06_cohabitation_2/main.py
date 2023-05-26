from classes import House, Husband, Wife, Cat
from random import randint


def start_life_simulator():
    """
    The simulating of cohabitation husband, wife and cat in one house
    within one year. Every member of family can make only one action
    per day. Every action is spelled out in classes' documentation.
    """
    house = House()
    husband = Husband('Артём')
    wife = Wife('Елена')
    cat = Cat('Барсик')

    for day in range(1, 366):
        print('\n======= ДЕНЬ {} ======='.format(day))
        house.set_dirt(house.get_dirt() + 5)
        if house.get_dirt() > 90:
            husband.set_happy(husband.get_happy() - 10)
            wife.set_happy(wife.get_happy() - 10)

        simulate_husband_day(husband, house)
        simulate_wife_day(wife, house)
        simulate_cat_day(cat, house)

        house.print_general_info()
        husband.print_general_info()
        wife.print_general_info()
        cat.print_general_info()

    print('\n========== ИТОГИ ГОДА ==========')
    print('Заработано денег: {}\nСъедено еды: {}\nКуплено шуб: {}'.format(
        husband.get_earned_money(),
        husband.get_eaten_food() + wife.get_eaten_food(),
        wife.get_fur_coat_amount()
    ))


def simulate_husband_day(husband, house):
    """Function simulates one day of husband."""
    if husband.get_satiety() <= 30:
        husband.eat(house)
    elif husband.get_happy() <= 50:
        husband.game()
    else:
        husband.go_work(house)


def simulate_wife_day(wife, house):
    """Function simulates one day of wife."""
    if house.get_dirt() >= 70:
        wife.clean_up(house)
    elif wife.get_satiety() <= 30:
        wife.eat(house)
    elif house.get_humans_food() <= 50:
        wife.buy_humans_food(house)
    elif house.get_cats_food() <= 10:
        wife.buy_cats_food(house)
    elif house.get_money() >= 1500:
        wife.buy_fur_coat(house, 1500)
    else:
        wife.pet_a_cat()


def simulate_cat_day(cat, house):
    """Function simulates one day of cat."""
    action = randint(1, 2)
    if cat.get_satiety() <= 10:
        cat.eat(house)
    elif action == 1:
        cat.sleep()
    elif action == 2:
        cat.tear_wallpapers(house)


if __name__ == '__main__':
    start_life_simulator()
