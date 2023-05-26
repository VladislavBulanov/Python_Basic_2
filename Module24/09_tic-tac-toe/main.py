from tic_tac_toe import Board, Player


def play_game():
    print('ДОБРО ПОЖАЛОВАТЬ В ИГРУ "КРЕСТИКИ-НОЛИКИ"!\n')
    player_1 = Player(input('Введите имя первого игрока (крестик): '), 'X')
    player_2 = Player(input('Введите имя второго игрока (нолик): '), 'O')
    board = Board()

    while True:
        board.draw()
        player_1.make_move(board)
        if board.check_win():
            print('\nПОЗДРАВЛЯЕМ, {}! ВЫ ВЫИГРАЛИ!'.format(
                player_1.name.upper()
            ))
            board.draw()
            return
        if board.is_full():
            break
        board.draw()
        player_2.make_move(board)
        if board.check_win():
            print('\nПОЗДРАВЛЯЕМ, {}! ВЫ ВЫИГРАЛИ!'.format(
                player_2.name.upper()
            ))
            board.draw()
            return

    print('\nНИЧЬЯ!')
    board.draw()


if __name__ == '__main__':
    play_game()
