class Student:

    def __init__(self, name: str, group_number: str, performance: list):
        self.name = name
        self.group_number = group_number
        self.performance = performance

    def get_average_grade(self):
        amount = sum(self.performance)
        quantity = len(self.performance)
        return amount / quantity

    def show_info(self):
        print(
            f'\nФамилия Имя: {self.name}'
            f'\nНомер группы: {self.group_number}'
            f'\nСредний балл: {round(self.get_average_grade(), 1)}\n'
        )


def generate_students_list(quantity):
    students = []
    for index in range(quantity):
        print(f'\nВведите данные {index + 1}-го студента:')
        students_name = input('\tФамилия Имя: ')
        students_group = input('\tНомер группы: ')
        students_performance = [
            int(mark) for mark in input('\tОценки через пробел: ').split()
        ]
        students.append(Student(
            students_name,
            students_group,
            students_performance
        ))
    return students


def show_students_list(source_list):
    print('\n\n=====СПИСОК СТУДЕНТОВ=====\n')
    for student in source_list:
        student.show_info()


students_list = generate_students_list(3)
sorted_students_list = sorted(students_list, key=Student.get_average_grade)
show_students_list(sorted_students_list)
