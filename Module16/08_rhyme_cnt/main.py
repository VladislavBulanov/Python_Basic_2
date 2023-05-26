def find_winner(players_list, number):
    current_index = 0
    players_quantity = len(players_list)

    while players_quantity > 1:
        print('Текущий круг людей:', players_list)
        print('Начало счёта с номера', players_list[current_index])

        current_index = (current_index + number - 1) % players_quantity

        # Обрабатываем случай, когда выбывший является последним в списке, и,
        # таким образом, после его "удаления" текущий индекс выйдет за
        # пределы размерности:
        if current_index == players_quantity - 1:
            print(f'Выбывает человек под номером {players_list.pop(current_index)}\n')
            current_index = 0
        else:
            print(f'Выбывает человек под номером {players_list.pop(current_index)}\n')

        players_quantity -= 1


human_quantity = int(input('Введите количество человек: '))
human_list = list(range(1, human_quantity + 1))
counting_number = int(input('Введите число в считалке: '))
print(f'Значит, выбывает каждый {counting_number}-й человек.\n')

find_winner(human_list, counting_number)
print('Остался человек под номером', *human_list)
