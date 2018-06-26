# Purpose:
#   - Fight handles the fighting of two objects
#   - Objects can be monsters and heros

from helden import held as hero_lib
from monsters import *
from items import *
from random import randint as rnd

"""import kivy
from kivy.app import App
from kivy.uix.label import Label"""


# class fight for the logic
class Fight:
    def __init__(self, attacker: hero_lib.Hero, defender: hero_lib.Hero):
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

        # quicklaunch
        self._attacker_lifepoints, self._defender_lifepoints = self._attacker_combat[2], self._defender_combat[2]

        # dict for all attacks based an items, 0-99 basic, 100-199 medium, 200-299 strong, 300-399 extreme
        self._attacks_dict = {"Dolch": 0, "Schwert": 0}

        # counter for blocked damge, after 3 blocks one attack goes through with 100%
        self._blocked_counter = 0

        # the real damage dealt is safed in a var
        self._realdamage = 0

    # attacking - calculating the truedamage dealt to the object
    def attack(self, item):
        attack = self._attacks_dict[item.getname()]
        add_damage = item.gettp()[0]
        # checking if attack goes throuh
        if self._attacker_combat[0] + attack > rnd(0, 20) < self._defender_combat[
            1] + self._defender_armor or self._blocked_counter == 3:
            # reset counter for blocked damage
            self._blocked_counter = 0
            print("attack")
            # damage dependent on the KK of the object
            damage = round(
                (self._attacker_combat[0] + self._attacker_characteristics[7] * rnd(0, 3) + add_damage) * 0.2)
            return damage
        else:
            self._blocked_counter += 1
            print("no attack")
            return 0

    # defending - calculating the realdamage dealt to the object
    def defend(self, item: Item, damage: int) -> int:
        add_armor = item.getrs()
        # deduct the armor shielding
        damage -= self._defender_armor + add_armor
        if damage <= 0:
            self._realdamage = 0
            return 0
        else:
            self._realdamage = damage
            return damage

    def update_health(self):
        self._defender.setle(self._defender_lifepoints - self._realdamage)
        # refresh of defender live
        self._defender_lifepoints = self._defender.getle()
        print("refresh")
        if self._defender_lifepoints <= 0:
            print("defender dead")
            self._defender._typ = 0
            self._defender._name = ''
            self._defender._begehbar = True
            self._defender._aufnehmbar = False
            self._defender._bild = 'gfx/blank.gif'
            self._defender._werte = ()
            # if self._defender.getitemdrop() != 0:
            # self._attacker.itemnehmen(self._defender.itemtodrop)


"""
# class fightscreen for gui
class FightScreen(App):
    def build(self):
        return Label(text="Test text")
"""

if __name__ == "__main__":
    B = hero_lib.Hero.factory("Batman")
    S = hero_lib.Hero.factory("Superman")
    print(S.getrs())
    o = Ork1(1)
    print(o.geteigenschaften())
    f = Fight(S, o)
    # print(f._attacker_characteristics)
    d = Dolch(0)
    h = Kleidung(0)
    for i in range(660):
        print(f.defend(h, f.attack(d)))
    f.update_health()

    f = FightScreen()
    f.run()
