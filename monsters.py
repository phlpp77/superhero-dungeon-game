from items import *
from monster import *

class Nomonster(Monster):
    def __init__(self):
        Monster.__init__(self,10100,'',True,False,'gfxitems/noitem.gif',(0,0,0,0,0,0,0,0,0,0,Noitem()))

class Ork1(Monster):
    def __init__(self):
        Monster.__init__(self,10101,'Ork',False,False,'gfxmnstr/ork1.gif',(0,11,9,25,1,4,0,0,2,20,Noitem()))

