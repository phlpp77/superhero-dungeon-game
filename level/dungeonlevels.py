class DungeonLevel01:
    spielende = False
    dungeonlayout = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                     [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                     [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonitems = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 10101, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 10101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 20101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 902, 0, 0, 101, 0, 0, 0, 911, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonswitches = [
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


class DungeonLevel02:
    spielende = False
    dungeonlayout = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
                     [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
                     [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonitems = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 911, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 902, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 10101, 0, 0, 101, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10101, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonswitches = [
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


class DungeonLevel03:
    spielende = False
    dungeonlayout = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
                     [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                     [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonitems = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 902, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20101, 0],
                    [0, 0, 10101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10101, 30101, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonswitches = [
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (1, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (11, [(15, 7)]),
         (0, []), (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])]]


class DungeonLevel04:
    spielende = False
    dungeonlayout = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonitems = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10101, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10101, 0, 10101, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10101, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 902, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 911, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonswitches = [
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (1, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])]]


class DungeonLevel05:
    spielende = False
    dungeonlayout = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonitems = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 10101, 0, 0, 0, 0, 0, 10101, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 902, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 20101, 0, 0, 20101, 0, 0, 30101, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonswitches = [
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (1, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])]]


class DungeonLevel06:
    spielende = False
    dungeonlayout = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonitems = [[0, 0, 0, 0, 0, 0, 0, 0, 10102, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 104, 10101, 0, 10101, 203, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 902, 0, 0, 30101, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dungeonswitches = [
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (2, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (11, [(8, 0)]), (0, []), (0, []), (0, []),
         (21, [(8, 2), (8, 1)]), (0, []), (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (21, [(8, 5), (8, 4)]), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (21, [(8, 6)]), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, []), (0, [])],
        [(0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []), (0, []),
         (0, []), (0, []), (0, []), (0, []), (0, [])]]
