from elements import Water, Air, Fire, Earth, Metal


def check_object(initial_object):
    if initial_object:
        print(initial_object.name)
    else:
        print(initial_object)


# Tests:
water = Water()
air = Air()
fire = Fire()
earth = Earth()
metal = Metal()

# Проверяем соединение базовых элементов:
check_object(water + air)
check_object(water + fire)
check_object(water + earth)
check_object(air + fire)
check_object(air + earth)
check_object(fire + earth)
print()

# Проверяем соединение собственного элемента с другими:
check_object(metal + fire)
check_object(metal + water)
molten_metal = metal + fire
check_object(molten_metal + water)
