class File:
    """The custom file's context manager."""
    def __init__(self, filename: str, mode: str) -> None:
        """
        Class constructor.
        :param filename: name of opening file
        :param mode: mode of the opening
        """
        self.__filename = filename
        self.__mode = mode
        self.__file = None

    def __enter__(self):
        self.__file = open(self.__filename, self.__mode)
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()
        if isinstance(exc_type, (FileExistsError, FileNotFoundError)):
            return True


if __name__ == '__main__':
    with File('example.txt', 'w') as file:
        file.write('Hello World!')
