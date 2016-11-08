from helden.held import *
from items import *

class Ironman(Held):

    def __init__(self,name):
        Held.__init__(self,name)
        self._heldentyp = 3
        self._typname = 'Ironman'                              # Typ des Helden
        self._eigenschaften = [12,9,8,10,11,12,13,13]           # MU KL CH IN FF GE KO KK
        self._kampfwerte = [13,10,180]                           # AT PA LeP
        self._maxle=self._kampfwerte[2]                         # LeP-Maximum        
        self._bild = 'gfxhelden/Ironman.gif'
        self._anzeigeBild = 'gfxhelden/Ironman0.gif'
        self._lichtradius = 2.0
        self._itemliste = [Langschwert(),Kettenhemd()]          # leere Liste, in der alle Items gespeichert sind
        self._waffe = self._itemliste[0]                        # Waffe
        self._ruestung = self._itemliste[1]                     # Ruestung
