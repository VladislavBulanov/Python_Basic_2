from typing import List


if __name__ == '__main__':
    letters: List[str] = ['a', 'b', 'c', 'd', 'e']
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

    print(list(map(lambda letter, number: (letter, number), letters, numbers)))
