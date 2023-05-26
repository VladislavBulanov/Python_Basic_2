import os

def get_folder_statistics(source_path):
    result_statistics = {
        'folder_size': 0,
        'sub_folders_quantity': 0,
        'files_quantity': 0
    }

    if os.path.exists(source_path):
        for element in os.listdir(source_path):
            current_path = os.path.join(source_path, element)

            if os.path.isfile(current_path):
                result_statistics['folder_size'] += os.path.getsize(current_path)
                result_statistics['files_quantity'] += 1
            else:
                result_statistics['sub_folders_quantity'] += 1
                sub_folders_statistics = get_folder_statistics(current_path)

                result_statistics['folder_size'] += \
                    sub_folders_statistics['folder_size']
                result_statistics['sub_folders_quantity'] += \
                    sub_folders_statistics['sub_folders_quantity']
                result_statistics['files_quantity'] += \
                    sub_folders_statistics['files_quantity']

        return result_statistics

    else:
        print('Каталога по указанному пути не существует.')


path = os.path.abspath(os.path.join('..', '..', 'Module14'))
folder_statistics = get_folder_statistics(path)
if folder_statistics:
    print('Искомый путь:', path)
    print('Размер каталога (в Кб):', round(folder_statistics['folder_size'] / 1024, 1))
    print('Количество подкаталогов:', folder_statistics['sub_folders_quantity'])
    print('Количество файлов:', folder_statistics['files_quantity'])
