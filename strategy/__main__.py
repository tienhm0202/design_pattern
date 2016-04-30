import random

import strategy.characters as c
import strategy.weapon as w

characters = [c.Assassin, c.Fighter, c.Ranger, c.Paladin]
weapons = [w.Axe, w.BowAndArrow, w.Knife, w.Sword]


def get_opponent():
    char = random.choice(characters)
    weapon = random.choice(weapons)

    return char(weapon())


def fight(opp1, opp2):
    type1 = opp1.__class__.__name__
    w1 = opp1.weapon.__class__.__name__

    type2 = opp2.__class__.__name__
    w2 = opp2.weapon.__class__.__name__
    line = """Fight between "%s with %s" and "%s with %s\"""" % (
        type1, w1, type2, w2
    )
    power1 = opp1.fight()
    power2 = opp2.fight()

    oop1_info = "\"%s with %s\" power: %s" % (type1, w1, power1)
    oop2_info = "\"%s with %s\" power: %s" % (type2, w2, power2)

    congrats_tpl = "Winner is \"%s with %s\""
    if power1 > power2:
        congrats = congrats_tpl % (type1, w1)
    elif power2 > power1:
        congrats = congrats_tpl % (type2, w2)
    else:
        congrats = "Draw"

    print(line)
    print("===================")
    print(oop1_info)
    print(oop2_info)
    print("===================")
    print(congrats)


opponent1 = get_opponent()
opponent2 = get_opponent()

fight(opponent1, opponent2)
