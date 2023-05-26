list_length = int(input('Введите длину списка: '))
result_list = [1 if index % 2 == 0 else index % 5
               for index in range(list_length)]
print(result_list)
