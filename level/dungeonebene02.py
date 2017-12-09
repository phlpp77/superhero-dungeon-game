from level.dungeonebene import *


class Dungeonebene02(Dungeonebene):

    def __init__(self, nr, held):
        super().__init__(nr, held)
        self._nr = nr
        self._levelende = False
        self._spielende = False
        self._dungeonlayoutdaten = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
                                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
                                    [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self._dungeonoverlaydaten = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self._dungeonitemdaten = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 911, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 902, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 10101, 0, 0, 101, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10101, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self._dungeonschalterdaten = [
            [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (0, []), (0, []), (1, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, [])],
            [(0, []), (0, []), (0, []), (0, []), (21, [(10, 4)]), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
             (0, []), (0, []), (0, []), (0, []), (0, []), (0, [])],
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
