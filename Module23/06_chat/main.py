def start_chat():
    print('=====ПРИВЕТСТВУЕМ ВАС В ЧАТЕ=====')
    user_name = input('\nВведите своё имя: ')
    print('\nВы можете посмотреть текущий текст чата (1) '
          'или отправить сообщение (2).')

    while True:
        user_choice = input('Введите Ваш выбор - посмотреть/отправить (1/2): ')
        if user_choice == '1':
            try:
                with open('custom_chat.txt', 'r', encoding='utf-8') as file:
                    print(file.read())
            except FileNotFoundError:
                print('\nЧат пока пуст.')

        elif user_choice == '2':
            with open('custom_chat.txt', 'a', encoding='utf-8') as file:
                message = input('Введите сообщение: ')
                file.write(f'{user_name}: {message}\n')
        else:
            print('Некорректный выбор. Пожалуйста, повторите ввод.\n')


start_chat()
