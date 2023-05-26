violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
total_time = 0
quantity = int(input('Введите количество песен: '))

for index in range(quantity):
    song = input(f'Название {index + 1}-ой песни: ')

    for element in violator_songs:
        if song in element:
            total_time += element[1]

print(f'\nОбщее время звучания песен: {round(total_time, 2)} минут(ы).')
