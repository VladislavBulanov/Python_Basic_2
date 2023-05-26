from garden import PotatoGarden, Gardener


def create_gardener():
    gardener_name = input('Введите имя садовника: ')
    potato_count = int(input('Введите количество картошки, за которой он ухаживает: '))
    current_garden = PotatoGarden(potato_count)
    current_gardener = Gardener(gardener_name, current_garden)
    return current_gardener


def start_gameplay(character):
    while True:
        print('\nВыберете действие:')
        print('1 - Показать текущее состояние картошки')
        print('2 - Поухаживать за картошкой')
        print('3 - Собрать урожай')
        print('4 - Показать количество собранного урожая')
        print('5 - Выйти из игры')
        try:
            user_choice = int(input('Ваш выбор: '))
            if user_choice not in (1, 2, 3, 4, 5):
                print('Нет такого пункта. Пожалуйста, повторите ввод.')
            elif user_choice == 1:
                character.potato_garden.print_potatoes_state()
            elif user_choice == 2:
                character.take_care()
            elif user_choice == 3:
                character.collect_harvest()
            elif user_choice == 4:
                character.show_collected_harvest()
            elif user_choice == 5:
                print('\nИГРА ЗАВЕРШЕНА!')
                break
        except ValueError:
            print('Значение должно быть целым числом. Пожалуйста, повторите ввод.')


def main():
    print('======= ДОБРО ПОЖАЛОВАТЬ В ИГРУ "ВЕСЁЛАЯ ФЕРМА"! =======\n')
    print('ДАВАЙТЕ СОЗДАДИМ САД')
    gardener = create_gardener()
    start_gameplay(gardener)


if __name__ == '__main__':
    main()
