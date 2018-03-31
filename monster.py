from item import *
import random
from fightsystem import *


class Monster(Item):

    def __init__(self, typ, name, begehbar, aufnehmbar, bild, werte):
        Item.__init__(self, typ, name, begehbar, aufnehmbar, bild, werte)  # Wert der Waffe in Silbertalern
        self._characteristics = [0, 0, 0, 0, 0, 0, 0, 0]  # empty list, because a monster doesn't have characteristics
        self._kampfwerte = [werte[1], werte[2], werte[3]]  # AT PA LeP wie bei einem Held
        self._tp = (werte[4], werte[5])  # Wuerfel, Additiver Schaden
        self._mod = (werte[6], werte[7])  # AT-Modifkator, PA-Modifikator
        self._rs = werte[8]  # RüstungsSchutz
        self._ap = werte[9]  # Abenteuerpunkte
        self.itemtodrop = werte[10]  # item (Objekt), welches man bekommt, wenn man das Monster besiegt
        self._itemliste = [Kleidung(0), Dolch(0)]

    def getkampfwerte(self):
        return self._kampfwerte

    def geteigenschaften(self):
        return self._characteristics

    def getrs(self):
        return self._rs

    def getap(self):
        return self._ap

    def getitemdrop(self):
        return self.itemtodrop

    def getitemliste(self):
        return self._itemliste

    def gettp(self):
        return self._tp

    def getmod(self):
        return self._mod

    def setle(self, leben):
        self._kampfwerte[2] = leben

    def getle(self):
        return self._kampfwerte[2]

    def benutzen(self, held):
        while held.getkampfwerte()[2] > 0 and self._kampfwerte[2] > 0:  # solange beide noch leben

            # hero first
            attack_hero = Fight(held, self)
            dmg = attack_hero.attack(held.getwaffe())
            attack_hero.defend(self.getitemliste()[0], dmg)
            attack_hero.update_health()

            # monster second
            attack_monster = Fight(self, held)
            dmg = attack_monster.attack(self.getitemliste()[1])
            attack_monster.defend(held.getruestung(), dmg)
            attack_monster.update_health()

            print("Zwischenstand - Monstereben:", self._kampfwerte[2], "Heldleben: ", held.getle())  # Testausgabe

        return held
