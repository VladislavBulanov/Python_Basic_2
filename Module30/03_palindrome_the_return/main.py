from collections import Counter


def can_be_poly(string: str) -> bool:
    """
    The function that checks whether a string can be a palindrome.
    Counts quantity of odd chars. If quantity is more than one,
    string can't be a palindrome.
    :param string: source string
    """
    counter = Counter(string)
    total_odd_chars = sum(map(lambda number: number % 2, counter.values()))
    return total_odd_chars <= 1


if __name__ == '__main__':
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))
