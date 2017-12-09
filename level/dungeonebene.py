from feld import *


class Dungeonebene:

    def __init__(self, nr, held):
        self._nr = nr
        self._levelende = False
        self._spielende = False
        self._dungeonlayoutdaten = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                                    [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                                    [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self._dungeonoverlaydaten = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 41, 0, 0, 0, 0, 0, 0, 61, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self._dungeonitemdaten = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 10101, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 10101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 20101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 902, 0, 0, 101, 0, 0, 0, 911, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self._dungeonschalterdaten = [
            [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (11, [(7, 4), (8, 4)]), (0, []), (0, []), (21, [(6, 1)]), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (1, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])]]

        self._maxy = len(self._dungeonlayoutdaten)
        self._maxx = len(self._dungeonlayoutdaten[0])

        self._dungeonplan = list(
            range(self._maxx))  # Anlegen eines Feldes, in dem die alle Kacheln des Dungeons gespeichert sind
        for i in range(self._maxx):
            self._dungeonplan[i] = list(range(self._maxy))

        for x in range(self._maxx):
            for y in range(self._maxy):
                self._dungeonplan[x][y] = Feld(nr, self._dungeonlayoutdaten[y][x], 0.001,
                                               self._dungeonoverlaydaten[y][x], self._dungeonitemdaten[y][x],
                                               self._dungeonschalterdaten[y][x])
                if (self._dungeonitemdaten[y][x] > 900) and (self._dungeonitemdaten[y][x] < 910):
                    held.setx(x)
                    held.sety(y)

    def getlevelnr(self):
        return self._nr

    def getlevelende(self):
        return self._levelende

    def setlevelende(self, levelende):
        self._levelende = levelende

    def getspielende(self):
        return self._spielende

    def setspielende(self, spielende):
        self._spielende = spielende

    def getmaxx(self):
        return self._maxx

    def getmaxy(self):
        return self._maxy

    def getbild(self, x, y):
        return self._dungeonplan[x][y].getbodenbild()

    def setbodenbild(self, x, y, bild):
        return self._dungeonplan[x][y].setbodenbild(bild)

    def getlightmap(self, x, y):
        return self._dungeonplan[x][y].getlightmap()

    def setlightmap(self, x, y, wert):
        self._dungeonplan[x][y].setlightmap(wert)

    def getfog(self, x, y):
        return self._dungeonplan[x][y].getfog()

    def setfog(self, x, y, fog=True):
        self._dungeonplan[x][y].setfog(fog)

    def getoverlaybild(self, x, y):
        return self._dungeonplan[x][y].getoverlaybild()

    def getitembild(self, x, y):
        return self._dungeonplan[x][y].getitembild()

    def getitem(self, x, y):
        return self._dungeonplan[x][y].getitem()

    def setitem(self, x, y, item):
        return self._dungeonplan[x][y].setitem(item)

    def getschalter(self, x, y):
        return self._dungeonplan[x][y].getschalter()

    def setschalter(self, x, y, schalter):
        return self._dungeonplan[x][y].setschalter(schalter)

    def getbegehbar(self, x, y):
        return self._dungeonplan[x][y].getbegehbar()

    def setbegehbar(self, x, y, begehbar):
        self._dungeonplan[x][y].setbegehbar(begehbar)

    def getfeld(self, x, y):
        return self._dungeonplan[x][y]

    def drawdungeon(self):
        s = ''
        for i in range(len(self._dungeonlayoutdaten)):
            for j in range(len(self._dungeonlayoutdaten[i])):
                if self._dungeonlayoutdaten[i][j] == 1:
                    s = s + ' '
                elif self._dungeonlayoutdaten[i][j] == 254:
                    s = s + chr(216)
                elif self._dungeonlayoutdaten[i][j] == 255:
                    s = s + chr(79)
                else:
                    s = s + chr(127)
            print(s)
            s = ''
