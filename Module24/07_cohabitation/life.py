class Human:

    def __init__(self, name, house, satiety=50):
        self.name = name
        self.house = house
        self.satiety = satiety

    def eat(self, gain):
        print('{} ест (+{} к сытости, -{} еды)'.format(
            self.name,
            gain,
            gain
        ))
        self.satiety += gain
        self.house.food -= gain

    def go_to_store(self, gain):
        print('{} идёт в магазин (+{} к еде, -{} денег)'.format(
            self.name,
            gain,
            gain
        ))
        self.house.food += gain
        self.house.money -= gain

    def go_work(self, gain):
        print('{} идёт на работу (+{} к деньгам, -{} сытости)'.format(
            self.name,
            gain,
            gain
        ))
        self.house.money += gain
        self.satiety -= gain

    def play(self, gain):
        print('{} играет (-{} сытости)'.format(
            self.name,
            gain
        ))
        self.satiety -= gain


class House:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money
