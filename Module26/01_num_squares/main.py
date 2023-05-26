from collections.abc import Iterable


# # Класс-итератор:
# class SequenceOfSquares:
#     """
#     Class creates iterator of sequence of numbers' squares."""
#     def __init__(
#         self,
#         limit: int,
#         start_number: int = 1,
#         step: int = 1
#     ) -> None:
#         """
#         Class constructor.
#         :param limit: the last number of sequence (inclusive)
#         :param start_number: the start number of sequence
#         :param self: step of sequence
#         """
#         self.__start_number = start_number
#         self.__last_number = limit
#         self.__step = step
#
#     def __iter__(self):
#         self.__current_value = self.__start_number - self.__step
#         return self
#
#     def __next__(self):
#         self.__current_value += self.__step
#         if self.__current_value <= self.__last_number:
#             return self.__current_value ** 2
#         else:
#             raise StopIteration
#
#
# initial_limit = int(input('Введите целое положительное число: '))
# sequence_of_squares_generator = SequenceOfSquares(limit=initial_limit)
# for square in sequence_of_squares_generator:
#     print(square, end=' ')
# print()
# # Для проверки обновления итератора:
# for square in sequence_of_squares_generator:
#     print(square, end=' ')


# # Функция-генератор:
# def generate_sequence_of_squares(limit: int) -> Iterable[int]:
#     """
#     This function generate sequence of numbers' squares.
#     :param limit: length of numbers' sequence
#     """
#     for number in range(1, limit + 1):
#         yield number ** 2
#
#
# initial_limit = int(input('Введите целое положительное число: '))
# sequence_of_squares_generator = generate_sequence_of_squares(initial_limit)
# print(*sequence_of_squares_generator)


# # Генераторное выражение:
# limit = int(input('Введите целое положительное число: '))
# print(*(number ** 2 for number in range(1, limit + 1)))
