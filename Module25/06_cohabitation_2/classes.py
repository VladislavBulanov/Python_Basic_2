"""The module describing classes for the simulating cohabitation."""


class House:
    """The class describing house."""
    def __init__(
            self,
            money: int = 100,
            humans_food: int = 50,
            cats_food: int = 30,
            dirt: int = 0
    ):
        """
        Class constructor.
        :param money: quantity of money in house
        :param humans_food: quantity of food for humans in house
        :param cats_food: quantity of food for cats in house
        :param dirt: quantity of dirt in house
        """
        self.__money = money
        self.__humans_food = humans_food
        self.__cats_food = cats_food
        self.__dirt = dirt

    def print_general_info(self):
        """Displays all attributes of class exemplar."""
        print('\nСОСТОЯНИЕ ДОМА:\nДеньги: {}\nПродукты: {}'.format(
            self.get_money(),
            self.get_humans_food()
        ))
        print('Корм: {}\nГрязь: {}'.format(
            self.get_cats_food(),
            self.get_dirt()
        ))

    def get_money(self) -> int:
        """Getter of money quantity in house."""
        return self.__money

    def set_money(self, money: int):
        """Setter of money quantity in house."""
        self.__money = money

    def get_humans_food(self) -> int:
        """Getter of human's food quantity in house."""
        return self.__humans_food

    def set_humans_food(self, humans_food: int):
        """Setter of human's food quantity in house."""
        self.__humans_food = humans_food

    def get_cats_food(self) -> int:
        """Getter of cat's food quantity in house."""
        return self.__cats_food

    def set_cats_food(self, cats_food: int):
        """Setter of cat's food quantity in house."""
        self.__cats_food = cats_food

    def get_dirt(self) -> int:
        """Getter of dirt quantity in house."""
        return self.__dirt

    def set_dirt(self, dirt: int):
        """Setter of dirt quantity in house."""
        self.__dirt = dirt


class Human:
    """
    The class describing human. Each action (except eat) decreases
    degree of satiety by 10 points.
    """
    def __init__(
            self,
            name: str,
            satiety: int = 30,
            happy: int = 100,
            eaten_food: int = 0
    ):
        """
        Class constructor.
        :param name: name of human
        :param satiety: degree of human's satiety
        :param happy: degree of human's happy
        :param eaten_food: how much food was eaten
        """
        self.__name = name
        self.__satiety = satiety
        self.__happy = happy
        self.__eaten_food = eaten_food

    def get_name(self) -> str:
        """Getter of human's name."""
        return self.__name

    def set_name(self, name: str):
        """Setter of human's name."""
        self.__name = name

    def get_satiety(self) -> int:
        """Getter of degree of human's satiety."""
        return self.__satiety

    def set_satiety(self, satiety: int):
        """
        Setter of degree of human's satiety.
        After setting check if satiety is less than or equal to zero.
        Raise error 'died of hunger' if it is.
        :param satiety: degree of human's satiety
        :raise ValueError: if satiety is less than or equal to zero
        """
        self.__satiety = satiety
        if self.get_satiety() <= 0:
            raise ValueError('ЧЕЛОВЕК УМЕР ОТ ГОЛОДА!')

    def get_happy(self) -> int:
        """Getter of degree of human's happy."""
        return self.__happy

    def set_happy(self, happy: int):
        """
        Setter of degree of human's happy.
        After setting check if happy is less than ten.
        Raise error 'died of depression' if it is.
        :param happy: degree of human's happy
        :raise ValueError: if happy is less than ten
        """
        self.__happy = happy
        if self.get_happy() < 10:
            raise ValueError('ЧЕЛОВЕК УМЕР ОТ ДЕПРЕССИИ!')

    def get_eaten_food(self) -> int:
        """Getter of eaten food."""
        return self.__eaten_food

    def set_eaten_food(self, food: int):
        """Setter of eaten food."""
        self.__eaten_food = food

    def eat(self, house: House, food_quantity: int = 20):
        """
        Method allows human increase his degree of satiety by specified points.
        Human can eat only 30 units of food per time.
        :param house: the house where human lives
        :param food_quantity: total food human will eat
        """
        if house.get_humans_food() >= food_quantity:
            self.set_satiety(self.get_satiety() + food_quantity)
            self.set_eaten_food(self.get_eaten_food() + food_quantity)
            house.set_humans_food(house.get_humans_food() - food_quantity)
            print('{} поел(а).'.format(self.get_name()))
        else:
            print('Недостаточное количество еды.')
            self.set_satiety(self.get_satiety() - 10)

    def pet_a_cat(self):
        """
        Human pets a cat, this increases
        human's degree of happy by 5 points.
        """
        self.set_happy(self.get_happy() + 5)
        self.set_satiety(self.get_satiety() - 10)
        print('{} погладил(а) кота.'.format(self.get_name()))


