from re import findall, DOTALL
from typing import List
import requests


def get_tag_content(tag: str, data: str) -> List[str]:
    """
    The function returns list of contents of specified HTML-tag.
    :param tag: HTML-tag
    :param data: source HTML-code
    """
    pattern = fr'<{tag}>(.*?)</{tag}>'
    return findall(pattern, data, flags=DOTALL)


if __name__ == '__main__':
    # Test 1:
    with open('examples.html', 'r') as file:
        text = file.read()
    print(get_tag_content('h3', text))

    # Test 2:
    response = requests.get('https://skillbox.ru/')
    if response.status_code == 200:
        print(get_tag_content('h3', response.text))
