def count_of_item(source_item, source_items_list):
    result_list = [0, 0]  # [0] - total count, [1] - total price
    for element in source_items_list:
        item_quantity = element.count(source_item)
        if item_quantity:
            result_list[0] += 1
            result_list[1] += element[1]

    return result_list


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

item = input('Введите название детали: ').lower()

data_list = count_of_item(item, shop)
total_item_count = data_list[0]
total_price = data_list[1]

if total_item_count:
    print('Количество деталей:', total_item_count)
    print('Общая стоимость:', total_price)
else:
    print('Такой детали в магазине нет.')