class Husband(Human):
    """
    The subclass of class 'Human' describing husband. Each action
    (except eat) decreases degree of satiety by 10 points.
    """
    def __init__(self, name: str, earned_money: int = 0):
        """
        Class constructor.
        :param name: husband's name
        :param earned_money: quantity of earned money by husband
        """
        super().__init__(name)
        self.__earned_money = earned_money

    def print_general_info(self):
        """Displays all attributes of class exemplar."""
        print('\nИНФОРМАЦИЯ О МУЖЕ:\nИмя: {}\nСытость: {}\nСчастье: {}'.format(
            self.get_name(),
            self.get_satiety(),
            self.get_happy()
        ))

    def get_earned_money(self) -> int:
        """Getter of earned money by husband."""
        return self.__earned_money

    def set_earned_money(self, total: int):
        """Setter of earned money by husband."""
        self.__earned_money = total

    def game(self):
        """Husband plays computer. It increases his happy by 20 points."""
        self.set_happy(self.get_happy() + 20)
        self.set_satiety(self.get_satiety() - 10)
        print('{} поиграл в компьютер.'.format(self.get_name()))

    def go_work(self, house: House, salary: int = 150):
        """
        Husband goes to the work and brings salary
        in house (150 units of money by default).
        :param house: house where husband lives
        :param salary: husband's salary
        """
        house.set_money(house.get_money() + salary)
        self.set_earned_money(self.get_earned_money() + salary)
        self.set_satiety(self.get_satiety() - 10)
        print('{} сходил на работу.'.format(self.get_name()))


