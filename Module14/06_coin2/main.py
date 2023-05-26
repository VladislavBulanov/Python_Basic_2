# Задача 6. Монетка 2


import math


def distance(dot_1, dot_2):
    return math.sqrt((dot_1 ** 2) + (dot_2 ** 2))


print('Введите координаты монетки: ')
x = float(input('X: '))
y = float(input('Y: '))
radius = float(input('Введите радиус: '))

if distance(x, y) > radius:
    print('\nМонетки в области нет.')
else:
    print('\nМонетка где-то рядом.')
