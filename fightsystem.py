# Purpose:
#   - Fight handles the fighting of two objects
#   - Objects can be monsters and heros

from helden import held as hero_lib
from monsters import *


class Fight:
    def __init__(self, attacker, defender):
        self._attacker, self._defender = attacker, defender
        # getting itemlists from objects
        self._attacker_items, self._defender_items = attacker.getitemliste(), defender.getitemliste()
        # getting armor values from objects
        self._attacker_armor, self._defender_armor = attacker.getrs(), defender.getrs()
        # getting values from attacker
        self._attacker_characteristics, self._attacker_combat = attacker.geteigenschaften(), attacker.getkampfwerte()
        # getting values from defender
        self._defender_characteristics, self._defender_combat = defender.geteigenschaften(), defender.getkampfwerte()
        # getting experience points (ap) from objects
        self._attacker_exp, self._defender_exp = attacker.getap(), defender.getap()
        
    def attack(self):
        pass

    def defend(self):
        pass


B = hero_lib.Hero.factory("Batman")
S = hero_lib.Hero.factory("Superman")
print(S.getrs())
o = Ork1(1)
print(o.geteigenschaften())
f = Fight(S, o)
print(f._attacker_characteristics)