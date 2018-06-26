class Item:

    def __init__(self, typ: int, name: str, begehbar: bool, aufnehmbar: bool, bild: str, werte: [int]):
        self._typ = typ
        self._name = name
        self._begehbar = begehbar
        self._aufnehmbar = aufnehmbar
        self._aktiv = 0  # -1 immer aktiv; 0 nicht aktiv; >0 Anzahl, wie oft noch aktiviert werden kann
        # wird intern von abgeleiteten Items in der Benutzen-Methode verwaltet
        self._bild = bild  # Bild des Items
        self._wert = werte[0]  # erster Wert ist immer der Wert des Items in Silbertalern
        self._eigenschaften = werte[1:]
        self._wirdgetragen = False

    def gettyp(self) -> int:
        return self._typ

    def getname(self) -> str:
        return self._name

    def getbegehbar(self) -> bool:
        return self._begehbar

    def getaufnehmbar(self) -> bool:
        return self._aufnehmbar

    def getaktiv(self) -> int:
        return self._aktiv

    def setaktiv(self, aktiv: int):
        self._aktiv = aktiv

    def getbild(self) -> str:
        return self._bild

    def setbild(self, bild: str):
        self._bild = bild

    def getwert(self) -> int:
        return self._wert

    def geteigenschaften(self) -> [int]:
        return self._eigenschaften

    def benutzen(self, held):
        return held

    def anlegen(self, held):
        self._wirdgetragen = True
        return held

    def ablegen(self, held):
        self._wirdgetragen = False
        return held

    def wirdgetragen(self) -> bool:
        return self._wirdgetragen

    def next_lvl(self):
        pass

    def get_image(self) -> str:
        return self._bild
