"""
Module describing two classes of vehicle: car (main class) and bus (subclass).
"""

from  math import sin, cos, radians


class Car:
    """
    Main class describing car: coordinates defining the car's position
    and angle (degrees) of moving direction.
    """
    def __init__(self, x: float = 0, y: float = 0, angle: float = 0):
        """
        Class constructor.
        :param x: coordinate x
        :type x: float
        :param y: coordinate y
        :type y: float
        :param angle: angle (degrees) of moving direction
        :type angle: float
        """
        self.__x = x
        self.__y = y
        self.__angle = angle

    def get_position(self):
        """
        Car's position getter.
        :rtype: tuple
        """
        return self.__x, self.__y

    def set_position(self, x: float, y: float):
        """Car's position setter."""
        self.__x = x
        self.__y = y

    def get_angle(self):
        """
        Car's angle getter.
        :rtype: float
        """
        return self.__angle

    def set_angle(self, angle: float):
        """Car's angle setter."""
        self.__angle = angle

    def move(self, distance: float):
        """
        Forces the vehicle to move a specified distance.
        Sets new coordinates of vehicle.
        :param distance: the distance to which the car should move
        :type distance: float
        """
        difference_x = distance * cos(radians(self.__angle))
        difference_y = distance * sin(radians(self.__angle))
        self.__x += difference_x
        self.__y += difference_y

    def turn(self, angle: float):
        """
        Forces the vehicle to change direction by a specified angle.
        :param angle: the angle by which the direction changes
        :type angle: float
        """
        self.__angle += angle


class Bus(Car):
    """
    Subclass of class 'Car' describing bus position, direction of moving
    as well as information about passengers and money earned.
    """
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        angle: float = 0,
        passengers: int = 0,
        money: float = 0
    ):
        """
        Class constructor.
        :param x: coordinate x
        :param y: coordinate y
        :param angle: angle (degrees) of moving direction
        :param passengers: quantity of passengers in bus
        :param money: earned money
        """
        super().__init__(x, y, angle)
        self.__passengers = passengers
        self.__money = money


    def get_passengers(self):
        """
        Quantity of passengers getter.
        :rtype: int
        """
        return self.__passengers

    def set_passengers(self, passengers: int):
        """Quantity of passengers setter."""
        self.__passengers = passengers

    def get_money(self):
        """
        Amount money getter.
        :rtype: float
        """
        return self.__money

    def set_money(self, money: float):
        """Amount money setter."""
        self.__money = money

    def move(self, distance: float):
        """
        Forces the vehicle to move a specified distance.
        Sets new coordinates of vehicle and collects money.
        :param distance: the distance to which the car should move
        :type distance: float
        """
        super().move(distance)
        self.__money += distance * self.__passengers

    def board(self, passengers: int):
        """Take passengers on board (increase passengers quantity)."""
        self.__passengers += passengers

    def leave(self, passengers: int):
        """Disembark passengers from the board (decrease passengers quantity)."""
        self.__passengers -= passengers
