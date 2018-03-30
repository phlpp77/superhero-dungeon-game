from helden import *
from monsters import *


class Fight:
    def __init__(self, attacker, defender):
        self._attacker, self._defender = attacker, defender
        self._attacker_characteristics, self._attacker_combat = attacker.geteigenschaften(), attacker.getkampfwerte()


# print(f._attacker_characteristics)
B = Hero(Batman)
S = Superman
f = Fight(Batman, Superman)
B.geteigenschaften()[0]