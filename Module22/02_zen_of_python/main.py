import os

def backward_order_of_strings(source_path):
    """
    :param source_path: path to data file
    :returns: strings in backward order from data file
    :rtype: str
    """
    data_file = open(source_path, 'r')
    result_list = []

    for line in data_file:
        if not line.endswith('\n'):
            line += '\n'
        result_list.insert(0, line)

    data_file.close()
    return ''.join(result_list)


path = os.path.abspath('zen.txt')
print(backward_order_of_strings(path))
