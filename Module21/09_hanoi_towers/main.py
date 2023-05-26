def move(number, start_rod, finish_rod):
    # Выражение '6 - start_rod - finish_rod' означает,
    # что мы используем вспомогательный колышек.
    if number == 1:
        print(f'Переложить диск {number} со стержня номер '
              f'{start_rod} на стержень номер {finish_rod}')
    else:
        move(number - 1, start_rod, 6 - start_rod - finish_rod)
        print(f'Переложить диск {number} со стержня номер '
              f'{start_rod} на стержень номер {finish_rod}')
        move(number - 1, 6 - start_rod - finish_rod, finish_rod)


discs_quantity = int(input('Введите количество дисков: '))
move(discs_quantity, 1, 3)
