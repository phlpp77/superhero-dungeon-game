from helden.held import *
from items import *


class GreenLantern(Held):

    def __init__(self, name):
        Held.__init__(self, name)
        self._heldentyp = 4
        self._typname = 'GreenLantern'  # Typ des Helden
        self._eigenschaften = [9, 13, 10, 13, 12, 11, 13, 9]  # MU KL CH IN FF GE KO KK
        self._kampfwerte = [14, 10, 90]  # AT PA LeP
        self._maxle = self._kampfwerte[2]  # LeP-Maximum
        self._unlocklevel = 1
        self._bild = 'gfxhelden/GreenLantern.gif'
        self._anzeigeBild = 'gfxhelden/GreenLantern0.gif'
        self._itemliste = [Dolch(), Kleidung()]  # leere Liste, in der alle Items gespeichert sind
        self._waffe = self._itemliste[0]  # Waffe
        self._ruestung = self._itemliste[1]  # Ruestung

    def heilen(self, sp):
        self._kampfwerte[2] = self._kampfwerte[2] + int(
            sp * (self._eigenschaften[4] + self._eigenschaften[6] + 6) / 40)  # 6/40=15% Heilen Bonus
        if self._kampfwerte[2] > self._maxle:
            self._kampfwerte[2] = self._maxle
