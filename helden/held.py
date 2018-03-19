from math import *
from items import *
import time


# Class hero
class Hero:

    def __init__(self, name):
        self._heldenname = name
        self._heldentyp = 0  # 0 Batman, 1 Superman, 2 Spiderman, 3 Ironman, Green Lantern, 4 Flash
        self._geschlecht = 0  # 0 maennlich; 1 weiblich
        self._typname = 'Batman'  # Typ des Heroen
        self._eigenschaften = [11, 11, 10, 11, 10, 11, 10, 10]  # MU KL CH IN FF GE KO KK
        self._kampfwerte = [11, 11, 165]  # AT PA LeP
        self._unlocklevel = 0
        self._bild = 'gfxhelden/Batman.gif'
        self._anzeigeBild = 'gfxhelden/Batman0.gif'
        self._x, self._y, self._ap = 0, 0, 0
        self._lichtradius, self.timeout = 1.0, 0.1
        self._itemliste = [Schwert(), Wattierterwaffenrock()]  # leere Liste, in der alle Items gespeichert sind
        self._ruestung = self._waffe = self._maxle = 0
        self.var_init()

    @staticmethod
    def factory(wanted_obj):
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

    def var_init(self):
        self._maxle, self._waffe, self._ruestung = self._kampfwerte[2], self._itemliste[0], self._itemliste[1]

    def getheldenname(self):
        return self._heldenname

    def setheldenname(self, name):
        self._heldenname = str(name)

    def getgeschlecht(self):
        return self._geschlecht

    def setgeschlecht(self, geschlecht):
        self._geschlecht = int(geschlecht)

    def getheldentyp(self):
        return self._heldentyp

    def gettypname(self):
        return self._typname

    def geteigenschaften(self):
        return self._eigenschaften

    def seteigenschaften(self, liste):
        self._eigenschaften = liste

    def geteigenschaft(self, pos):
        return self._eigenschaften[pos]

    def seteigenschaft(self, pos, wert):
        self._eigenschaften[pos] = wert

    def getkampfwerte(self):
        return self._kampfwerte

    def setkampfwerte(self, liste):
        self._kampfwerte = liste

    def getkampfwert(self, pos):
        return self._kampfwerte[pos]

    def setkampfwert(self, pos, wert):
        self._kampfwerte[pos] = wert

    def getwaffe(self):
        return self._waffe

    def setwaffe(self, waffe):
        self._waffe = waffe

    def getruestung(self):
        return self._ruestung

    def setruestung(self, ruestung):
        self._ruestung = ruestung

    def getbild(self):
        return self._bild

    def setbild(self, bild):
        self._bild = bild

    def get_anzeige_bild(self):
        return self._anzeigeBild

    def getx(self):
        return self._x

    def setx(self, x):
        self._x = x

    def gety(self):
        return self._y

    def sety(self, y):
        self._y = y

    # noinspection PyAttributeOutsideInit
    def ausleuchten(self):
        light = [(self._x, self._y)]
        self.fackelradius = 1.0  # spaeter an anderer Stelle einfuegen, etwa beim Entzueden oder Besitzen einer Fackel
        maxr = self._lichtradius + self.fackelradius
        for i in range(int(8 * maxr)):
            for r in range(int(maxr)):
                light = light + [(self._x + int(round((r + 1) * cos(2 * pi * (i + 1) / (8 * maxr)), 0)),
                                  self._y + int(round((r + 1) * sin(2 * pi * (i + 1) / (8 * maxr)), 0)))]
        return light

    def itemnehmen(self, it):  # nimmt das Item it in die Itemliste auf
        self._itemliste = self._itemliste + [it]

    def itemablegen(self, n):  # gibt das n-te Item aus der Itemliste zurueck
        if n < len(self._itemliste):
            it = self._itemliste[n]
        else:
            it = Noitem()
        return it

    def getitemliste(self):
        return self._itemliste

    def getap(self):
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

    def setle(self, le):
        self._kampfwerte[2] = le

    def heilen(self, sp):
        self._kampfwerte[2] = self._kampfwerte[2] + int(sp * (self._eigenschaften[4] + self._eigenschaften[6]) / 40)
        if self._kampfwerte[2] > self._maxle:
            self._kampfwerte[2] = self._maxle

    def get_timeout(self):
        return self.timeout


