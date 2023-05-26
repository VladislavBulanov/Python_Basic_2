"""Module of classes describing company's employees."""


class Person:
    """Main class describing name, surname and age of human."""
    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_info(self):
        """
        Person's information getter.
        :return: name, surname, age
        :rtype: tuple
        """
        return self.__name, self.__surname, self.__age


class Employee(Person):
    """Subclass of class 'Person'."""
    __fix_salary = 0

    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname, age)

    def get_salary(self):
        """
        Employee's salary getter.
        :rtype: float
        """
        return self.__fix_salary


    def show_employee_info(self):
        """
        Displays full information about employee:
        position, name, surname, age and salary.
        """
        name, surname, age = super().get_info()
        salary = self.get_salary()
        print(
            '\nИНФОРМАЦИЯ О СОТРУДНИКЕ\n'
            'Имя: {}\nФамилия: {}\nВозраст: {}\n'
            'Должность: {}\nЗарплата: {:,.2f}'.format(
                name, surname, age, self, salary
            )
        )


class Manager(Employee):
    """Subclass of class 'Employee' describing manager position."""
    __fix_salary = 13000

    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname, age)

    def __str__(self):
        return 'менеджер'

    def get_salary(self):
        """
        Manager's salary getter.
        :rtype: float
        """
        return self.__fix_salary


class Agent(Employee):
    """Subclass of class 'Employee' describing agent position."""
    __fix_salary = 5000
    __percent_by_sales = 0.05

    def __init__(self, name: str, surname: str, age: int, total_sold: float):
        super().__init__(name, surname, age)
        self.__total_sold = total_sold

    def __str__(self):
        return 'агент'

    def get_salary(self):
        """
        Agent's salary getter.
        :rtype: float
        """
        return self.__fix_salary + self.__total_sold * self.__percent_by_sales


class Worker(Employee):
    """Subclass of class 'Employee' describing worker position."""
    __hour_cost = 100

    def __init__(self, name: str, surname: str, age: int, hours_worked: float):
        super().__init__(name, surname, age)
        self.__hours_worked = hours_worked

    def __str__(self):
        return 'рабочий'

    def get_salary(self):
        """
        Worker's salary getter.
        :rtype: float
        """
        return self.__hour_cost * self.__hours_worked
