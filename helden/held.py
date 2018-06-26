from math import *
from items import *


# Class hero
class Hero:

    def __init__(self, name):
        self._heldenname = name
        self._heldentyp = 0  # 0 Batman, 1 Superman, 2 Spiderman, 3 Ironman, 4 Green Lantern, 5 Flash
        self._geschlecht = 0  # 0 maennlich; 1 weiblich
        self._typname = 'Batman'  # Typ des Heroen
        self._eigenschaften = [11, 11, 10, 11, 10, 11, 10, 10]  # MU KL CH IN FF GE KO KK
        self._kampfwerte = [11, 11, 165]  # AT PA LeP
        self._unlocklevel = 0
        self._bild = 'gfxhelden/Batman.gif'
        self._anzeigeBild = 'gfxhelden/Batman0.gif'
        self._x, self._y, self._ap = 0, 0, 0
        self._lichtradius, self.timeout = 1.0, 0.1
        self._itemliste = [Schwert(0), Wattierterwaffenrock(0)]  # leere Liste, in der alle Items gespeichert sind
        self._ruestung, self._waffe, self._maxle = self._itemliste[1], self._itemliste[0], self._kampfwerte[2]
        self.itemtodrop = Noitem(0)

    def var_init(self):
        self._ruestung, self._waffe, self._maxle = self._itemliste[1], self._itemliste[0], self._kampfwerte[2]

    @staticmethod
    def factory(wanted_obj: str):
        text = "Bitten Name eingeben"
        subclasses = {
            "Batman": Batman(text),
            "Superman": Superman(text),
            "Spiderman": Spiderman(text),
            "Ironman": Ironman(text),
            "GreenLantern": GreenLantern(text),
            "Flash": Flash(text)
        }
        return subclasses.get(wanted_obj)

    def getheldenname(self) -> str:
        return self._heldenname

    def setheldenname(self, name: str):
        self._heldenname = str(name)

    def getgeschlecht(self) -> int:
        return self._geschlecht

    def setgeschlecht(self, geschlecht: int):
        self._geschlecht = int(geschlecht)

    def getheldentyp(self) -> int:
        return self._heldentyp

    def gettypname(self) -> str:
        return self._typname

    def geteigenschaften(self) -> [int]:
        return self._eigenschaften

    def seteigenschaften(self, liste: [int]):
        self._eigenschaften = liste

    def geteigenschaft(self, pos: int) -> int:
        return self._eigenschaften[pos]

    def seteigenschaft(self, pos: int, wert: int):
        self._eigenschaften[pos] = wert

    def getkampfwerte(self) -> [int]:
        return self._kampfwerte

    def setkampfwerte(self, liste: [int]):
        self._kampfwerte = liste

    def getkampfwert(self, pos: int) -> int:
        return self._kampfwerte[pos]

    def setkampfwert(self, pos: int, wert: int):
        self._kampfwerte[pos] = wert

    def getwaffe(self) -> Waffe:
        return self._waffe

    def setwaffe(self, waffe: int):
        self._waffe = waffe

    def getruestung(self) -> Ruestung:
        return self._ruestung

    def setruestung(self, ruestung: int):
        self._ruestung = ruestung

    def getrs(self) -> int:
        return self.getruestung().getrs()

    def getbild(self) -> str:
        return self._bild

    def setbild(self, bild: str):
        self._bild = bild

    def get_anzeige_bild(self) -> str:
        return self._anzeigeBild

    def getx(self) -> int:
        return self._x

    def setx(self, x: int):
        self._x = x

    def gety(self) -> int:
        return self._y

    def sety(self, y: int):
        self._y = y

    # noinspection PyAttributeOutsideInit
    def ausleuchten(self) -> [(int, int)]:
        light = [(self._x, self._y)]
        self.fackelradius = 1.0  # spaeter an anderer Stelle einfuegen, etwa beim Entzueden oder Besitzen einer Fackel
        maxr = self._lichtradius + self.fackelradius
        for i in range(int(8 * maxr)):
            for r in range(int(maxr)):
                light = light + [(self._x + int(round((r + 1) * cos(2 * pi * (i + 1) / (8 * maxr)), 0)),
                                  self._y + int(round((r + 1) * sin(2 * pi * (i + 1) / (8 * maxr)), 0)))]
                print(light)
        return light

    def itemnehmen(self, item: Item):  # nimmt das Item it in die Itemliste auf
        self._itemliste = self._itemliste + [item]

    def itemablegen(self, n: int) -> Item:  # gibt das n-te Item aus der Itemliste zurueck
        if n < len(self._itemliste):
            it = self._itemliste[n]
        else:
            it = Noitem(0)
        return it

    def getitemliste(self) -> [Item]:
        return self._itemliste

    def getap(self) -> int:
        return self._ap

    def addap(self, ap):
        self._ap = self._ap + ap

    def getmaxle(self):
        return self._maxle

    def setmaxle(self, maxle):
        self._maxle = maxle

    def getunlocklvl(self):
        return self._unlocklevel

    def setunlocklvl(self, lvl):
        self._unlocklevel = lvl

    def getle(self):
        return self._kampfwerte[2]

    def setle(self, le: int):
        self._kampfwerte[2] = le

    def getitemdrop(self) -> Item:
        return self.itemtodrop

    def heilen(self, sp: int):
        self._kampfwerte[2] = self._kampfwerte[2] + int(sp * (self._eigenschaften[4] + self._eigenschaften[6]) / 40)
        if self._kampfwerte[2] > self._maxle:
            self._kampfwerte[2] = self._maxle

    def get_timeout(self) -> float:
        return self.timeout


