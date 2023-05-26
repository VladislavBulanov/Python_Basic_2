import copy
import json

def get_site(structure, sites_data, count=0):
    if count == 0:
        return

    product = input('\nВведите название продукта для нового сайта: ')
    result_structure = copy.deepcopy(structure)
    result_structure['html']['head']['title'] = result_structure['html']['head'] \
                                                ['title'].format(name=product)
    result_structure['html']['body']['h2'] = result_structure['html']['body'] \
                                             ['h2'].format(name=product)
    sites_data[product] = result_structure

    for brand, site in sites_data.items():
        print(f'\nСайт для {brand}:\nsite = ', end='')
        print(json.dumps(site, indent=4, ensure_ascii=False))  # Это если нужен вывод в точности,
                                                               # как в условии. Другого способа не нашёл.
    get_site(site_structure, active_sites_data, count - 1)


site_structure = {
    'html': {
        'head': {
            'title': 'Куплю/продам {name} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {name}',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
active_sites_data = dict()
sites_quantity = int(input('Сколько необходимо сделать сайтов: '))
get_site(site_structure, active_sites_data, sites_quantity)
