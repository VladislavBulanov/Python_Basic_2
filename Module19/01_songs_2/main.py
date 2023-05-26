def calculate_total_time(playlist, tracks_quantity):
    time = 0

    for index in range(tracks_quantity):
        while True:
            song = input(f'Введите название {index + 1}-й песни: ')
            if song in playlist:
                time += playlist[song]
                break
            else:
                print('Такой песни нет. Пожалуйста, повторите ввод.\n')

    return time


violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_quantity = int(input('Сколько песен выбрать? '))
total_time = calculate_total_time(violator_songs, songs_quantity)
print(f'\nОбщее время звучания песен: {round(total_time, 2)} минут(ы).')
