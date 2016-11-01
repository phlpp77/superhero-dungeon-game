from items import *
from schalters import *
from monsters import *
from fallen import *

class Feld:

    def __init__(self,level,feldtyp,lightmap,overlaytyp,itemtyp,schaltertyp):
        self.level = level
        if feldtyp==0:                  # je nach feldtyp (aus der Datendatei), wird eine bestimmte Bodenkachel angelegt
            self._begehbar = False      # Wand
            self._bodenbild = 'gfxlvl'+str(self.level)+'/wand.gif'
        elif feldtyp==1:
            self._begehbar = True       # einfacher Boden
            self._bodenbild = 'gfxlvl'+str(self.level)+'/boden.gif'
        elif feldtyp==254:
            self._begehbar = True       # Einstieg
            self._bodenbild = 'gfxlvl'+str(self.level)+'/boden.gif'
        elif feldtyp==255:
            self._begehbar = True       # Ausgang
            self._bodenbild = 'gfxlvl'+str(self.level)+'/boden.gif'
        self._lightmap=lightmap
        self._fog=True

        if overlaytyp==0:
            self._overlaybild = 'gfxoverlay/nooverlay.gif'
        elif overlaytyp==41:  # 4x Steine: 41 kleiner Stein unten links
            self._overlaybild = 'gfxoverlay/41stein.gif'
        elif overlaytyp==51:  # Fackel
            self._overlaybild = 'gfxoverlay/51fackel.gif'
        elif overlaytyp==61:  # 6x Skelettteile: 61 Schaedel unten links
            self._overlaybild = 'gfxoverlay/61skelett.gif'

        if itemtyp==0:
            self._item = Noitem()
        elif itemtyp==101:  # Dolch
            self._item = Dolch()
        elif itemtyp==902:  # Teleport aus anderem Level -> zu Klasse wandeln
            self._item = Teleport2(self.level)
        elif itemtyp==911:  # Treppe nach unten ins naechste Level
            self._item = Treppe1(self.level)
        elif itemtyp==10101:    # Ork1
            self._item = Ork1()
        elif itemtyp==20101:    # Falle
            self._item = Steinschlagfalle()

        if schaltertyp[0]==0:
            self._schalter = Noschalter(schaltertyp[1])
        elif schaltertyp[0]==1:  # Levelende
            self._schalter = Levelendschalter(schaltertyp[1])
        elif schaltertyp[0]==2:  # Spielende
            self._schalter = Spielendschalter(schaltertyp[1])
        elif schaltertyp[0]==11:  # Spielende
            self._schalter = Lichtschalter(schaltertyp[1])
        elif schaltertyp[0]==21:  # Spielende
            self._schalter = Wandwegschalter(schaltertyp[1])

    def getbodenbild(self):
        return self._bodenbild

    def setbodenbild(self,bodenbild):
        self._bodenbild = bodenbild

    def getlightmap(self):
        return self._lightmap

    def setlightmap(self,wert):
        self._lightmap = wert

    def getfog(self):
        return self._fog

    def setfog(self,fog=True):
        self._fog = fog

    def getoverlaybild(self):
        return self._overlaybild
    
    def getitembild(self):
        return self._item.getbild()

    def getitemtyp(self):
        return self._itemtyp

    def getschaltertyp(self):
        return self._schaltertyp

    def getitem(self):
        return self._item

    def setitem(self,item):
        self._item = item

    def getschalter(self):
        return self._schalter

    def setitem(self,schalter):
        self._schalter = schalter
    
    def getbegehbar(self):
        return (self._begehbar and self._item.getbegehbar())

    def setbegehbar(self,begehbar):
        self._begehbar = begehbar
        
    def betreten(self,held):
        if self._item.getaufnehmbar():       
            held.itemnehmen(self._item)
            self._item = Noitem()
        else:
            
            self._item.benutzen(held)
        return held

    def itembenutzen(self,held):
        return self._item.benutzen(held)

    def schalterausloesen(self,dungeonebene):
        return self._schalter.ausloesen(dungeonebene)
