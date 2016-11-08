from helden.held import *
from items import *

class Flash(Held):

    def __init__(self,name):
        Held.__init__(self,name)
        self._heldentyp = 5
        self._typname = 'Flash'                                  # Typ des Helden
        self._eigenschaften = [9,13,10,13,12,11,13,9]            # MU KL CH IN FF GE KO KK
        self._kampfwerte = [14,10,600]                            # AT PA LeP
        self._maxle=self._kampfwerte[2]                          # LeP-Maximum        
        self._bild = 'gfxhelden/Flash.gif'
        self._anzeigeBild = 'gfxhelden/Flash0.gif'
        self._itemliste = [Dolch(),Kleidung()]                  # leere Liste, in der alle Items gespeichert sind
        self._waffe = self._itemliste[0]                        # Waffe
        self._ruestung = self._itemliste[1]                     # Ruestung
