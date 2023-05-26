from typing import Optional, Any
from collections.abc import Iterable


class Node:
    """
    The class describing the node of linked list.
    """
    def __init__(
            self,
            value: Optional[Any] = None,
            next_node: Optional['Node'] = None
    ) -> None:
        """
        Class constructor.
        :param value: value of node
        :param next_node: next node in linked list
        """
        self.__value = value
        self.__next_node = next_node

    def get_value(self) -> Optional[Any]:
        """Getter of value."""
        return self.__value

    def set_value(self, value: Optional[Any]) -> None:
        """
        Setter of value.
        :param value: value of node
        """
        self.__value = value

    def get_next_node(self) -> Optional[Any]:
        """Getter of next node."""
        return self.__next_node

    def set_next_node(self, next_node: Optional[Any]) -> None:
        """Setter of next node."""
        self.__next_node = next_node


class LinkedList:
    """
    The class describing the linked list consisting of nodes of 'Node' class.
    """
    def __init__(
            self,
            head: Optional[Node] = None,
            tail: Optional[Node] = None,
    ) -> None:
        """
        Class constructor.
        :param head: the head node of linked list
        :param tail: the last node of linked list
        """
        self.__head = head
        self.__tail = tail
        self.__length = 0

    def __str__(self) -> str:
        """
        :return: linked list in string format
        """
        current_node = self.__head
        output = '['
        while current_node is not None:
            output += str(current_node.get_value())
            current_node = current_node.get_next_node()
            if current_node is not None:
                output += ' '
        output += ']'
        return output

    def get_head(self) -> Optional[Node]:
        """Getter of head node."""
        return self.__head

    def set_head(self, node: Optional[Node]) -> None:
        """Setter of head node."""
        self.__head = node

    def get_tail(self) -> Optional[Node]:
        """Getter of tail node."""
        return self.__tail

    def set_tail(self, node: Optional[Node]) -> None:
        """Setter of tail node."""
        self.__tail = node

    def append(self, value: Optional[Any]) -> None:
        """
        Appends node in the end of linked list.
        :param value: the value of new node
        """
        new_node = Node(value)
        if self.__head is None:
            self.set_head(new_node)
            self.set_tail(new_node)
        else:
            self.__tail.set_next_node(new_node)
            self.set_tail(new_node)
        self.__length += 1

    def get(self, index: int) -> Optional[Any]:
        """
        Get value of node by index.
        :param index: the index of node in linked list
        """
        if index not in range(self.__length):
            raise IndexError('Index out of range')
        current_node = self.__head
        for _ in range(index):
            current_node = current_node.get_next_node()
        return current_node.get_value()

    def remove(self, index: int) -> None:
        """
        Delete node by index.
        :param index: the index of node in linked list
        """
        if index not in range(self.__length):
            raise IndexError('Index out of range')
        if index == 0:
            self.set_head(self.get_head().get_next_node())
            if self.__head is None:
                self.set_tail(None)
        else:
            current_node = self.__head
            for _ in range(index - 1):
                current_node = current_node.get_next_node()
            current_node.set_next_node(current_node.get_next_node().get_next_node())
            if current_node.get_next_node() is None:
                self.set_tail(current_node)
        self.__length -= 1

    def __iter__(self) -> Iterable[Optional[Any]]:
        """Iterator."""
        current_node = self.get_head()
        while current_node is not None:
            yield current_node.get_value()
            current_node = current_node.get_next_node()


def test_creating_linked_list() -> None:
    """Create and test the linked list of 'LinkedList' class."""
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    print('Текущий список: {}'.format(linked_list))
    print('Получение третьего элемента: {}'.format(linked_list.get(2)))
    print('Удаляем второго элемент.')
    linked_list.remove(1)
    print('Новый список: {}'.format(linked_list))


if __name__ == '__main__':
    test_creating_linked_list()
