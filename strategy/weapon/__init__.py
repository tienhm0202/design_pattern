"""Define all weapons here"""


class Weapon(object):
    """Weapon common class"""

    def attack(self):
        """How hard this weapon can damage. From 1 to 5. 5 is hardest"""
        raise NotImplementedError

    def speed(self):
        """
        How many turn for this weapon can attack. From 1 to 5. 1 is fastest.
        """
        raise NotImplementedError


class Knife(Weapon):
    def attack(self):
        return 3  # 5 damages

    def speed(self):
        return 2


class BowAndArrow(Weapon):
    def attack(self):
        return 2

    def speed(self):
        return 1


class Axe(Weapon):
    def attack(self):
        return 4

    def speed(self):
        return 5


class Sword(Weapon):
    def attack(self):
        return 4

    def speed(self):
        return 4