# Subclasses for all heros, new ones are added on top of the old ones
class Flash(Hero):
    def __init__(self, name: str):
        Hero.__init__(self, name)
        self._heldentyp, self.timeout, self._typname = 5, 0, 'Flash'
        self._bild, self._anzeigeBild = 'gfxhelden/Flash.gif', 'gfxhelden/Flash0.gif'
        self._eigenschaften, self._kampfwerte = [9, 13, 10, 13, 12, 11, 13, 9], [14, 10, 150]
        self._unlocklevel = 5
        self._itemliste = [Dolch(0), Kleidung(0)]
        self.var_init()


class GreenLantern(Hero):
    def __init__(self, name: str):
        Hero.__init__(self, name)
        self._heldentyp, self._typname, self._lichtradius = 4, 'GreenLantern', 2.0
        self._bild, self._anzeigeBild = 'gfxhelden/GreenLantern.gif', 'gfxhelden/GreenLantern0.gif'
        self._eigenschaften, self._kampfwerte = [9, 13, 10, 13, 12, 11, 13, 9], [14, 10, 90]
        self._unlocklevel = 3
        self._itemliste = [Dolch(0), Kleidung(0)]
        self.var_init()

    def heilen(self, sp: int):
        self._kampfwerte[2] += int(sp * (self._eigenschaften[4] + self._eigenschaften[6] + 6) / 40)  # 15% heilen Bonus
        if self._kampfwerte[2] > self._maxle:
            self._kampfwerte[2] = self._maxle


class Ironman(Hero):
    def __init__(self, name: str):
        Hero.__init__(self, name)
        self._heldentyp, self._typname, self._lichtradius = 2, 'Ironman', 2.0
        self._bild, self._anzeigeBild = 'gfxhelden/Ironman.gif', 'gfxhelden/Ironman0.gif'
        self._eigenschaften, self._kampfwerte = [12, 9, 8, 10, 11, 12, 13, 13], [13, 10, 180]
        self._unlocklevel = 4
        self._itemliste = [Langschwert(0), Kettenhemd(0)]
        self.var_init()


class Spiderman(Hero):
    def __init__(self, name: str):
        Hero.__init__(self, name)
        self._heldentyp, self._typname, self._lichtradius = 2, 'Spiderman', 2.0
        self._bild, self._anzeigeBild = 'gfxhelden/Spiderman.gif', 'gfxhelden/Spiderman0.gif'
        self._eigenschaften, self._kampfwerte = [10, 11, 13, 12, 13, 13, 10, 10], [8, 12, 166]
        self._unlocklevel = 2
        self._itemliste = [Kurzschwert(0), Wattierterwaffenrock(0)]
        self.var_init()


class Superman(Hero):
    def __init__(self, name: str):
        Hero.__init__(self, name)
        self._heldentyp, self._typname = 1, 'Superman'
        self._bild, self._anzeigeBild = 'gfxhelden/Superman.gif', 'gfxhelden/Superman0.gif'
        self._eigenschaften, self._kampfwerte = [12, 9, 8, 10, 11, 12, 13, 13], [19, 10, 98]
        self._unlocklevel = 0
        self._itemliste = [Langschwert(0), Kettenhemd(0)]
        self.var_init()


class Batman(Hero):
    def __init__(self, name: str):
        Hero.__init__(self, name)
        self._heldentyp, self._typname = 0, 'Batman'
        self._bild, self._anzeigeBild = 'gfxhelden/Batman.gif', 'gfxhelden/Batman0.gif'
        self._eigenschaften, self._kampfwerte = [11, 11, 10, 11, 10, 11, 10, 10], [11, 11, 165]
        self._unlocklevel = 0
        self._itemliste = [Schwert(0), Wattierterwaffenrock(0)]
        self.var_init()
