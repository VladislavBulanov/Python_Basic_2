def calculating_math_func(data, factorial={0: 1}):
    """
    :param data: source number to calculate function value
    :type: int
    :param factorial: cache of calculated factorial values (number: factorial)
    :type: dict
    :returns: function result
    :rtype: float
    """

    if data in factorial:
        result = factorial.get(data)
        result /= data ** 3
        result = result ** 10
        return result

    else:
        for number in range(max(factorial) + 1, data + 1):
            result = factorial.get(max(factorial))
            result *= number
            factorial.update({number: result})
        return calculating_math_func(data)


input_number = int(input('Введите число: '))
function_result = calculating_math_func(input_number)
print(f'Результат вычисления функции равен {function_result}.')
