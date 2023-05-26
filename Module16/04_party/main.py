guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
    choice = input('Гость пришёл или ушёл? ').lower()
    if choice == 'пора спать':
        break
    else:
        guest_name = input('Имя гостя: ')

        if choice == 'пришёл' or choice == 'пришел':
            if len(guests) < 6:
                print(f'Привет, {guest_name}!\n')
                guests.append(guest_name)
            else:
                print(f'Прости, {guest_name}, но мест нет.\n')

        elif choice == 'ушёл' or choice == 'ушел':
            print(f'Пока, {guest_name}!\n')
            guests.remove(guest_name)

print('\nВечеринка закончилась, все легли спать.')
