file_name = input('Введите название файла: ')
forbidden_symbols = ("@", "№", "$", "%", "^", "&", "\\", "*", "(", ")")
correct_extensions = (".docx", ".txt")

if file_name.startswith(forbidden_symbols):
    print('\nОшибка: название начинается на один из специальных символов.')
elif not file_name.endswith(correct_extensions):
    print('\nОшибка: неверное расширение файла. Ожидается .docx или .txt.')
else:
    print('\nФайл назван верно.')
