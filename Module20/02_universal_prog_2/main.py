def eratosthenes_sieve(number):
    prime_numbers_list = []
    sieve = set(range(2, number + 1))

    while sieve:
        prime_number = min(sieve)
        prime_numbers_list.append(prime_number)
        sieve -= set(range(prime_number, number + 1, prime_number))

    return prime_numbers_list


def is_prime(source_number):
    if source_number == 0 or source_number == 1:
        return False
    else:
        list_of_prime_numbers = eratosthenes_sieve(source_number)
        if source_number in list_of_prime_numbers:
            return True
        else:
            return False


def crypto(source_object):
    return [element for index, element in enumerate(source_object)
            if is_prime(index)]


# Tests:
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(crypto('О Дивный Новый мир!'))
# print(crypto((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
# print(crypto({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))
# print(crypto({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
