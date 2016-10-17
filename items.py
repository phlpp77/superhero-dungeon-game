import os
from item import *
from waffe import *
from ruestung import *


#Sammlung der aufnehmbaren Items

class Noitem(Item):
    def __init__(self):
        Item.__init__(self,0,'',True,False,'gfxitems/noitem.gif',(0,))

class Dolch(Waffe):
    def __init__(self):
        Waffe.__init__(self,101,'Dolch',True,True,'gfxitems/dolch.gif',(25,1,2,0,0))

class Kurzschwert(Waffe):
    def __init__(self):
        Waffe.__init__(self,102,'Kurzschwert',True,True,'gfxitems/kurzschwert.gif',(40,1,3,0,0))

class Schwert(Waffe):
    def __init__(self):
        Waffe.__init__(self,103,'Schwert',True,True,'gfxitems/schwert.gif',(50,1,4,0,0))

class Langschwert(Waffe):
    def __init__(self):
        Waffe.__init__(self,104,'Langschwert',True,True,'gfxitems/langschwert.gif',(70,1,5,0,0))



class Kleidung(Ruestung):
    def __init__(self):
        Ruestung.__init__(self,201,'Kleidung',True,True,'gfxitems/kleidung.gif',(10,1))

class Wattierterwaffenrock(Ruestung):
    def __init__(self):
        Ruestung.__init__(self,202,'wattierter Waffenrock',True,True,'gfxitems/watwaffenrock.gif',(30,2))

class Kettenhemd(Ruestung):
    def __init__(self):
        Ruestung.__init__(self,203,'Kettenhemd',True,True,'gfxitems/kettenhemd.gif',(50,3))        


#Teleportpunkte

class Teleport2(Item):
    def __init__(self, levelnr):
        schatten_gif = os.path.join("gfxlvl" + str(levelnr), "teleportschatten.gif")
        Item.__init__(self,902,'Einstieg',True,False,schatten_gif,(0,))

class Treppe1(Item):
    def __init__(self, levelnr):
        treppe_gif = os.path.join("gfxlvl" + str(levelnr), "treppe.gif")
        Item.__init__(self,911,'Treppe in den naechsten Level',True,False,treppe_gif,(0,))


