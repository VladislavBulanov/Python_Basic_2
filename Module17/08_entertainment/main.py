import random

def make_sticks_row(quantity):
    return ['I' for _ in range(quantity)]


def generate_interval(limit):
    return [random.randint(1, limit) for _ in range(2)]


def shot_result(current_row, left_border, right_border):
    result_row = current_row[:]
    result_row[left_border - 1:right_border] = ['.' for _ in range(right_border - left_border + 1)]
    return result_row


total_sticks = int(input('Введите количество палок: '))
total_shots = int(input('Введите количество бросков: '))

sticks_row = make_sticks_row(total_sticks)

for time in range(1, total_shots + 1):
    strike_interval = sorted(generate_interval(total_sticks))
    left_downed_stick = strike_interval[0]
    right_downed_stick = strike_interval[1]

    print('\nБросок {0}. Сбиты палки с номера {1}\nпо номер {2}.'.format(
        time,
        left_downed_stick,
        right_downed_stick
    ))

    sticks_row = shot_result(sticks_row, left_downed_stick, right_downed_stick)

print('\nРезультат:', "".join(sticks_row))
