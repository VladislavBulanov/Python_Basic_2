def is_palindrome(initial_string):
    if initial_string == initial_string[::-1]:
        return True
    else:
        return False


def can_become_palindrome(source_string):
    symbols_frequency = dict()
    for symbol in source_string:
        symbols_frequency[symbol] = symbols_frequency.get(symbol, 0) + 1

    odds_quantity = 0
    for value in symbols_frequency.values():
        if value % 2 == 1:
            odds_quantity += 1

    if odds_quantity <= 1:
        return True
    else:
        return False


inputted_string = input('Введите строку: ').lower()

if is_palindrome(inputted_string):
    print('Строка является палиндромом.')
else:
    if can_become_palindrome(inputted_string):
        print('Данную строку можно сделать палиндромом.')
    else:
        print('Данную строку нельзя сделать палиндромом.')
