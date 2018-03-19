import os
from item import *
from waffe import *
from ruestung import *


# pickable items

class Noitem(Item):
    # noinspection PyUnusedLocal
    def __init__(self, lvl_number):
        Item.__init__(self, 0, '', True, False, 'gfxitems/noitem.gif', (0,))

    def get_image(self):
        pass


class Dolch(Waffe):
    # noinspection PyUnusedLocal
    def __init__(self, lvl_number):
        Waffe.__init__(self, 101, 'Dolch', True, True, 'gfxitems/dolch.gif', (25, 1, 2, 0, 0))


class Kurzschwert(Waffe):
    # noinspection PyUnusedLocal
    def __init__(self, lvl_number):
        Waffe.__init__(self, 102, 'Kurzschwert', True, True, 'gfxitems/kurzschwert.gif', (40, 1, 3, 0, 0))


class Schwert(Waffe):
    # noinspection PyUnusedLocal
    def __init__(self, lvl_number):
        Waffe.__init__(self, 103, 'Schwert', True, True, 'gfxitems/schwert.gif', (50, 1, 4, 0, 0))


class Langschwert(Waffe):
    # noinspection PyUnusedLocal
    def __init__(self, lvl_number):
        Waffe.__init__(self, 104, 'Langschwert', True, True, 'gfxitems/langschwert.gif', (70, 1, 5, 0, 0))


class Kleidung(Ruestung):
    # noinspection PyUnusedLocal
    def __init__(self, lvl_number):
        Ruestung.__init__(self, 201, 'Kleidung', True, True, 'gfxitems/kleidung.gif', (10, 1))


class Wattierterwaffenrock(Ruestung):
    def __init__(self):
        Ruestung.__init__(self, 202, 'Watwaffenrock', True, True, 'gfxitems/watwaffenrock.gif', (30, 2))


class Kettenhemd(Ruestung):
    # noinspection PyUnusedLocal
    def __init__(self, lvl_number):
        Ruestung.__init__(self, 203, 'Kettenhemd', True, True, 'gfxitems/kettenhemd.gif', (50, 3))


# not pickable items

class Torch(Item):
    def __init__(self):
        Item.__init__(self, 801, "Torch", True, False, "gfxoverlay/51fackel.gif", (0,))


# Teleportation

class Teleport2(Item):
    def __init__(self, lvl_number):
        schatten_gif = os.path.join("gfxlvl" + str(lvl_number), "teleportschatten.gif")
        Item.__init__(self, 902, 'Einstieg', True, False, schatten_gif, (0,))


class Treppe1(Item):
    def __init__(self, lvl_number):
        treppe_gif = os.path.join("gfxlvl" + str(lvl_number), "treppe.gif")
        Item.__init__(self, 911, 'Treppe in den naechsten Level', True, False, treppe_gif, (0,))
