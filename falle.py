from item import *
import random


class Falle(Item):

    def __init__(self, typ, name, begehbar, aufnehmbar, bild, werte):
        Item.__init__(self, typ, name, begehbar, aufnehmbar, 'gfxitems/noitem.gif',
                      werte)  # Werte[0] des Items in Silbertalern
        self._realbild = bild
        self._schongespaeht = False
        self._entdeckenerschwernis = werte[1]
        self._tp = (werte[2], werte[3])
        self._ausweichenerschwernis = werte[4]
        self._ausloesbar = werte[5]
        self._ap = werte[6]

    def entdecken(self, held):
        if not self._schongespaeht:         # nur beim ersten Aufruf wird geprueft, ob die Falle entdeckt wird,
                                            # damit die Wahrscheinlichkeit nicht durch wiederholten betreten steigt
            if held.getheldentyp == 2:      # beim Dieb gibt es einen Bonus von 3=15% auf das Entdecken
                if random.randint(1, 20) <= held.geteigenschaften()[3] - self._entdeckenerschwernis + 3:
                    print('Dieb')
                    self._bild = self._realbild
            else:  # fuer alle anderen Helden ohne Bonus
                print('Y')
                if random.randint(1, 20) <= held.geteigenschaften()[3] - self._entdeckenerschwernis:
                    print('X')
                    self._bild = self._realbild
        self._schongespaeht = True

    def benutzen(self, held):
        self._bild = self._realbild
        if self._ausloesbar > 0:
            heldaltle = held.getle()
            if held.getheldentyp == 2:  # beim Dieb gibt es einen Bonus von 3=15% auf das Ausweichen
                if random.randint(1, 20) <= held.geteigenschaften()[5] - self._ausweichenerschwernis + 3:
                    tp = self._tp[1]
                    for i in range(self._tp[0]):
                        tp = tp + random.randint(1, 6)
                    if (tp - held.getruestung().getrs()) > 0:
                        heldle = held.getle() - (tp - held.getruestung().getrs())
                        held.setle(heldle)
            else:  # fuer alle anderen Helden ohne Bonus
                if random.randint(1, 20) <= held.geteigenschaften()[5] - self._ausweichenerschwernis:
                    tp = self._tp[1]
                    for i in range(self._tp[0]):
                        tp = tp + random.randint(1, 6)
                    if (tp - held.getruestung().getrs()) > 0:
                        heldle = held.getle() - (tp - held.getruestung().getrs())
                        held.setle(heldle)
            self._ausloesbar = self._ausloesbar - 1
            held.heilen(heldaltle - held.getle())
            held.addap(self._ap)
        return held
