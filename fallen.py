from falle import *


class Nofalle(Falle):
    def __init__(self, lvl_number):
        Falle.__init__(self, 20100, '', True, False, 'gfxitems/noitem.gif', (0, 0, 0, 0, 0, 0, 0))

    def get_image(self):
        pass


class Steinschlagfalle(Falle):
    def __init__(self, lvl_number):
        Falle.__init__(self, 20101, 'Steinschlagfalle', True, False, 'gfxitems/steinschlagfalle.gif',
                       (0, 2, 1, 2, 0, 1, 5))


class Todesfalle(Falle):
    def __init__(self, lvl_number):
        Falle.__init__(self, 30101, 'Todesfalle', True, False, 'gfxitems/todesfalle.gif', (0, 2, 1000, 1000, 0, 1, 5))
