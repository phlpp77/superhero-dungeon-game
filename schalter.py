# Typ: Schalter


class Schalter:

    def __init__(self, typ, felderliste):
        self._schaltertyp = typ
        self._aktiv = 0  # wird intern von den Ausloeseprozeduren verwaltet
        self._felderliste = felderliste

    def getschaltertyp(self):
        return self._schaltertyp

    def getfelderliste(self):
        return self._felderliste

    def ausloesen(self, dungeonebene):
        return dungeonebene
