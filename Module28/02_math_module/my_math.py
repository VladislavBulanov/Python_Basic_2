from math import pi
from abc import ABC, abstractmethod


class MyMath(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    def circle_len(cls, radius: float) -> float:
        """Calculates length of circle with specified radius."""
        return 2 * pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """Calculates square of circle with specified radius."""
        return pi * radius ** 2

    @classmethod
    def cube_volume(cls, length: float) -> float:
        """Calculates volume of cube with specified length."""
        return length ** 3

    @classmethod
    def sphere_surface_square(cls, radius: float) -> float:
        """Calculates square of sphere surface with specified radius."""
        return 4 * pi * radius ** 2
