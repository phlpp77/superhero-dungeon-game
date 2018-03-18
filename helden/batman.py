from helden.held import *
from items import *


class Batman(Held):

    def __init__(self, name):
        Held.__init__(self, name)
        self._heldentyp = 0
        self._typname = 'Batman'  # Typ des Helden
        self._eigenschaften = [11, 11, 10, 11, 10, 11, 10, 10]  # MU KL CH IN FF GE KO KK
        self._kampfwerte = [11, 11, 165]  # AT PA LeP
        self._maxle = self._kampfwerte[2]  # LeP-Maximum
        self._unlocklevel = 0
        self._bild = 'gfxhelden/Batman.gif'
        self._anzeigeBild = 'gfxhelden/Batman0.gif'
        self._lichtradius = 1.0
        self._itemliste = [Schwert(), Wattierterwaffenrock()]  # leere Liste, in der alle Items gespeichert sind
        self._waffe = self._itemliste[0]  # Waffe
        self._ruestung = self._itemliste[1]
