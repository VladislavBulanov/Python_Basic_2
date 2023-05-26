import requests
import json
from typing import List


def get_starship_data(url: str) -> dict:
    """
    The function parses starship's url and
    renders dictionary of data with specified keys.
    :param url: source url of starship on 'swapi.dev'
    """
    source_data = json.loads(requests.get(url).text)
    result_data = dict()
    for key, value in source_data.items():
        if key in ('name', 'max_atmosphering_speed', 'starship_class', 'pilots'):
            result_data[key] = value
    return result_data


def get_pilot_data(url: str) -> dict:
    """
    The function parses pilot's url and
    renders dictionary of data with specified keys.
    :param url: source url of pilot on 'swapi.dev'
    """
    source_data = json.loads(requests.get(url).text)
    result_data = dict()
    for key, value in source_data.items():
        if key in ('name', 'height', 'mass'):
            result_data[key] = value
        elif key == 'homeworld':
            result_data['homeworld'] = json.loads(requests.get(value).text)['name']
            result_data['homeworld_url'] = value
    return result_data


if __name__ == '__main__':
    starship_data = get_starship_data(url='https://swapi.dev/api/starships/10/')
    pilots_urls_list: List[str] = starship_data['pilots']
    pilots_info = []
    for pilot_url in pilots_urls_list:
        current_pilot = get_pilot_data(url=pilot_url)
        pilots_info.append(current_pilot)
    starship_data['pilots'] = pilots_info

    with open('millennium_falcon.json', 'w', encoding='utf-8') as file:
        json.dump(starship_data, file, indent=4)

    print(starship_data)
