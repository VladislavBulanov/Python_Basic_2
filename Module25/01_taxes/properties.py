"""This module describing difference types of human properties."""


class Property:
    """Basic class describing human's property."""
    def __init__(self, worth: float):
        """
        :param worth: property cost
        """
        self.__worth = 0
        self.set_worth(worth)

    def get_worth(self) -> float:
        """Worth getter."""
        return self.__worth

    def set_worth(self, source_worth: float):
        """Worth setter."""
        if source_worth >= 0:
            self.__worth = source_worth
        else:
            raise Exception('Стоимость не может быть отрицательной.')

    def calculate_tax(self, coefficient=10) -> float:
        """
        Calculation of property tax.
        :param coefficient: tax coefficient for current type of property
        """
        return self.__worth / coefficient


class Apartment(Property):
    """A class describing human's apartment."""
    def __init__(self, apartment_worth: float):
        """
        :param apartment_worth: apartment's cost
        """
        super().__init__(apartment_worth)

    def calculate_tax(self, coefficient=1000) -> float:
        """
        :return: apartment's tax
        """
        return self.get_worth() / coefficient


class Car(Property):
    """A class describing human's car."""
    def __init__(self, car_worth: float):
        """
        :param car_worth: car's cost
        """
        super().__init__(car_worth)

    def calculate_tax(self, coefficient=200) -> float:
        """
        :return: car's tax
        """
        return self.get_worth() / coefficient


class CountryHouse(Property):
    """A class describing human's country house."""
    def __init__(self, house_worth: float):
        """
        :param house_worth: country house cost
        """
        super().__init__(house_worth)

    def calculate_tax(self, coefficient=500) -> float:
        """
        :return: country house tax
        """
        return self.get_worth() / coefficient