# Subclasses for all heros, new ones are added on top of the old ones
class Flash(Hero):
    def __init__(self, name):
        Hero.__init__(self, name)
        self._heldentyp, self.timeout, self._typname = 5, 0, 'Flash'
        self._bild, self._anzeigeBild = 'gfxhelden/Flash.gif', 'gfxhelden/Flash0.gif'
        self._eigenschaften, self._kampfwerte = [9, 13, 10, 13, 12, 11, 13, 9], [14, 10, 150]
        self._unlocklevel = 5
        self._itemliste = [Dolch(), Kleidung()]
        self.var_init()


class GreenLantern(Hero):
    def __init__(self, name):
        Hero.__init__(self, name)
        self._heldentyp, self._typname, self._lichtradius = 4, 'GreenLantern', 2.0
        self._bild, self._anzeigeBild = 'gfxhelden/GreenLantern.gif', 'gfxhelden/GreenLantern0.gif'
        self._eigenschaften, self._kampfwerte = [9, 13, 10, 13, 12, 11, 13, 9], [14, 10, 90]
        self._unlocklevel = 3
        self._itemliste = [Dolch(), Kleidung()]
        self.var_init()

    def heilen(self, sp):
        self._kampfwerte[2] += int(sp * (self._eigenschaften[4] + self._eigenschaften[6] + 6) / 40)  # 15% heilen Bonus
        if self._kampfwerte[2] > self._maxle:
            self._kampfwerte[2] = self._maxle


class Ironman(Hero):
    def __init__(self, name):
        Hero.__init__(self, name)
        self._heldentyp, self._typname, self._lichtradius = 2, 'Ironman', 2.0
        self._bild, self._anzeigeBild = 'gfxhelden/Ironman.gif', 'gfxhelden/Ironman0.gif'
        self._eigenschaften, self._kampfwerte = [12, 9, 8, 10, 11, 12, 13, 13], [13, 10, 180]
        self._unlocklevel = 4
        self._itemliste = [Langschwert(), Kettenhemd()]
        self.var_init()


class Spiderman(Hero):
    def __init__(self, name):
        Hero.__init__(self, name)
        self._heldentyp, self._typname, self._lichtradius = 2, 'Spiderman', 2.0
        self._bild, self._anzeigeBild = 'gfxhelden/Spiderman.gif', 'gfxhelden/Spiderman0.gif'
        self._eigenschaften, self._kampfwerte = [10, 11, 13, 12, 13, 13, 10, 10], [8, 12, 166]
        self._unlocklevel = 2
        self._itemliste = [Kurzschwert(), Wattierterwaffenrock()]
        self.var_init()


class Superman(Hero):
    def __init__(self, name):
        Hero.__init__(self, name)
        self._heldentyp, self._typname = 1, 'Superman'
        self._bild, self._anzeigeBild = 'gfxhelden/Superman.gif', 'gfxhelden/Superman0.gif'
        self._eigenschaften, self._kampfwerte = [12, 9, 8, 10, 11, 12, 13, 13], [19, 10, 98]
        self._unlocklevel = 0
        self._itemliste = [Langschwert(), Kettenhemd()]
        self.var_init()


class Batman(Hero):
    def __init__(self, name):
        Hero.__init__(self, name)
        self._heldentyp, self._typname = 0, 'Batman'
        self._bild, self._anzeigeBild = 'gfxhelden/Batman.gif', 'gfxhelden/Batman0.gif'
        self._eigenschaften, self._kampfwerte = [11, 11, 10, 11, 10, 11, 10, 10], [11, 11, 165]
        self._unlocklevel = 0
        self._itemliste = [Schwert(), Wattierterwaffenrock()]
        self.var_init()
