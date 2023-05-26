from os import walk, path
from collections.abc import Iterable


def count_lines(root_path: str) -> Iterable[str]:
    """
    Generator for counting strings in python files in specified directory.
    :param root_path: path of root directory which we find python files in
    """
    for foldername, _, filenames in walk(root_path):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = path.join(foldername, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            yield line


if __name__ == '__main__':
    root_directory_path = path.abspath(path.join('..', '03_str_count'))
    lines_count = sum(1 for _ in count_lines(root_directory_path))
    print('Количество строк кода в каталоге {directory}: {count}.'.format(
        directory=root_directory_path,
        count=lines_count
    ))
