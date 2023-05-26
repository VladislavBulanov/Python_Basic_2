class Stack:
    """The class describing stack of something."""
    def __init__(self):
        """Class constructor."""
        self.__stack = []

    def __str__(self):
        """
        :return: current stack
        :rtype: str
        """
        return '; '.join(self.__stack)

    def get_stack_elements(self):
        """
        :return: list of stack elements
        :rtype: list
        """
        return self.__stack

    def get_stack_size(self):
        """
        :return: quantity of elements in stack
        :rtype: int
        """
        return len(self.__stack)

    def add_element(self, element):
        """Add element in stack."""
        self.__stack.append(element)

    def remove_element(self):
        """Remove last element from stack if stack is not empty."""
        if self.__stack:
            self.__stack.pop()
        else:
            print('Стек сейчас пуст.')


class TaskManager:
    """
    The class describing task manager (type dictionary).
    Every task has priority (key of dictionary). Tasks
    (value of dictionary) are 'Stack' class.
    """
    def __init__(self):
        """Class constructor."""
        self.__tasks = dict()

    def __str__(self):
        """
        :return: current tasks sorted by priority
        :rtype: str
        """
        result_dictionary = ['ЗАДАЧИ:\n']
        if self.__tasks:
            for priority in sorted(self.__tasks.keys()):
                result_dictionary.append('{priority}: {task}\n'.format(
                    priority=priority,
                    task=self.__tasks[priority]
                ))
        return ''.join(result_dictionary)

    def new_task(self, task: str, priority: int):
        """
        Add new task to stack of the specified priority.
        Check if this task exists in stack with specified priority.
        """
        if priority not in self.__tasks:
            self.__tasks[priority] = Stack()
            self.__tasks[priority].add_element(task)
        elif task in self.__tasks[priority].get_stack_elements():
            print(f'Задача "{task}" уже есть в стеке с таким приоритетом.\n')
        else:
            self.__tasks[priority].add_element(task)

    def delete_task(self, task: str):
        """
        Delete task from stack if it exists, and it's last element in stack.
        :param task: task which we want to delete
        :type task: str
        """
        for priority, stack in self.__tasks.items():
            if stack.get_stack_size() != 0 and \
                    stack.get_stack_elements()[-1] == task:

                stack.remove_element()
                print(f'Задача "{task}" успешно удалена.\n')
                if stack.get_stack_size() == 0:
                    self.__tasks.pop(priority)
                break
        else:
            print(f'Задача "{task}" не последняя в стеке или её не существует.\n')


def start_testing():
    """Create the task manager and test his working."""
    manager = TaskManager()

    # Testing the adding new tasks:
    manager.new_task('сделать уборку', 4)
    manager.new_task('помыть посуду', 4)
    manager.new_task('отдохнуть', 1)
    manager.new_task('поесть', 2)
    manager.new_task('сдать дз', 2)
    print(manager)

    # Testing the deleting tasks:
    manager.delete_task('поесть')  # Task exists but isn't first in stack
    manager.delete_task('сдать дз')  # Task exists and is first in stack
    print(manager)
    manager.delete_task('поесть')  # Task exists and is first in stack
    print(manager)  # Priority '2' has no stack now
    # and was deleted from task manager

    # Try to create same task in stack:
    manager.new_task('сделать уборку', 4)


if __name__ == '__main__':
    start_testing()
