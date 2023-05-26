from vehicles import Car, Bus


def start_drive_simulator():
    while True:
        print('\nВЫБЕРЕТЕ, ДВИЖЕНИЕ КАКОГО ТРАНСПОРТНОГО СРЕДСТВА ВЫ ХОТИТЕ '
              'СМОДЕЛИРОВАТЬ:\n1. Автомобиль\n2. Автобус\n3. Выйти из программы')
        user_choice = input('Ваш выбор: ')
        if user_choice not in ('1', '2', '3'):
            print('Некорректный ввод, попробуйте снова.\n')
        elif user_choice == '1':
            car_drive_simulator()
        elif user_choice == '2':
            bus_drive_simulator()
        elif user_choice == '3':
            print('\nПрограмма завершена.')
            return


def car_drive_simulator():
    car = Car()
    print('\nДОБРО ПОЖАЛОВАТЬ В СИМУЛЯТОР ДВИЖЕНИЯ АВТОМОБИЛЯ!')
    while True:
        show_cars_actions()
        user_choice = int(input('Ваш выбор: '))

        if user_choice not in range(1, 6):
            print('Некорректный ввод, попробуйте снова.\n')

        elif user_choice == 1:
            print('Текущие координаты автомобиля (x, y): {}'.format(
                car.get_position()
            ))

        elif user_choice == 2:
            print('Угол движения автомобиля (относительно оси х): {} град.'.format(
                car.get_angle()
            ))

        elif user_choice == 3:
            try:
                distance = float(input('Введите дистанцию: '))
                car.move(distance)
            except ValueError:
                print('ОШИБКА: дистанция должна быть числом.')

        elif user_choice == 4:
            try:
                angle = float(input('Введите угол (град.): '))
                car.turn(angle)
            except ValueError:
                print('ОШИБКА: угол должен быть числом.')

        elif user_choice == 5:
            return


def show_cars_actions():
    print('\nВыберите действие:')
    print('1. Показать текущие координаты автомобиля')
    print('2. Показать угол движения автомобиля')
    print('3. Задать дистанцию, на которую переместится автомобиль')
    print('4. Повернуть на заданный угол')
    print('5. Выйти в главное меню')


def bus_drive_simulator():
    bus = Bus()
    print('\nДОБРО ПОЖАЛОВАТЬ В СИМУЛЯТОР ДВИЖЕНИЯ АВТОБУСА!')
    while True:
        show_bus_actions()
        user_choice = int(input('Ваш выбор: '))

        if user_choice not in range(1, 10):
            print('Некорректный ввод, попробуйте снова.\n')

        elif user_choice == 1:
            print('Текущие координаты автомобиля (x, y): {}'.format(
                bus.get_position()
            ))

        elif user_choice == 2:
            print('Угол движения автобуса (относительно оси х): {} град.'.format(
                bus.get_angle()
            ))

        elif user_choice == 3:
            print('В автобусе сейчас {} человек(а).'.format(
                bus.get_passengers()
            ))

        elif user_choice == 4:
            print('За поездку водитель заработал {} руб.'.format(
                bus.get_money()
            ))

        elif user_choice == 5:
            try:
                distance = float(input('Введите дистанцию: '))
                bus.move(distance)
            except ValueError:
                print('ОШИБКА: дистанция должна быть числом.')

        elif user_choice == 6:
            try:
                angle = float(input('Введите угол (град.): '))
                bus.turn(angle)
            except ValueError:
                print('ОШИБКА: угол должен быть числом.')

        elif user_choice == 7:
            try:
                passengers_in = int(input('Сколько пассажиров берём на борт: '))
                bus.board(passengers_in)
            except ValueError:
                print('ОШИБКА: количество должно быть целым положительным числом.')

        elif user_choice == 8:
            try:
                passengers_out = int(input('Сколько пассажиров выходит из автобуса: '))
                if passengers_out <= bus.get_passengers():
                    bus.leave(passengers_out)
                else:
                    print('Введённое количество превышает текущее '
                          'количество пассажиров в автобусе.')
            except ValueError:
                print('ОШИБКА: количество должно быть целым положительным числом.')

        elif user_choice == 9:
            return


def show_bus_actions():
    print('\nВыберите действие:')
    print('1. Показать текущие координаты автобуса')
    print('2. Показать угол движения автобуса')
    print('3. Показать количество пассажиров на борту')
    print('4. Показать количество заработанных денег')
    print('5. Задать дистанцию, на которую переместится автобус')
    print('6. Повернуть на заданный угол')
    print('7. Посадить пассажиров в автобус')
    print('8. Высадить пассажиров из автобуса')
    print('9. Выйти в главное меню')


if __name__ == '__main__':
    start_drive_simulator()
