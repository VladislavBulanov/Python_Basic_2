from blackjack import Deck, Human
from random import randint


def get_two_starting_cards(man, current_deck):
    for _ in range(2):
        man.get_card(current_deck, randint(0, len(current_deck.deck) - 1))


def who_wins(player, dealer):
    players_points = player.calculate_points()
    dealers_points = dealer.calculate_points()
    print('\nВАШИ ОЧКИ:', players_points)
    print('ОЧКИ ДИЛЕРА:', dealers_points)
    if players_points > dealers_points:
        print('\nВЫ ПОБЕДИЛИ!')
    elif players_points < dealers_points:
        print('\nВЫ ПРОИГРАЛИ!')
    else:
        print('НИЧЬЯ')


def start_game():
    print('======= ИГРА БЛЭКДЖЕК НАЧАЛАСЬ =======\n')
    player = Human()
    dealer = Human()
    deck = Deck()

    print('Игрок и дилер получили по две карты.')
    get_two_starting_cards(player, deck)
    get_two_starting_cards(dealer, deck)

    while True:
        print('\nВАШИ КАРТЫ:')
        player.show_cards()
        current_points = player.calculate_points()
        print('Сумма очков: ', current_points)

        if current_points > 21:
            print('\nПЕРЕБОР! ВЫ ПРОИГРАЛИ!')
            break
        else:
            print('\n1 - взять ещё карту\n2 - открыться')
            player_choice = input('Ваш выбор: ')

            if player_choice == '1':
                player.get_card(deck, randint(0, len(deck.deck) - 1))
            elif player_choice == '2':
                who_wins(player, dealer)
                break
            else:
                print('Нет такого пункта, пожалуйста, повторите ввод.')


if __name__ == '__main__':
    start_game()
