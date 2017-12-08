from schalter import *


# Sammlung der Schalter

class Noschalter(Schalter):
    def __init__(self, felderliste):
        Schalter.__init__(self, 0, [])


class Levelendschalter(Schalter):
    def __init__(self, felderliste):
        Schalter.__init__(self, 1, [])

    def ausloesen(self, dungeonebene):
        dungeonebene.setlevelende(True)
        return dungeonebene


class Spielendschalter(Schalter):
    def __init__(self, felderliste):
        Schalter.__init__(self, 2, [])

    def ausloesen(self, dungeonebene):
        dungeonebene.setspielende(True)
        return dungeonebene


class Lichtschalter(Schalter):
    def __init__(self, felderliste):
        Schalter.__init__(self, 11, felderliste)

    def ausloesen(self, dungeonebene):
        for i in self._felderliste:
            dungeonebene.setlightmap(i[0], i[1], 0.999)  # Felderkoordinaten die ausgeleuchtet werden. Bei 0 beginnend!!
        return dungeonebene


class Wandwegschalter(Schalter):
    def __init__(self, felderliste):
        Schalter.__init__(self, 21, felderliste)

    def ausloesen(self, dungeonebene):
        for i in self._felderliste:
            dungeonebene.setbodenbild(i[0], i[1], 'gfxlvl' + str(dungeonebene.getlevelnr()) + '/boden.gif')
            dungeonebene.setbegehbar(i[0], i[1], True)
        return dungeonebene
