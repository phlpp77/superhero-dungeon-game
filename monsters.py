from items import *
from monster import *


class Nomonster(Monster):  # Werte, Geldwert, Angriff, Verteidigung, Leben, würfel adativer Schaden (2x),
    # Modifikation (2x), Rüstungsschutz, Abenteuerpunkte, Itemdrop
    def __init__(self):
        Monster.__init__(self, 10100, '', True, False, 'gfxitems/noitem.gif', (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Noitem()))


class Ork1(Monster):  # Handlanger
    def __init__(self):
        Monster.__init__(self, 10101, 'Ork', False, False, 'gfxmnstr/ork1.gif',
                         (0, 11, 9, 25, 1, 4, 3, 0, 2, 20, Noitem()))


class Joker(Monster):  # Endboss
    def __init__(self):
        Monster.__init__(self, 10102, 'Joker', False, False, 'gfxmnstr/joker.gif',
                         (0, 11, 7, 10, 1, 4, 0, 0, 2, 20, Noitem()))
