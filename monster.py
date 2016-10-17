from item import *
import random

class Monster(Item):
    
    def __init__(self,typ,name,begehbar,aufnehmbar,bild,werte):
        Item.__init__(self,typ,name,begehbar,aufnehmbar,bild,werte)   # Wert der Waffe in Silbertalern
        self._kampfwerte = [werte[1],werte[2],werte[3]] # AT PA LeP
        self._tp = (werte[4],werte[5])    # Wuerfel, Additiver Schaden
        self._mod = (werte[6],werte[7])   # AT-Modifkator, PA-Modifikator
        self._rs = werte[8]
        self._ap = werte[9]
        self._itemtodrop = werte[10]

    def getkampfwerte(self):
        return self._kampfwerte
        
    def gettp(self):
        return self._tp

    def getmod(self):
        return self._mod

    def benutzen(self,held):
        heldaltle = held.getle()
        while held.getkampfwerte()[2]>0 and self._kampfwerte[2]>0:
            tp = 0
            heldle = 0
            # Held schlaegt zu
            if random.randint(1,20)<=held.getkampfwerte()[0]+held.getwaffe().getmod()[0] and random.randint(1,20)>self._kampfwerte[1]+self._mod[1]:
                tp = held.getwaffe().gettp()[1]
                for i in range(held.getwaffe().gettp()[0]):
                    tp = tp + random.randint(1,6)
                if (tp - self._rs)>0:
                    print('Treffer Monster: LE',self._kampfwerte[2],'TP',tp,'RS',self._rs) # Testausgabe
                    self._kampfwerte[2] = self._kampfwerte[2] - (tp - self._rs)
            # Monster schlaegt zu
            if self._kampfwerte[2]>0 and random.randint(1,20)<=self._kampfwerte[0]+self._mod[0] and random.randint(1,20)>held.getkampfwerte()[1]+held.getwaffe().getmod()[1]:
                tp = self._tp[1]
                for i in range(self._tp[0]):
                    tp = tp + random.randint(1,6)
                if (tp - held.getruestung().getrs())>0:
                    heldle = held.getle() - (tp - held.getruestung().getrs())
                    held.setle(heldle)
            print (self._kampfwerte[2],held.getle()) # Testausgabe
            # Monster verschwindet bei LE<0
            if self._kampfwerte[2]<=0:
                self._typ = 0
                self._name = ''
                self._begehbar = True
                self._aufnehmbar = False
                self._bild = 'gfx/blank.gif'
                self._werte = (0,)
                print(heldaltle,held.getle(),'also',heldaltle-held.getle())
                held.heilen(heldaltle-held.getle())
                held.addap(self._ap)
                if self._itemtodrop.gettyp()!=0:
                    held.itemnehmen(self._itemtodrop)
            print(self._kampfwerte[2],held.getle()) # Testausgabe                
            
        return held
