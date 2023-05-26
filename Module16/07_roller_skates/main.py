skates_size = []
human_foot_size = []
fits_quantity = 0

roller_skates_quantity = int(input('Введите количество пар коньков: '))
for index in range(roller_skates_quantity):
    size = int(input(f'Размер {index + 1}-й пары: '))
    skates_size.append(size)

human_quantity = int(input('\nВведите количество людей: '))
for index in range(human_quantity):
    foot_size = int(input(f'Размер ноги {index + 1}-го человека: '))
    human_foot_size.append(foot_size)

# Сортируем списки по возрастанию, чтобы при подборе
# не забрать излишне большой размер и тем самым не отнять
# этот размер у более маленькой подходящей ноги:
skates_size.sort()
human_foot_size.sort()

for human in human_foot_size:
    for skates in skates_size:
        if skates >= human:
            fits_quantity += 1
            skates_size.remove(skates)
            break

print('\nНаибольшее количество людей, которые смогут взять ролики:', fits_quantity)
