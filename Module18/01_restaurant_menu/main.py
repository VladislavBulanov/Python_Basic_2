def get_menu(list_of_dishes):
    return ', '.join(list_of_dishes)


dishes_list = input('Доступное меню ресторана: ').lower().split(';')
menu = get_menu(dishes_list)
print('\nНа данный момент в меню есть: {}.'.format(menu))
