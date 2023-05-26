from math import pi

class Circle:

    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius


    def show_circle_data(self):
        print('\nx: {}\ny: {}\nradius: {}'.format(
            self.x,
            self.y,
            self.radius
        ))


    def calculate_area(self):
        return pi * self.radius ** 2


    def calculate_circumference(self):
        return 2 * pi * self.radius


    def increase_by_k_times(self, coefficient):
        area = self.calculate_area()
        if coefficient > 0:
            new_area = area * coefficient
            self.radius = (new_area / pi) ** 0.5
        elif coefficient < 0:
            new_area = area / abs(coefficient)
            self.radius = (new_area / pi) ** 0.5


    def is_intersects(self, another_circle):
        """
        :return: True if circles intersect each other, False if they don't.
        """
        x_2 = another_circle.x
        y_2 = another_circle.y
        radius_2 = another_circle.radius
        distance = (((self.x - x_2) ** 2) + ((self.y - y_2) ** 2)) ** 0.5
        return distance < (self.radius + radius_2)


# Tests:
# circle_1 = Circle()
#
# print(circle_1.calculate_area())
#
# print(circle_1.calculate_circumference())
#
# circle_1.increase_by_k_times(2)
# circle_1.show_circle_data()
#
# circle_2 = Circle(2, 0, 1)
# print(circle_1.is_intersects(circle_2))
