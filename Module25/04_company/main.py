from company import Manager, Agent, Worker


def generate_employees():
    employees = [
        Manager('Иван', 'Иванов', 20),
        Manager('Пётр', 'Петров', 21),
        Manager('Андрей', 'Сидоров', 22),
        Agent('Антон', 'Козлов', 23, 100000),
        Agent('Юрий', 'Скворцов', 24, 200000),
        Agent('Александр', 'Миньков', 25, 300000),
        Worker('Михаил', 'Чижов', 26, 150),
        Worker('Артём', 'Варлахин', 27, 160),
        Worker('Алексей', 'Ломакин', 28, 170)
    ]

    for employee in employees:
        employee.show_employee_info()


if __name__ == '__main__':
    generate_employees()
