def get_two_sex_surnames(source_surname):
    if source_surname[-1] == 'а':
        women_surname = source_surname
        men_surname = source_surname[:-1]
    elif source_surname[-2:] == 'ой' or source_surname[-2:] == 'ый':
        women_surname = source_surname[:-2] + 'ая'
        men_surname = source_surname
    elif source_surname[-2:] == 'ая':
        women_surname = source_surname
        men_surname = source_surname[:-2] + 'ой'
        # Вообще тут может быть и '-ый' (Чёрная-Чёрный),
        # но я не знаю, как это прописать.
    else:
        women_surname = source_surname + 'а'
        men_surname = source_surname

    return women_surname, men_surname


def find_family_information(source_data, initial_surname):
    surnames = get_two_sex_surnames(initial_surname)

    return {surname_name: age for surname_name, age in source_data.items()
            if surname_name[0].lower() in surnames}


information = {
    ('Петров', 'Александр'): 10,
    ('Петрова', 'Мария'): 20,
    ('Петров', 'Алексей'): 30,
    ('Иванова', 'Екатерина'): 20,
    ('Иванов', 'Пётр'): 30,
    ('Иванова', 'Дарья'): 40,
    ('Донской', 'Евгений'): 15,
    ('Донская', 'Ирина'): 25
}

inputted_surname = input('Введите фамилию: ').lower()
family_information = find_family_information(information, inputted_surname)

if family_information:
    print()
    for key, value in family_information.items():
        print(*key, value)
else:
    print('\nЧеловека с такой фамилией нет в базе данных.')
