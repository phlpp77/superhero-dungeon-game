from item import *

class Ruestung(Item):

    def __init__(self,typ,name,begehbar,aufnehmbar,bild,werte):
        Item.__init__(self,typ,name,begehbar,aufnehmbar,bild,werte)     # Wert der Ruestung   
        self._rs = werte[1] # Ruestungsschutz
       
    def getrs(self):
        return self._rs    
