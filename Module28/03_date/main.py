from typing import Tuple, Optional


class Date:
    def __init__(self) -> None:
        """Class constructor."""
        self.__day = 0
        self.__month = 0
        self.__year = 0

    def __str__(self) -> str:
        """Returns result date."""
        result_date = 'День: {day}\t\tМесяц: {month}\t\tГод: {year}'.format(
            day=self.__day,
            month=self.__month,
            year=self.__year,
        )
        return result_date

    @classmethod
    def parse_date_string(cls, date_string: str) -> Tuple[int]:
        """
        Parses source date string at three number: day, month and year.
        :param date_string: source string with date
        """
        return tuple(map(int, date_string.split('-')))

    @classmethod
    def is_date_valid(cls, src_date: str) -> bool:
        """
        Method checks whether the date in the source string is correct.
        :param src_date: source string describing date
        """
        try:
            result_date: Tuple[int] = cls.parse_date_string(src_date)
            return 0 < result_date[0] < 32 and 0 < result_date[1] < 13
        except Exception:
            return False

    @classmethod
    def from_string(cls, src_date: str) -> Optional['Date']:
        """
        Creates instance of 'Date' class if date string is valid.
        :param src_date: source string with date
        """
        if cls.is_date_valid(src_date):
            result_date = cls.parse_date_string(src_date)
            new_instance = cls()
            new_instance.__day = result_date[0]
            new_instance.__month = result_date[1]
            new_instance.__year = result_date[2]
            return new_instance
        print('Некорректный формат даты.')


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
