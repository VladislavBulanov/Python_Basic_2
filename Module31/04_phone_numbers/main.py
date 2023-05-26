import re


def validate_number(src_number: str) -> bool:
    """
    The function checks whether source number is valid.
    :param src_number: source phone number
    """
    pattern = r'\b[89]\d{9}'
    matches = re.findall(pattern, src_number)
    return len(matches) > 0


if __name__ == '__main__':
    numbers_list = ['9999999999', '999999-999', '99999x9999']
    for index, number in enumerate(numbers_list, 1):
        is_valid = validate_number(number)
        print('{index}-й номер: {result}'.format(
            index=index,
            result='всё в порядке' if is_valid else 'не подходит',
        ))
