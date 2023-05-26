class MyDict(dict):
    """Subclass of built-in class 'dict' with changed 'get' method."""
    def get(self, key, default=0):
        """Get value by key. If key doesn't exist return 0."""
        return super().get(key, default)

    def show_dictionary(self):
        """Show current data in format 'key: value'."""
        for key, value in self.items():
            print('{}: {}'.format(key, value))


# # Tests:
# dictionary = MyDict({'a': 5, 'b': 10})
# print(dictionary.get('a'))  # key exists
# print(dictionary.get('c'))  # key doesn't exist
# print(dictionary.get('c', 1))  # key doesn't exist with returned value 1
# print()
# dictionary.show_dictionary()
