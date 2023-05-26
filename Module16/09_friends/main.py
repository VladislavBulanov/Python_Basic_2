friends_quantity = int(input('Введите количество друзей: '))
friends_balance = [0] * friends_quantity
# IOU - I owe you - долговая расписка:
iou_quantity = int(input('Введите количество долговых расписок: '))

for iou in range(iou_quantity):
    print(f'\n{iou + 1}-Я РАСПИСКА')
    debtor = int(input('Должник (кому): '))
    lender = int(input('Заимодатель (от кого): '))
    debt_amount = int(input('Сумма долга: '))

    friends_balance[debtor - 1] -= debt_amount
    friends_balance[lender - 1] += debt_amount

print('\nБАЛАНС ДРУЗЕЙ')
for number, friend in enumerate(friends_balance):
    print(f'{number + 1}-й друг: {friend}')
