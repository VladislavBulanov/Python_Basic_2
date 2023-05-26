# Задача 2. Сессия


print('Введите первую точку: ')
x1 = float(input('X: '))
y1 = float(input('Y: '))
print('\nВведите вторую точку: ')
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2

if x_diff == 0:
    print('\nУравнение вида y = k * x + b составить нельзя.')
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print('\nУравнение прямой, проходящей через эти точки: ')
    if k == 0 and b == 0:
        print('y = 0')
    elif k == 0:
        print(f'y = {b}')
    elif b == 0:
        print(f'y = {k} * x')
    elif b < 0:
        print(f'y = {k} * x - {abs(b)}')
    else:
        print(f'y = {k} * x + {b}')
