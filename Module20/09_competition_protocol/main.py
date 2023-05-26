def generate_protocol(quantity):
    result_protocol = []

    print('Введите записи (результат и имя через пробел):')
    for index in range(quantity):
        points, player = input(f'{index + 1}-я запись: ').split()
        result_protocol.append((int(points), player, index))

    return result_protocol


def get_standing(source_protocol):
    final_results = [element for element in source_protocol]
    length = len(final_results)

    # Sort results by points:
    for i_index in range(length):
        for j_index in range(i_index, length):

            if final_results[j_index][0] > final_results[i_index][0]:
                final_results[j_index], final_results[i_index] = (
                    final_results[i_index], final_results[j_index]
                )

    # Sort results by time (who first shown same result):
    for i_index in range(length):
        for j_index in range(i_index, length):

            if final_results[j_index][0] == final_results[i_index][0] and \
                                            final_results[j_index][2] < final_results[i_index][2]:
                final_results[j_index], final_results[i_index] = (
                    final_results[i_index], final_results[j_index]
                )

    return final_results


def show_standing(results):
    shown_players = []
    place = 1
    index = 0

    print('\nИтоги соревнований:')
    while place < 4:
        total_points, name = results[index][0], results[index][1]

        if name not in shown_players:
            print('{}-е место: {} ({})'.format(
                place,
                name,
                total_points
            ))
            place += 1
            shown_players.append(name)

        index += 1


records_quantity = int(input('Введите количество записей в протоколе: '))
protocol = generate_protocol(records_quantity)
tournament_standing = get_standing(protocol)
show_standing(tournament_standing)
