#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from item import *

class Waffe(Item):
    
    def __init__(self,typ,name,begehbar,aufnehmbar,bild,werte):
        Item.__init__(self,typ,name,begehbar,aufnehmbar,bild,werte)   # Werte[0] der Waffe in Silbertalern     
        self._tp = (werte[1],werte[2])    # Wuerfel, Additiver Schaden
        self._mod = (werte[3],werte[4])   # AT-Modifkator, PA-Modifikator
        
    def gettp(self):
        return self._tp

    def getmod(self):
        return self._mod

