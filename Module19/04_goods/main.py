def generate_goods_information(goods_info, store_info):
    result_information = []

    for key, value in goods_info.items():
        total_quantity = 0
        total_price = 0

        for record in store_info[value]:
            total_quantity += record['quantity']
            total_price += record['quantity'] * record['price']

        result_information.append([key, total_quantity, total_price])

    return result_information


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

goods_information = generate_goods_information(goods, store)
for item in goods_information:
    print('{article} - {quantity} штук(и), стоимость {total_amount:,d} руб.'.format(
        article = item[0],
        quantity = item[1],
        total_amount = item[2]
    ))
