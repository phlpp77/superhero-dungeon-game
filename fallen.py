from falle import *

class Nofalle(Falle):
    def __init__(self):
        Falle.__init__(self,20100,'',True,False,'gfxitems/noitem.gif',(0,0,0,0,0,0,0))

class Steinschlagfalle(Falle):
    def __init__(self):
        Falle.__init__(self,20101,'Steinschlagfalle',True,False,'gfxitems/steinschlagfalle.gif',(0,2,1,2,0,1,5))

