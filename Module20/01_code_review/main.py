def get_id_and_ages_list(students_info):
    return [(current_key, current_value['age']) for current_key, current_value
            in students_info.items() if 'age' in current_value]


def get_interests_and_surnames_length(students_data):
    interests = []
    surnames_length = 0

    for key, value in students_data.items():
        if 'interests' in value:
            interests += students_data[key]['interests']

        if 'surname' in value:
            surnames_length += len(students_data[key]['surname'])

    return set(interests), surnames_length


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

id_and_ages_list = get_id_and_ages_list(students)
interests_and_surnames_length = get_interests_and_surnames_length(students)
students_interests = interests_and_surnames_length[0]
sum_length_of_surnames = interests_and_surnames_length[1]

print('Список пар "ID студента — возраст":', id_and_ages_list)
print('Полный список интересов всех студентов:', students_interests)
print('Общая длина всех фамилий студентов:', sum_length_of_surnames)
