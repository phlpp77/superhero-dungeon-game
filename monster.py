from item import *
import random


class Monster(Item):

    def __init__(self, typ, name, begehbar, aufnehmbar, bild, werte):
        Item.__init__(self, typ, name, begehbar, aufnehmbar, bild, werte)  # Wert der Waffe in Silbertalern
        self._characteristics = []  # empty list, because a monster doesn't have characteristics
        self._kampfwerte = [werte[1], werte[2], werte[3]]  # AT PA LeP wie bei einem Held
        self._tp = (werte[4], werte[5])  # Wuerfel, Additiver Schaden
        self._mod = (werte[6], werte[7])  # AT-Modifkator, PA-Modifikator
        self._rs = werte[8]  # RüstungsSchutz
        self._ap = werte[9]  # Abenteuerpunkte
        self._itemtodrop = werte[10]  # item (Objekt), welches man bekommt, wenn man das Monster besiegt
        self._itemliste = []

    def getkampfwerte(self):
        return self._kampfwerte

    def geteigenschaften(self):
        return self._characteristics

    def getrs(self):
        return self._rs

    def getap(self):
        return self._ap

    def getitemdrop(self):
        return self._itemtodrop

    def getitemliste(self):
        return self._itemliste

    def gettp(self):
        return self._tp

    def getmod(self):
        return self._mod

    def benutzen(self, held):
        heldaltle = held.getle()
        while held.getkampfwerte()[2] > 0 and self._kampfwerte[2] > 0:  # solange beide noch leben
            tp = 0  # Trefferpunkte die abgezogen werden
            heldle = 0  # Heldleben

            # Held schlaegt zu, wenn wahrscheinlichkeit es erlaubt
            if held.getkampfwerte()[0] + held.getwaffe().getmod()[0] >= random.randint(1, 20) \
                    > self._kampfwerte[1] + self._mod[1]:
                # Schaden (Tp-Trefferpunkte) wird berechnet
                tp = held.getwaffe().gettp()[1]
                for i in range(held.getwaffe().gettp()[0]):
                    tp += random.randint(1, 6)
                if (tp - self._rs) > 0:
                    print('Treffer auf Monster: LE', self._kampfwerte[2], 'TP:', tp, 'RS von Monster:', self._rs)  # Testausgabe
                    self._kampfwerte[2] -= (tp - self._rs)

            # Monster schlaegt zu, wenn Monster noch lebt und wahrscheinlichkeit es erlaubt
            if self._kampfwerte[2] > 0 and self._kampfwerte[0] + self._mod[0] >= random.randint(1, 20) \
                    > held.getkampfwerte()[1] + held.getwaffe().getmod()[1]:
                # Schaden (Tp-Trefferpunkte) wird berechnet
                tp = self._tp[1]
                for i in range(self._tp[0]):
                    tp += random.randint(1, 6)
                if (tp - held.getruestung().getrs()) > 0:
                    print('Treffer auf Held: LE', held.getle(), 'TP:', tp, 'RS von Held:',
                          held.getruestung().geteigenschaften()[0])  # Testausgabe
                    heldle = held.getle() - (tp - held.getruestung().getrs())
                    held.setle(heldle)

            # Monster verschwindet bei LE<0
            if self._kampfwerte[2] <= 0:
                self._typ = 0
                self._name = ''
                self._begehbar = True
                self._aufnehmbar = False
                self._bild = 'gfx/blank.gif'
                self._werte = (0,)
                print("Tot ", heldaltle, held.getle(), 'also', heldaltle - held.getle()) # Testausgabe
                # Lebensraub
                held.heilen(heldaltle - held.getle())
                # Abenteurpunkt hinzufügen
                held.addap(self._ap)
                if self._itemtodrop.gettyp() != 0:
                    held.itemnehmen(self._itemtodrop)
                break

            print("Zwischenstand - Monstereben:", self._kampfwerte[2], "Heldleben: ", held.getle())  # Testausgabe

        return held
