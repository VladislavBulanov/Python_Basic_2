def joint_list_of_information(source_information):
    """
    :param source_information: source data with names and points of each player
    :type: dict
    :returns: joint list of players' information
    :rtype: list[tuple]
    """
    return [player + points for player, points in source_information.items()]


players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

print(joint_list_of_information(players))
