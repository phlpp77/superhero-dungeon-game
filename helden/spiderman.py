from helden.held import *
from items import *


class Spiderman(Held):

    def __init__(self, name):
        Held.__init__(self, name)
        self._heldentyp = 2
        self._typname = 'Spiderman'  # Typ des Helden
        self._eigenschaften = [10, 11, 13, 12, 13, 13, 10, 10]  # MU KL CH IN FF GE KO KK
        self._kampfwerte = [8, 12, 166]  # AT PA LeP
        self._maxle = self._kampfwerte[2]  # LeP-Maximum
        self._unlocklevel = 0
        self._bild = 'gfxhelden/Spiderman.gif'
        self._anzeigeBild = 'gfxhelden/Spiderman0.gif'
        self._lichtradius = 2.0
        self._itemliste = [Kurzschwert(), Wattierterwaffenrock()]  # leere Liste, in der alle Items gespeichert sind
        self._waffe = self._itemliste[0]  # Waffe
        self._ruestung = self._itemliste[1]  # Ruestung
