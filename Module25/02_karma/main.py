from random import randint
from  os import path
from errors import (
    KillError, DrunkError, CarCrashError, GluttonyError, DepressionError
)


class Human:
    """Class create human with karma points."""
    def __init__(self, karma_points=0):
        self.__karma_points = karma_points

    def get_karma_points(self):
        """Karma points getter."""
        return self.__karma_points

    def set_karma_points(self, points: int):
        """Karma points setter."""
        self.__karma_points = points


def simulate_life():
    """
    The main function of program which create human and possible karma
    violations (errors) and simulate human's life with observation of karma.
    Karma violations are written in logfile.
    """
    human = Human()
    possible_errors = create_possible_errors()

    while human.get_karma_points() < 500:
        try:
            one_day(human)
        except Warning:
            with open(path.abspath('karma.log'), 'a', encoding='utf-8') as log_file:
                log_file.write('{}\n'.format(
                    str(possible_errors[randint(0, 4)])
                ))

    print('\nВаши очки кармы: {}.\nВЫ ДОСТИГЛИ ПРОСВЕТЛЕНИЯ!'.format(
        human.get_karma_points()
    ))


def one_day(human):
    """
    Simulating of one day of human. Human can earn karma points
    or can raise karma violation.
    """
    if randint(1, 10) == 1:
        raise Warning
    else:
        karma_gain = randint(1, 7)
        human.set_karma_points(human.get_karma_points() + karma_gain)


def create_possible_errors():
    """
    Creating possible karma violations (subclasses of Error class).
    :rtype: tuple
    """
    kill = KillError()
    drunk = DrunkError()
    car_crash = CarCrashError()
    gluttony = GluttonyError()
    depression = DepressionError()
    return kill, drunk, car_crash, gluttony, depression


if __name__ == '__main__':
    simulate_life()
