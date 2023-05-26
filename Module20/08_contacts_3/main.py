def add_contact(source_contacts):
    """
    :param source_contacts: actual dictionary of contacts
    :type: dict
    :returns: depend on inputted information return current or updated dictionary
    :rtype: dict
    """
    current_contacts = {key: value for key, value in source_contacts.items()}
    new_name, new_surname = input('\nВведите имя и фамилию нового контакта '
                                  '(через пробел): ').split()

    for person in current_contacts:
        if new_name.lower() == person[0].lower() and new_surname.lower() == person[1].lower():
            print('Такой человек уже есть в контактах.')
            break
    else:
        new_phone_number = int(input('Введите номер телефона: '))
        current_contacts[(new_name, new_surname)] = new_phone_number

    print('Текущий словарь контактов:', current_contacts)
    return current_contacts


def find_person(initial_contacts):
    surname = input('Введите фамилию для поиска: ').lower()

    found_matches = {human: number for human, number in initial_contacts.items()
                     if human[1].lower() == surname}

    if found_matches:
        for human, number in found_matches.items():
            print(*human, number)


contacts = dict()

while True:
    user_choice = int(input('\nВведите номер действия:\n'
                            '\t1. Добавить контакт\n'
                            '\t2. Найти человека\n'))

    if user_choice not in (1, 2):
        print('Такого пункта меню не существует. Пожалуйста, повторите ввод.')
    else:
        if user_choice == 1:
            contacts = add_contact(contacts)
        elif user_choice == 2:
            find_person(contacts)
