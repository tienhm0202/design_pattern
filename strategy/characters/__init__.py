"""Define all characters class here"""
from strategy.weapon import Knife, Weapon, Axe, BowAndArrow, Sword


class Characters(object):
    """Common characters class"""

    def __init__(self, weapon: Weapon, health: int):
        self.weapon = weapon
        self.health = health
        self.attack = 0

    def fight(self):
        return self.health * self.attack / int(self.weapon.speed())


class Assassin(Characters):
    def __init__(self, weapon):
        self.perfect_weapon = Knife
        super(Assassin, self).__init__(weapon, health=10)

    def fight(self):
        self.attack = self.weapon.attack()
        if isinstance(self.weapon, self.perfect_weapon):
            self.attack += 3

        return super(Assassin, self).fight()


class Fighter(Characters):
    def __init__(self, weapon):
        self.perfect_weapon = Axe
        super(Fighter, self).__init__(weapon, health=15)

    def fight(self):
        self.attack = self.weapon.attack()
        if isinstance(self.weapon, self.perfect_weapon):
            self.attack += 2

        return super(Fighter, self).fight()


class Ranger(Characters):
    def __init__(self, weapon):
        self.perfect_weapon = BowAndArrow
        super(Ranger, self).__init__(weapon, health=8)

    def fight(self):
        self.attack = self.weapon.attack()
        if isinstance(self.weapon, self.perfect_weapon):
            self.attack += 4

        return super(Ranger, self).fight()


class Paladin(Characters):
    def __init__(self, weapon):
        self.perfect_weapon = Sword
        super(Paladin, self).__init__(weapon, health=13)

    def fight(self):
        self.attack = self.weapon.attack()
        if isinstance(self.weapon, self.perfect_weapon):
            self.attack += 2

        return super(Paladin, self).fight()
