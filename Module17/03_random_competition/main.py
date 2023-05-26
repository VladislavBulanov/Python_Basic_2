import random

def list_of_participants_points():
    result_list = [round(random.uniform(5, 10), 2) for _ in range(20)]
    return result_list


def find_winner(player_1, player_2):
    winners_list = [player_1[member] if player_1[member] > player_2[member]
                    else player_2[member] for member in range(len(player_1))]
    return winners_list


first_team = list_of_participants_points()
second_team = list_of_participants_points()
print('Очки первой команды:', first_team)
print('Очки второй команды:', second_team)
print('Победители тура:', find_winner(first_team, second_team))
