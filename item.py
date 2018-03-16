class Item:

    def __init__(self, typ, name, begehbar, aufnehmbar, bild, werte):
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

    def gettyp(self):
        return self._typ

    def getname(self):
        return self._name

    def getbegehbar(self):
        return self._begehbar

    def getaufnehmbar(self):
        return self._aufnehmbar

    def getaktiv(self):
        return self._aktiv

    def setaktiv(self, aktiv):
        self._aktiv = aktiv

    def getbild(self):
        return self._bild

    def setbild(self, bild):
        self._bild = bild

    def getwert(self):
        return self._wert

    def geteigenschaften(self):
        return self._eigenschaften

    def benutzen(self, held):
        return held

    def anlegen(self, held):
        self._wirdgetragen = True
        return held

    def ablegen(self, held):
        self._wirdgetragen = False
        return held

    def wirdgetragen(self):
        return self._wirdgetragen
