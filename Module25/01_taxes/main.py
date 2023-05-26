from properties import Apartment, Car, CountryHouse


def calculate_total_tax(
        apartment_worth: float,
        car_worth: float,
        house_worth: float
) -> float:
    """
    :return: total tax of human properties
    """
    apartment = Apartment(apartment_worth)
    car = Car(car_worth)
    house = CountryHouse(house_worth)
    sum_of_tax = (
            apartment.calculate_tax() + car.calculate_tax() +
            house.calculate_tax()
    )
    return sum_of_tax


def main():
    """
    Main program collecting information about human properties and
    running function to calculate total tax.
    Then displays whether you have enough of your money to pay off
    the taxes or not.
    """
    total_money = float(input('Введите количество Ваших денег: '))
    apartment_cost = float(input('Введите стоимость Вашей квартиры: '))
    car_cost = float(input('Введите стоимость Вашей машины: '))
    house_cost = float(input('Введите стоимость Вашего дома: '))
    total_tax = calculate_total_tax(
        apartment_worth=apartment_cost,
        car_worth=car_cost,
        house_worth=house_cost
    )

    print('\nСуммарный налог на Ваше имущество: {:,.2f}'.format(total_tax))
    if total_money >= total_tax:
        print('Ваших денег достаточно, чтобы погасить все налоги.')
    else:
        print('Для погашения всех налогов вам не хватает {:,.2f}'.format(
            total_tax - total_money
        ))


if __name__ == '__main__':
    main()
