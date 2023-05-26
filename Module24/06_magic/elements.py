class Water:
    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None


class Earth:
    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:
    def __init__(self):
        self.name = 'Шторм'


class Steam:
    def __init__(self):
        self.name = 'Пар'


class Dirt:
    def __init__(self):
        self.name = 'Грязь'


class Lightning:
    def __init__(self):
        self.name = 'Молния'


class Dust:
    def __init__(self):
        self.name = 'Пыль'


class Lava:
    def __init__(self):
        self.name = 'Лава'


# Собственные элементы:
class Metal:
    def __init__(self):
        self.name = 'Металл'

    def __add__(self, other):
        if isinstance(other, Fire):
            return MoltenMetal()
        else:
            return None


class MoltenMetal:
    def __init__(self):
        self.name = 'Расплавленный металл'

    def __add__(self, other):
        if isinstance(other, Water):
            return SolidMetal()
        else:
            return None


class SolidMetal:
    def __init__(self):
        self.name = 'Твёрдый металл'
