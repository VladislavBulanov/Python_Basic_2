from json import load, dump
from typing import Union, Optional, List


def get_data_from_json_file(filename: str) -> Optional[dict]:
    """
    The function returns dictionary with data from specified JSON-file.
    :param filename: name of JSON-file
    """
    try:
        with open(f'{filename}.json', 'r', encoding='utf-8') as f:
            return load(f)
    except FileNotFoundError:
        print('Указанный файл не найден.')


def find_value_by_key(
        initial_dictionary: dict, target_key: Union[str, int, float]
) -> Optional[dict]:
    """
    The function finds value by source key.
    :param initial_dictionary: source dictionary
    :param target_key: source key for find value
    :return: function returns value by specified key if source key is in
    dictionary. Function returns None if key isn't in dictionary.
    """
    def recursive_search(
            dictionary: dict, target: Union[str, int, float]
    ) -> Optional[dict]:
        """
        The function for recursive search value by specified key.
        :param dictionary: source dictionary
        :param target: source key for find value
        """
        for key, value in dictionary.items():
            if key == target:
                return value
            elif isinstance(value, dict):
                search_result = recursive_search(value, target)
                if search_result is not None:
                    return search_result

    result = recursive_search(initial_dictionary, target_key)
    return result


def compare_json_data(data_1: dict, data_2: dict, keys_for_search: List[str]) -> dict:
    """
    The function receives two dictionaries with data from two JSON-files and
    compares them by keys that is specified in 'keys_for_search' list.
    :param data_1: first data from JSON-file
    :param data_2: second data from JSON-file
    :param keys_for_search: list of keys by which differences will be searched
    :return: the dictionary with differences in two datas. If there are no
    differences the function returns empty dictionary
    """
    result_dictionary = dict()
    for key in keys_for_search:
        old_value = find_value_by_key(data_1, key)
        new_value = find_value_by_key(data_2, key)
        if old_value != new_value:
            result_dictionary[key] = new_value
    return result_dictionary


if __name__ == '__main__':
    old_data = get_data_from_json_file('json_old')
    new_data = get_data_from_json_file('json_new')
    keys_for_search_differences: List[str] = ['services', 'staff', 'datetime']
    result = compare_json_data(old_data, new_data, keys_for_search_differences)
    print(result)
    with open('result.json', 'w', encoding='utf-8') as file:
        dump(result, file, indent=4)
