from math import *
from items import *
import time


class Held:

    def __init__(self,name):
        self._heldenname = name
        self._heldentyp = 0                                     # 0 Batman; 1 Superman; 2 Ironman; 3 Heiler
        self._geschlecht = 0                                    # 0 maennlich; 1 weiblich
        self._typname = 'Batman'                                # Typ des Helden
        self._eigenschaften = [11,11,10,11,10,11,10,10]         # MU KL CH IN FF GE KO KK
        self._kampfwerte = [11,11,165]                         # AT PA LeP
        self._maxle=self._kampfwerte[2]                         # LeP-Maximum
        self._bild = 'gfxhelden/Batman.gif'
        self._anzeigeBild = 'gfxhelden/Batman0.gif'
        self._x=0
        self._y=0
        self._lichtradius = 1.0
        self._itemliste = [Schwert(),Wattierterwaffenrock()]    # leere Liste, in der alle Items gespeichert sind
        self._waffe = self._itemliste[0]                        # Waffe
        self._ruestung = self._itemliste[1]                     # Ruestung
        self._ap = 0
        
    def getheldenname(self):
        return self._heldenname

    def setheldenname(self, name):
        self._heldenname = str(name)

    def getgeschlecht(self):
        return self._geschlecht

    def setgeschlecht(self,geschlecht):
        self._geschlecht = int(geschlecht)

    def getheldentyp(self):
        return self._heldentyp

    def gettypname(self):
        return self._typname

    def geteigenschaften(self):
        return self._eigenschaften

    def seteigenschaften(self,liste):
        self._eigenschaften = liste

    def geteigenschaft(self,pos):
        return self._eigenschaften[pos]

    def seteigenschaft(self,pos,wert):
        self._eigenschaften[pos] = wert

    def getkampfwerte(self):
        return self._kampfwerte

    def setkampfwerte(self,liste):
        self._kampfwerte = liste

    def getkampfwert(self,pos):
        return self._kampfwerte[pos]

    def setkampfwert(self,pos,wert):
        self._kampfwerte[pos] = wert

    def getwaffe(self):
        return self._waffe

    def setwaffe(self,waffe):
        self._waffe = waffe

    def getruestung(self):
        return self._ruestung

    def setruestung(self, ruestung):
        self._ruestung = ruestung

    def getbild(self):
        return self._bild

    def setbild(self, bild):
        self._bild = bild

    def getanzeigeBild(self):
        return self._anzeigeBild

    def getx(self):
        return self._x

    def setx(self,x):
        self._x = x

    def gety(self):
        return self._y

    def sety(self,y):
        self._y = y

    def ausleuchten(self):
        L=[(self._x,self._y)]
        self.fackelradius=1.0         # spaeter an anderer Stelle einfuegen, etwa beim Entzueden oder Besitzen einer Fackel
        maxr = self._lichtradius+self.fackelradius
        for i in range(int(8*maxr)):
            for r in range(int(maxr)):
                L=L+[( self._x+int(round((r+1)*cos(2*pi*(i+1)/(8*maxr)),0)) , self._y+int(round((r+1)*sin(2*pi*(i+1)/(8*maxr)),0)) )]
        return L

    def itemnehmen(self,it):        # nimmt das Item it in die Itemliste auf
        self._itemliste = self._itemliste + [it]

    def itemablegen(self,n):        # gibt das n-te Item aus der Itemliste zurueck
        if n < len(self._itemliste):
          it = self._itemliste[n]
        else:
          it = Noitem()
        return it

    def getitemliste(self):
        return self._itemliste

    def getap(self):
        return self._ap

    def addap(self,ap):
        self._ap = self._ap + ap

    def getmaxle(self):
        return self._maxle

    def setmaxle(self,maxle):
        self._maxle = maxle
    
    def getle(self):
        return self._kampfwerte[2]

    def setle(self,le):
        self._kampfwerte[2] = le

    def heilen(self,sp):
        self._kampfwerte[2] = self._kampfwerte[2]+ int( sp*(self._eigenschaften[4]+self._eigenschaften[6])/40 )
        if self._kampfwerte[2]>self._maxle:
            self._kampfwerte[2]=self.maxle

    def rennen(self, heldentyp):
        if heldentyp != 5:
            time.sleep(0.1)