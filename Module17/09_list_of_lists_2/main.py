nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

answer = [number for dimension_2 in nice_list
          for dimension_1 in dimension_2
          for number in dimension_1]

print('Ответ:', answer)