class Wife(Human):
    """
    The subclass of class 'Human' describing wife. Each action
    (except eat) decreases degree of satiety by 10 points.
    """
    def __init__(self, name: str, fur_coat_amount: int = 0):
        """Class constructor."""
        super().__init__(name)
        self.__fur_coat_amount = fur_coat_amount

    def print_general_info(self):
        """Displays all attributes of class exemplar."""
        print('\nИНФОРМАЦИЯ О ЖЕНЕ:\nИмя: {}\nСытость: {}'.format(
            self.get_name(),
            self.get_satiety()
        ))
        print('Счастье: {}\nКоличество шуб: {}'.format(
            self.get_happy(),
            self.get_fur_coat_amount()
        ))

    def get_fur_coat_amount(self) -> int:
        """Getter of wife's fur coat amount."""
        return self.__fur_coat_amount

    def set_fur_coat_amount(self, quantity: int):
        """Setter of wife's fur coat amount."""
        self.__fur_coat_amount = quantity

    def buy_humans_food(self, house: House):
        """
        Wife buys human's food. It costs 50 units of money
        and increases human's food in the house by 50 units.
        :param house: house where wife lives
        """
        if house.get_money() >= 50:
            house.set_money(house.get_money() - 50)
            house.set_humans_food(house.get_humans_food() + 50)
            print('{} купила продукты.'.format(self.get_name()))
        else:
            print('Недостаточное количество денег.')
        self.set_satiety(self.get_satiety() - 10)

    def buy_cats_food(self, house: House):
        """
        Wife buys cat's food. It costs 30 units of money
        and increases cat's food in the house by 30 units.
        :param house: house where wife lives
        """
        if house.get_money() >= 30:
            house.set_money(house.get_money() - 30)
            house.set_cats_food(house.get_cats_food() + 30)
            print('{} купила кошачий корм.'.format(self.get_name()))
        else:
            print('Недостаточное количество денег.')
        self.set_satiety(self.get_satiety() - 10)

    def buy_fur_coat(self, house: House, money_limit: int = 400):
        """
        Wife buys a fur coat. It costs 350 units of money and gives 60 points
        of happy. Wife can make purchase if there is enough quantity of money
        (400 units by default).
        :param house: the house where wife lives
        :param money_limit: the quantity of money in the house allows
        to make a purchase
        """
        if house.get_money() >= money_limit:
            house.set_money(house.get_money() - 350)
            self.set_happy(self.get_happy() + 60)
            self.set_fur_coat_amount(self.get_fur_coat_amount() + 1)
            print('{} купила шубу.'.format(self.get_name()))
        else:
            print('Сейчас недостаточно денег для покупки шубы.')
        self.set_satiety(self.get_satiety() - 10)

    def clean_up(self, house: House):
        """
        Wife cleans up in the house. The quantity
        of dirt decreases by 100 points.
        :param house: the house where wife cleans up
        """
        if house.get_dirt() > 100:
            house.set_dirt(house.get_dirt() - 100)
        else:
            house.set_dirt(0)
        self.set_satiety(self.get_satiety() - 10)
        print('{} убралась в доме.'.format(self.get_name()))


class Cat:
    """
    The class describing cat. Each action (except eat)
    decreases degree of satiety by 10 points.
    """
    def __init__(self, name: str, satiety: int = 30):
        """
        Class constructor.
        :param name: cat's name
        :param satiety: degree of cat's satiety
        """
        self.__name = name
        self.__satiety = satiety

    def print_general_info(self):
        """Displays all attributes of class exemplar."""
        print('\nИНФОРМАЦИЯ О КОТЕ/КОШКЕ:')
        print('Кличка: {}\nСытость: {}'.format(
            self.get_name(),
            self.get_satiety()
        ))

    def get_name(self) -> str:
        """Getter of cat's name."""
        return self.__name

    def set_name(self, name: str):
        """Setter of cat's name."""
        self.__name = name

    def get_satiety(self) -> int:
        """Getter of cat's satiety."""
        return self.__satiety

    def set_satiety(self, satiety: int):
        """
        Setter of degree of cat's satiety.
        After setting check if satiety is less than or equal to zero.
        Raise error 'died of hunger' if it is.
        :param satiety: degree of cat's satiety
        :raise ValueError: if satiety is less than or equal to zero
        """
        self.__satiety = satiety
        if self.get_satiety() <= 0:
            raise ValueError('КОТ УМЕР ОТ ГОЛОДА!')

    def eat(self, house: House):
        """
        Method allows cat increase his degree of satiety
        (one unit of food - two points of degree of satiety).
        :param house: the house where cat lives
        """
        if house.get_cats_food() >= 10:
            self.set_satiety(self.get_satiety() + 20)
            house.set_cats_food(house.get_cats_food() - 10)
            print('{} поел(а).'.format(self.get_name()))
        else:
            print('Недостаточное количество корма.')
            self.set_satiety(self.get_satiety() - 10)

    def sleep(self):
        """Cat sleeps."""
        self.set_satiety(self.get_satiety() - 10)
        print('{} поспал(а).'.format(self.get_name()))

    def tear_wallpapers(self, house: House):
        """
        Cat tears the wallpapers. It increases quantity of dirt by five points in house
        where cat lives.
        :param house: house where cat lives
        """
        house.set_dirt(house.get_dirt() + 5)
        self.set_satiety(self.get_satiety() - 10)
        print('{} подрал(а) обои.'.format(self.get_name()))
