from os import walk, path
from typing import List


def generate_files_paths(
        root_directory_path: str = '/',
        target_directory: str = ''
) -> List[str]:
    """
    Recursively generate paths of all files
    in a directory and its subdirectories.
    :param root_directory_path: root directory to start the search from
    :param target_directory: directory name to find files in
    :return: list of file paths
    """
    files_list = []

    for dir_path, dir_names, filenames in walk(root_directory_path):
        for filename in filenames:
            if target_directory in dir_path:
                files_list.append(path.join(dir_path, filename))

    return files_list


target_catalogue = 'Module26'
files_paths = generate_files_paths(target_directory=target_catalogue)
if files_paths:
    print('Пути всех файлов каталога {directory}:'.format(
        directory=target_catalogue
    ))
    for path in files_paths:
        print(path)
else:
    print('Такого каталога в указанной директории не существует.')
