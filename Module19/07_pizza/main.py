def generate_orders_list(quantity):
    return [input(f'{index + 1}-й заказ (имя_пицца_количество): ').split()
            for index in range(quantity)]


def detail_orders_information(list_of_orders):
    detailed_data = dict()

    for item in list_of_orders:
        # Если человек ещё не делал заказ:
        if item[0] not in detailed_data:
            detailed_data[item[0]] = {item[1]: int(item[2])}
        # Если человек уже делал заказ,
        # но пицца была другая:
        elif item[1] not in detailed_data[item[0]]:
            detailed_data[item[0]][item[1]] = int(item[2])
        # Если человек уже заказывал данную пиццу:
        else:
            detailed_data[item[0]][item[1]] += int(item[2])

    return detailed_data


orders_quantity = int(input('Введите количество заказов: '))
orders_list = generate_orders_list(orders_quantity)
detailed_orders_information = detail_orders_information(orders_list)

print('\nПодробная информация о заказах:')
for key in sorted(detailed_orders_information):
    print(f'{key}:')
    for current_key in sorted(detailed_orders_information[key]):
        print(f'\t\t{current_key}: {detailed_orders_information[key][current_key]}')
