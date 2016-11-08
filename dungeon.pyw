import time
import threading
from tkinter import *
import tkinter.ttk
from random import randint
from helden.held import *               #Batman
from helden.superman import *           #Superman
from helden.spiderman import *          #Spiderman
from helden.ironman import *            #Ironman
from helden.green_lantern import *      #Green Lantern
from helden.flash import *              #Flash
from level.dungeonebene import *
from level.dungeonebene01 import *
from level.dungeonebene02 import *
from level.dungeonebene03 import *

try:
    import winsound
except ImportError:
    winsound = None


# Flackern

class GUIThread(threading.Thread):
    def __init__(self, fenster):
        self.fenster = fenster
        self._stop = False
        threading.Thread.__init__ (self)

    def run(self):
        pass

    def stop(self):
        self._stop = True


class Flackern(GUIThread):
    def run(self):
          while not self._stop:
            time.sleep(0.2)
            self.fenster.wm_attributes('-alpha', 0.25)
            time.sleep(0.2)
            # print("Flacker!" + str(threading.get_ident()))
            self.fenster.wm_attributes('-alpha', 1)


class Musik(GUIThread):
    def run(self):
        while not self._stop:
            if winsound:
                winsound.PlaySound('music/sound.wav', winsound.SND_FILENAME)
            else:
                self.stop()


class LoadingBalken(threading.Thread):
    def __init__(self, progressbar, button):
        self.progressbar = progressbar
        self.button = button
        threading.Thread.__init__ (self)

    def run(self):
        for i in range(0, 90):
            self.progressbar.step()
            time.sleep(0.05)

        for i in range(0, 9):
            self.progressbar.step()
            time.sleep(0.5)

        self.button.pack(side=BOTTOM, anchor=E, padx=30, pady=30)


class Hauptprogramm:
    
    def __init__(self):
        self.fenster = Tk()
        self.fenster.title('Dungeon Game')
        self.fenster.minsize(600, 220)
        self.fenster.maxsize(600, 220)
        w = 600
        h = 220
        ws = self.fenster.winfo_screenwidth()
        hs = self.fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))     # Fenster mittig anordnen
        background_image = PhotoImage(file="gfx/bg.gif")
        background_label = Label(self.fenster, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.parallel = Flackern(self.fenster)
        self.parallel.setDaemon(True)
        self.parallel.start()
    
        self.label = Label(master=self.fenster,
                                         text='Dungeon Game',
                                         padx=30, pady=10,
                                         font=('Comic Sans MS',14),
                                         fg='red', bg='white')
        self.fenster.wm_attributes('-alpha', 0.5)
#        self.fenster.wm_attributes('-transparentcolor', 'white')
        self.neuesspiel_button = Button(master=self.fenster,text='Neues Spiel',
                                        command=self.einspieler,bg='white')
        
        self.label.pack()
        self.neuesspiel_button.pack()
        self.fenster.mainloop()

        
    def einspieler(self):
        self.heldenwahl()

        
        
# Heldenwahl

    def heldenwahl(self):
        self.parallel.stop()
        self.heldenwahl_fenster = Toplevel()
        self.heldenwahl_fenster.title('Dungeon Game')
        self.heldenwahl_fenster.minsize(600,320)
        self.heldenwahl_fenster.maxsize(600,320)
        w = 600
        h = 320
        ws = self.heldenwahl_fenster.winfo_screenwidth()
        hs = self.heldenwahl_fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.heldenwahl_fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.heldenwahl_fenster.config(bg='darkgray')
    
        self.label = Label(master=self.heldenwahl_fenster,
                                         text='Heldenauswahl',
                                         padx=30, pady=10,
                                         font=('Comic Sans MS',14),
                                         fg='white',bg='darkgray')
        self.radiogroup = Frame(master=self.heldenwahl_fenster,relief=RIDGE,
                                bd=2,bg='darkgray')
        self.auswahl = StringVar()
        self.auswahl.set(0)
        self.batman_radiobutton = Radiobutton(master=self.radiogroup,
                                              text='Batman',
                                              font=('Comic Sans MS',10),
                                              bg='darkgray',
                                              value='Batman', variable=self.auswahl,
                                              command=self.aktualisiere_beschreibung)
        self.batman_radiobutton.select()
        self.superman_radiobutton = Radiobutton(master=self.radiogroup,
                                              text='Superman',
                                              font=('Comic Sans MS',10),
                                              bg='darkgray',
                                              value='Superman', variable=self.auswahl,
                                              command=self.aktualisiere_beschreibung)
        self.spiderman_radiobutton = Radiobutton(master=self.radiogroup,
                                              text='Spiderman',
                                              font=('Comic Sans MS',10),
                                              bg='darkgray',
                                              value='Spiderman', variable=self.auswahl,
                                              command=self.aktualisiere_beschreibung)
        self.ironman_radiobutton = Radiobutton(master=self.radiogroup,
                                              text='Ironman',
                                              font=('Comic Sans MS',10),
                                              bg='darkgray',
                                              value='Ironman', variable=self.auswahl,
                                              command=self.aktualisiere_beschreibung)
        self.green_lantern_radiobutton = Radiobutton(master=self.radiogroup,
                                              text='Green Lantern',
                                              font=('Comic Sans MS',10),
                                              bg='darkgray',
                                              value='Green_Lantern', variable=self.auswahl,
                                              command=self.aktualisiere_beschreibung)
        self.flash_radiobutton = Radiobutton(master=self.radiogroup,
                                              text='Flash',
                                              font=('Comic Sans MS',10),
                                              bg='darkgray',
                                              value='Flash', variable=self.auswahl,
                                              command=self.aktualisiere_beschreibung)
        
        self.weiter_button = Button(master=self.radiogroup,text='weiter',
                               command=self.heldenwahl_beenden,bg='darkgray')
        self.beschreibung = Text(master=self.heldenwahl_fenster, width=50,
                                 height=8, wrap=WORD, font=('Comic Sans MS',10))

        self.aktualisiere_beschreibung()

        self.label.pack()
        self.radiogroup.pack(side=LEFT, padx = 5, pady = 5)
        self.batman_radiobutton.pack(anchor=W)
        self.superman_radiobutton.pack(anchor=W)
        self.spiderman_radiobutton.pack(anchor=W)
        self.ironman_radiobutton.pack(anchor=W)
        self.green_lantern_radiobutton.pack(anchor=W)
        self.flash_radiobutton.pack(anchor=W)
        
        self.weiter_button.pack(anchor=S, padx = 5, pady = 5, fill=X)
        self.beschreibung.pack(side=RIGHT, padx = 5 , pady = 5)
        self.heldenwahl_fenster.mainloop()

    def aktualisiere_beschreibung(self):
        self.beschreibung.delete(1.0,END)
        dateiname = os.path.join("helden", self.auswahl.get()+'.txt')
        daten=open(dateiname, "r", encoding="iso-8859-15")
        textdaten=daten.read()
        daten.close
        self.beschreibung.insert(1.0,textdaten)        

    def heldenwahl_beenden(self):
        if self.auswahl.get()=='Superman':
            self.held = Superman('Bitte Name eingeben')
        elif self.auswahl.get()=='Spiderman':
            self.held = Spiderman('Bitte Name eingeben')
        elif self.auswahl.get()=='Ironman':
            self.held = Ironman('Bitte Name eingeben')
        elif self.auswahl.get()=='Green_Lantern':
            self.held = Green_Lantern('Bitte Name eingeben')
        elif self.auswahl.get()=='Flash':
            self.held = Flash('Bitte Name eingeben')
        else:
            self.held = Held('Bitte Name eingeben')
        self.heldenwahl_fenster.destroy()
        self.heldbenennen()

# Held benennen

    def heldbenennen(self):
        self.heldbenennen_fenster = Toplevel()
        self.heldbenennen_fenster.title('Dungeon Game')
        self.heldbenennen_fenster.minsize(220,220)
        self.heldbenennen_fenster.maxsize(220,220)
        w = 220
        h = 220
        ws = self.heldbenennen_fenster.winfo_screenwidth()
        hs = self.heldbenennen_fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.heldbenennen_fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.heldbenennen_fenster.config(bg='darkgray')
    
        self.label = Label(master=self.heldbenennen_fenster,
                                         text='Held benennen',
                                         padx=30, pady=10,
                                         font=('Comic Sans MS',14),
                                         fg='white',bg='darkgray')
        self.eingabefeld = Entry(self.heldbenennen_fenster)
        self.eingabefeld.insert(END,self.held.getheldenname())
        self.auswahlgeschlecht = StringVar()
        self.maennlich = Radiobutton(master=self.heldbenennen_fenster,
                                     text='maennlich',
                                     font=('Comic Sans MS',10),
                                     bg='darkgray',
                                     value='0',
                                     variable=self.auswahlgeschlecht)
        self.weiblich = Radiobutton(master=self.heldbenennen_fenster,
                                     text='weiblich',
                                     font=('Comic Sans MS',10),
                                     bg='darkgray',
                                     value='1',
                                     variable=self.auswahlgeschlecht)
        self.maennlich.select()
        self.weiter_button = Button(master=self.heldbenennen_fenster,text='weiter',
                               command=self.heldbenennen_beenden,bg='darkgray')
        self.zurück_button = Button(master=self.heldbenennen_fenster,text='zurück',
                               command=self.heldenwahl_neustart,bg='darkgray')
        
        self.label.pack()
        self.eingabefeld.pack(padx = 30, fill=X)
        self.maennlich.pack(anchor=W, padx = 30, pady = 5)
        self.weiblich.pack(anchor=W, padx = 30, pady = 5)
        self.weiter_button.pack(side=BOTTOM,padx = 30, pady = 5, fill=X)
        self.zurück_button.pack(side=BOTTOM,padx = 30, pady = 5, fill=X)
        self.heldbenennen_fenster.mainloop()

    def heldenwahl_neustart(self):
        self.heldbenennen_fenster.destroy()
        self.heldenwahl()
        
    def heldbenennen_beenden(self):
        if self.eingabefeld.get() == "Bitte Name eingeben":
            self.held.setheldenname("Namenloser")
        else:
            self.held.setheldenname(self.eingabefeld.get())
        self.held.setgeschlecht(self.auswahlgeschlecht.get())
        self.heldbenennen_fenster.destroy()
        self.heldenzeigen()


# Held anzeigen

    def heldenzeigen(self):
        self.held_fenster = Toplevel()
        self.held_fenster.title('Dungeon Game')
        self.held_fenster.minsize(220,220)
        self.held_fenster.maxsize(220,220)
        w = 220
        h = 220
        ws = self.held_fenster.winfo_screenwidth()
        hs = self.held_fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.held_fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.held_fenster.config(bg='darkgray')
        bg_image = PhotoImage(file=self.held.getbild())
        bg_label = Label(self.held_fenster, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.weiter_button = Button(master=self.held_fenster,text='weiter',
                               command=self.heldenzeigen_beenden,bg='darkgray')
        self.zurück_button = Button(master=self.held_fenster,text='zurück',
                               command=self.wahl_neustart,bg='darkgray')
        self.weiter_button.pack(side=BOTTOM,padx = 30, pady = 5, fill=X)
        self.zurück_button.pack(side=BOTTOM,padx = 30, pady = 5, fill=X)
        self.held_fenster.mainloop()

    def wahl_neustart(self):
        self.heldbenennen_fenster.destroy()
        self.held_fenster.destroy()
        self.heldenwahl()

    def heldenzeigen_beenden(self):
        self.held_fenster.destroy()
        self.spielfeldzeigen(1)

        
# Spielfeld anzeigen

    def spielfeldzeigen(self, levelnr):
        self.spielfeld_fenster = Toplevel()
        self.spielfeld_fenster.focus_force()
        self.spielfeld_fenster.title('Dungeon Game')
        self.spielfeld_fenster.minsize(1088, 684)
        self.spielfeld_fenster.maxsize(1088, 684)
        w = 1088
        h = 684
        ws = self.spielfeld_fenster.winfo_screenwidth()
        hs = self.spielfeld_fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.spielfeld_fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.spielfeld_fenster.config(bg='darkgray')

        self.music = Musik(self.fenster)
        self.music.setDaemon(True)
        self.music.start()

        self.canvas = Canvas(master=self.spielfeld_fenster, width=1088,
                             height=576)
        self.canvas.pack(padx=0,pady=0)

        if levelnr==1:                                  # laden des Levels nach Nummer
            self.d = Dungeonebene01(levelnr,self.held)
        elif levelnr==2:
            self.d = Dungeonebene02(levelnr,self.held)
        elif levelnr==3:
            self.d = Dungeonebene03(levelnr,self.held)
        #elif levelnr==4:
            #self.d = Dungeonebene04(levelnr,self.held)
        #elif levelnr==5:
           #self.d = Dungeonebene05(levelnr,self.held)
        #elif levelnr==6:
            #self.d = Dungeonebene06(levelnr,self.held)

        
        self.feldbild = list(range(self.d.getmaxx()))     # Anlegen eines Feldes, in dem alle Bilder des Dungeons (Wand, Boden) gespeichert sind
        for i in range(self.d.getmaxx()):
            self.feldbild[i]=list(range(self.d.getmaxy()))
        self.overlaybild = list(range(self.d.getmaxx()))     # Anlegen eines Feldes, in dem alle Bilder der Overlays gespeichert sind
        for i in range(self.d.getmaxx()):
            self.overlaybild[i]=list(range(self.d.getmaxy()))
        self.itembild = list(range(self.d.getmaxx()))     # Anlegen eines Feldes, in dem alle Bilder der Items gespeichert sind
        for i in range(self.d.getmaxx()):
            self.itembild[i]=list(range(self.d.getmaxy()))
        self.fogbild = list(range(self.d.getmaxx()))     # Anlegen eines Feldes, in dem alle Bilder des Fogs gespeichert sind: alle Bilder sind schwarz, werden dann beim Beleuchten per Held oder Schalter gelöscht
        for i in range(self.d.getmaxx()):
            self.fogbild[i]=list(range(self.d.getmaxy()))


        self.canvas_zeichnen()
        self.lightmap_aktualisieren()
        self.heldenstats_zeichnen()
        
        self.spielfeld_fenster.bind('<KeyPress-Left>', self.links)
        self.spielfeld_fenster.bind('<KeyPress-Right>', self.rechts)
        self.spielfeld_fenster.bind('<KeyPress-Up>', self.hoch)
        self.spielfeld_fenster.bind('<KeyPress-Down>', self.runter)
        self.spielfeld_fenster.bind('<KeyPress-a>', self.links)
        self.spielfeld_fenster.bind('<KeyPress-d>', self.rechts)
        self.spielfeld_fenster.bind('<KeyPress-w>', self.hoch)
        self.spielfeld_fenster.bind('<KeyPress-s>', self.runter)
        self.spielfeld_fenster.focus_set()
        self.spielfeld_fenster.mainloop()

    def canvas_zeichnen(self):
        for x in range(self.d.getmaxx()):
            for y in range(self.d.getmaxy()):
                self.feldbild[x][y] = PhotoImage(file=self.d.getbild(x,y),gamma=self.d.getlightmap(x,y))
                self.canvas.create_image(64*x+2,64*y+2,anchor=NW,
                                         image=self.feldbild[x][y])
                self.overlaybild[x][y] = PhotoImage(file=self.d.getoverlaybild(x,y),gamma=self.d.getlightmap(x,y))
                self.canvas.create_image(64*x+2,64*y+2,anchor=NW,
                                         image=self.overlaybild[x][y])
                self.itembild[x][y] = PhotoImage(file=self.d.getitembild(x,y),gamma=self.d.getlightmap(x,y))
                self.canvas.create_image(64*x+2,64*y+2,anchor=NW,
                                         image=self.itembild[x][y])
                self.fogbild[x][y] = PhotoImage(file='gfx/fog.gif',gamma=self.d.getlightmap(x,y))
                self.canvas.create_image(64*x+2,64*y+2,anchor=NW,
                                         image=self.fogbild[x][y])                            
        self.heldenbild = PhotoImage(file=self.held.getbild())  #Held zeichnen
        self.heldid=self.canvas.create_image(64*self.held.getx()+2,64*self.held.gety()+2,anchor=NW,
                                 image=self.heldenbild)    

    def canvas_aktualisieren(self): # alte Version - nicht benutzt
        for x in range(self.d.getmaxx()):
            for y in range(self.d.getmaxy()):
                self.feldbild[x][y].config(file=self.d.getbild(x,y))
                self.overlaybild[x][y].config(file=self.d.getoverlaybild(x,y))
                self.itembild[x][y].config(file=self.d.getitembild(x,y))
                if self.d.getfog(x,y):
                    self.fogbild[x][y].config(file='gfx/fog.gif')
                else:
                    self.fogbild[x][y].config(file='gfx/blank.gif')
        self.heldenbild.config(file=self.held.getbild())  #Held zeichnen

    def canvas_aktualisieren(self, x, y):
        for i in self.d.getschalter(x,y).getfelderliste():
                self.feldbild[i[0]][i[1]].config(file=self.d.getbild(i[0],i[1]))
                self.overlaybild[i[0]][i[1]].config(file=self.d.getoverlaybild(i[0],i[1]))
                self.itembild[i[0]][i[1]].config(file=self.d.getitembild(i[0],i[1]))
                if self.d.getfog(i[0],i[1]):
                    self.fogbild[i[0]][i[1]].config(file='gfx/fog.gif')
                else:
                    self.fogbild[i[0]][i[1]].config(file='gfx/blank.gif')
        self.heldenbild.config(file=self.held.getbild())  #Held zeichnen

    def lightmap_aktualisieren(self):
        # alle bekannten Felder werden verdunkelt: gamma=0.3
        for i in range(self.d.getmaxx()):
            for j in range(self.d.getmaxy()):
                if self.feldbild[i][j].cget('gamma')=='1.0':
                    self.feldbild[i][j].config(gamma=0.3)
                    self.overlaybild[i][j].config(gamma=0.3)                    
                    self.itembild[i][j].config(gamma=0.3)
        # alle Felder, die durch einen Schalter auf einen Lichtwert von 0.999 gesetzt wurden, werden vom Schatten befreit
                if self.d.getlightmap(i,j)==0.999:
                    self.fogbild[i][j].config(file='gfx/blank.gif')
                    self.d.setfog(i,j,False)
                    self.feldbild[i][j].config(gamma=0.999)
                    self.overlaybild[i][j].config(gamma=0.999)
                    self.itembild[i][j].config(gamma=0.999)                    
        # alle Felder im Lichtschein des Helden werden normal=ausgeleuchtet dargestellt: Gamma=1        
        for i in self.held.ausleuchten():
            if (i[0]>=0) and (i[0]<self.d.getmaxx()) and (i[1]>=0) and (i[1]<self.d.getmaxy()):
                self.fogbild[i[0]][i[1]].config(file='gfx/blank.gif')
                self.d.setfog(i[0],i[1],False)
                self.feldbild[i[0]][i[1]].config(gamma=1.0)
                self.overlaybild[i[0]][i[1]].config(gamma=1.0)                
                self.itembild[i[0]][i[1]].config(gamma=1.0)
                if self.d.getitem(i[0],i[1]).gettyp()>20100 and self.d.getitem(i[0],i[1]).gettyp()<20200: # wenn das Item des ausgeleuchteten Feldes eine Falle ist, wird deren entdeckt()-Methode aufgerufen
                    self.d.getitem(i[0],i[1]).entdecken(self.held)
                    self.itembild[i[0]][i[1]].config(file=self.d.getitembild(i[0],i[1]))

    def heldenstats_zeichnen(self):
        self.statsframe1 = Frame(master=self.spielfeld_fenster,relief=FLAT,
                                bd=2,bg='darkgray')
        self.statsframe2 = Frame(master=self.spielfeld_fenster,relief=FLAT,
                                bd=2,bg='darkgray')
        self.labelheldenname = Label(master=self.statsframe1,text=self.held.getheldenname(),
                        bg = 'darkgray', fg = 'white', width=20, pady=2, font=('Comic Sans MS',10))       
        self.labelmu = Label(master=self.statsframe1,text='MU: '+str(self.held.geteigenschaften()[0]),
                        bg = 'darkgray', fg = 'white', width=6, pady=2, font=('Comic Sans MS',10))
        self.labelkl = Label(master=self.statsframe1,text='KL: '+str(self.held.geteigenschaften()[1]),
                        bg = 'darkgray', fg = 'white', width=6, pady=2, font=('Comic Sans MS',10))
        self.labelch = Label(master=self.statsframe1,text='CH: '+str(self.held.geteigenschaften()[2]),
                        bg = 'darkgray', fg = 'white', width=6, pady=2, font=('Comic Sans MS',10))
        self.labelin = Label(master=self.statsframe1,text='IN: '+str(self.held.geteigenschaften()[3]),
                        bg = 'darkgray', fg = 'white', width=6, pady=2, font=('Comic Sans MS',10))
        self.labelff = Label(master=self.statsframe1,text='FF: '+str(self.held.geteigenschaften()[4]),
                        bg = 'darkgray', fg = 'white', width=6, pady=2, font=('Comic Sans MS',10))
        self.labelge = Label(master=self.statsframe1,text='GE: '+str(self.held.geteigenschaften()[5]),
                        bg = 'darkgray', fg = 'white', width=6, pady=2, font=('Comic Sans MS',10))
        self.labelko = Label(master=self.statsframe1,text='KO: '+str(self.held.geteigenschaften()[6]),
                        bg = 'darkgray', fg = 'white', width=6, pady=2, font=('Comic Sans MS',10))
        self.labelkk = Label(master=self.statsframe1,text='KK: '+str(self.held.geteigenschaften()[7]),
                        bg = 'darkgray', fg = 'white', width=6, pady=2, font=('Comic Sans MS',10))
        self.labeltypname = Label(master=self.statsframe2,text=self.held.gettypname(),
                        bg = 'darkgray', fg = 'white', width=20, pady=2, font=('Comic Sans MS',10))
        self.labelat = Label(master=self.statsframe2,text='AT: '+str(self.held.getkampfwerte()[0]+self.held.getwaffe().getmod()[0]),
                        bg = 'darkgray', fg = 'white', width=6, pady=2, font=('Comic Sans MS',10))
        self.labelpa = Label(master=self.statsframe2,text='PA: '+str(self.held.getkampfwerte()[1]+self.held.getwaffe().getmod()[1]),
                        bg = 'darkgray', fg = 'white', width=6, pady=2, font=('Comic Sans MS',10))
        self.labelle = Label(master=self.statsframe2,text='LE: '+str(self.held.getkampfwerte()[2])+'/'+str(self.held.getmaxle()),
                        bg = 'darkgray', fg = 'white', width=12, pady=2, font=('Comic Sans MS',10))
        self.labelrs = Label(master=self.statsframe2,text='RS: '+str(self.held.getruestung().getrs()),
                        bg = 'darkgray', fg = 'white', width=6, pady=2, font=('Comic Sans MS',10))
        

        self.statsframe1.pack(anchor=NW,pady = 2)
        self.statsframe2.pack(anchor=NW,pady = 2)        
        self.labelheldenname.pack(anchor=NW,side=LEFT)
        self.labelmu.pack(anchor=NW,side=LEFT)
        self.labelkl.pack(anchor=NW,side=LEFT)
        self.labelch.pack(anchor=NW,side=LEFT)
        self.labelin.pack(anchor=NW,side=LEFT)
        self.labelff.pack(anchor=NW,side=LEFT)
        self.labelge.pack(anchor=NW,side=LEFT)
        self.labelko.pack(anchor=NW,side=LEFT)
        self.labelkk.pack(anchor=NW,side=LEFT)
        self.labeltypname.pack(anchor=NW,side=LEFT)
        self.labelat.pack(anchor=NW,side=LEFT)
        self.labelpa.pack(anchor=NW,side=LEFT)
        self.labelle.pack(anchor=NW,side=LEFT)
        self.labelrs.pack(anchor=NW,side=LEFT)        
        
    def heldenstats_aktualisieren(self):
        self.labelmu.config(text='MU: '+str(self.held.geteigenschaften()[0]))
        self.labelkl.config(text='KL: '+str(self.held.geteigenschaften()[1]))
        self.labelch.config(text='CH: '+str(self.held.geteigenschaften()[2]))
        self.labelin.config(text='IN: '+str(self.held.geteigenschaften()[3]))
        self.labelff.config(text='FF: '+str(self.held.geteigenschaften()[4]))
        self.labelge.config(text='GE: '+str(self.held.geteigenschaften()[5]))
        self.labelko.config(text='KO: '+str(self.held.geteigenschaften()[6]))
        self.labelkk.config(text='KK: '+str(self.held.geteigenschaften()[7]))
        self.labelat.config(text='AT: '+str(self.held.getkampfwerte()[0]+self.held.getwaffe().getmod()[0]))
        self.labelpa.config(text='PA: '+str(self.held.getkampfwerte()[1]+self.held.getwaffe().getmod()[1]))
        self.labelle.config(text='LE: '+str(self.held.getkampfwerte()[2])+'/'+str(self.held.getmaxle()))
        self.labelrs.config(text='RS: '+str(self.held.getruestung().getrs()))

    def endScreen(self):

        self.end_fenster = Toplevel()
        self.end_fenster.focus_force()
        self.end_fenster.title('Dungeon Game - Du hast gewonnen!')
        self.end_fenster.minsize(1088, 567)
        self.end_fenster.maxsize(1088, 567)
        w = 1088
        h = 567
        ws = self.end_fenster.winfo_screenwidth()
        hs = self.end_fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.end_fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.end_fenster.config(bg='darkgray')
        bg = PhotoImage(file="gfx/endScreen.gif")
        bl = Label(self.end_fenster, image=bg)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        self.end_fenster.mainloop()

    def loadingScreen(self):

        self.loading_fenster = Toplevel()
        self.loading_fenster.focus_force()
        self.loading_fenster.title('Dungeon Game - loading...')
        self.loading_fenster.minsize(1088, 567)
        self.loading_fenster.maxsize(1088, 567)
        w = 1088
        h = 567
        ws = self.loading_fenster.winfo_screenwidth()
        hs = self.loading_fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.loading_fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.loading_fenster.config(bg='darkgray')
        bg = PhotoImage(file="gfx/loadingScreen.gif")
        bl = Label(self.loading_fenster, image=bg)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        #test = Label(master=self.loading_fenster, text="test text" )
        #test.pack()
        progressbar = tkinter.ttk.Progressbar(master=self.loading_fenster, orient=HORIZONTAL, length=200, mode='determinate')
        progressbar.pack(side="bottom")

        w_button = Button(master=self.loading_fenster, text='weiter', command=self.loading_beenden, bg='white')

        balken = LoadingBalken(progressbar, w_button)
        balken.setDaemon(True)
        balken.start()

        tippslist = []
        tippstxt = open("tipps/tipps.txt", "r", encoding="iso-8859-15")
        for line in tippstxt:
            tippslist.append(line)
        tippstxt.close()
        tipps = Label(master=self.loading_fenster, text=tippslist[randint(0,len(tippslist)-1)],
                                         padx=30, pady=10,
                                         font=('Comic Sans MS',14),
                                         fg='black', bg='white')
        tipps.pack()

        self.loading_fenster.mainloop()

    def loading_beenden(self):
        self.loading_fenster.destroy()
        self.spielfeldzeigen(self.d.getlevelnr() + 1)

    def bildrichtung_aktualisieren(self, direction):
        if direction == 1:
            self.held.setbild(os.path.join("gfxhelden", self.held.gettypname()+"W.gif"))
        elif direction == 2:
            self.held.setbild(os.path.join("gfxhelden", self.held.gettypname()+"D.gif"))
        elif direction == 3:
            self.held.setbild(os.path.join("gfxhelden", self.held.gettypname()+"A.gif"))
        elif direction == 4:
            self.held.setbild(os.path.join("gfxhelden", self.held.gettypname()+".gif"))
        self.heldenbild.config(file=self.held.getbild())

    def links(self, event):
        self.held.rennen(self.held.getheldentyp())
        self.bildrichtung_aktualisieren(3)
        if (self.held.getx()>0):
            self.d = self.d.getschalter(self.held.getx()-1,self.held.gety()).ausloesen(self.d)
            if self.d.getschalter(self.held.getx()-1,self.held.gety()).getschaltertyp()!=0:
                self.canvas_aktualisieren(self.held.getx()-1, self.held.gety())
            self.held = self.d.getfeld(self.held.getx()-1,self.held.gety()).betreten(self.held)
            self.itembild[self.held.getx()-1][self.held.gety()].config(file=self.d.getfeld(self.held.getx()-1,self.held.gety()).getitembild())
            if (self.d.getbegehbar(self.held.getx()-1,self.held.gety())):
                self.canvas.move(self.heldid,-64,0)
                self.held.setx(self.held.getx()-1)
            self.lightmap_aktualisieren()
            self.heldenstats_aktualisieren()
# wenn held.le > 0, dann held tot mit fenster
            if self.held.getle()<=0:
                self.spielfeld_fenster.destroy()
# Heldtotschirm aufrufen              
            if self.d.getlevelende():
                self.spielfeld_fenster.destroy()
                self.loadingScreen()
            if self.d.getspielende():
                self.spielfeld_fenster.destroy()
                self.endScreen()
# Spielendschirm aufrufen                    
            
    def rechts(self,event):
        self.held.rennen(self.held.getheldentyp())
        self.bildrichtung_aktualisieren(2)
        if (self.held.getx()<self.d.getmaxx()):
            self.d = self.d.getschalter(self.held.getx()+1,self.held.gety()).ausloesen(self.d)
            if self.d.getschalter(self.held.getx()+1,self.held.gety()).getschaltertyp()!=0:
                self.canvas_aktualisieren(self.held.getx()+1, self.held.gety())
            self.held = self.d.getfeld(self.held.getx()+1,self.held.gety()).betreten(self.held)
            self.itembild[self.held.getx()+1][self.held.gety()].config(file=self.d.getfeld(self.held.getx()+1,self.held.gety()).getitembild())
            if (self.d.getbegehbar(self.held.getx()+1,self.held.gety())):
                self.canvas.move(self.heldid,64,0)
                self.held.setx(self.held.getx()+1)
            self.lightmap_aktualisieren()
            self.heldenstats_aktualisieren()
# wenn held.le > 0, dann held tot mit fenster
            if self.held.getle()<=0:
                self.spielfeld_fenster.destroy()
# Heldtotschirm aufrufen              
            if self.d.getlevelende():
                self.spielfeld_fenster.destroy()
                self.loadingScreen()
            if self.d.getspielende():
                self.spielfeld_fenster.destroy()
                self.endScreen()
# Spielendschirm aufrufen
                    
    def hoch(self,event):
        self.held.rennen(self.held.getheldentyp())
        self.bildrichtung_aktualisieren(1)
        if (self.held.gety()>0):
            self.d = self.d.getschalter(self.held.getx(),self.held.gety()-1).ausloesen(self.d)
            if self.d.getschalter(self.held.getx(),self.held.gety()-1).getschaltertyp()!=0:
                self.canvas_aktualisieren(self.held.getx(),self.held.gety()-1)
            self.held = self.d.getfeld(self.held.getx(),self.held.gety()-1).betreten(self.held)
            self.itembild[self.held.getx()][self.held.gety()-1].config(file=self.d.getfeld(self.held.getx(),self.held.gety()-1).getitembild())
            if (self.d.getbegehbar(self.held.getx(),self.held.gety()-1)):
                self.canvas.move(self.heldid,0,-64)
                self.held.sety(self.held.gety()-1)
            self.lightmap_aktualisieren()
            self.heldenstats_aktualisieren()
# wenn held.le > 0, dann held tot mit fenster
            if self.held.getle()<=0:
                self.spielfeld_fenster.destroy()
# Heldtotschirm aufrufen              
            if self.d.getlevelende():
                self.spielfeld_fenster.destroy()
                self.loadingScreen()
            if self.d.getspielende():
                self.spielfeld_fenster.destroy()
                self.endScreen()
# Spielendschirm aufrufen                    
            
    def runter(self,event):
        self.held.rennen(self.held.getheldentyp())
        self.bildrichtung_aktualisieren(4)
        if self.held.gety()<self.d.getmaxy():
            self.d = self.d.getschalter(self.held.getx(),self.held.gety()+1).ausloesen(self.d)            
            if self.d.getschalter(self.held.getx(),self.held.gety()+1).getschaltertyp()!=0:
                self.canvas_aktualisieren(self.held.getx(),self.held.gety()+1)
            self.held = self.d.getfeld(self.held.getx(),self.held.gety()+1).betreten(self.held)
            self.itembild[self.held.getx()][self.held.gety()+1].config(file=self.d.getfeld(self.held.getx(),self.held.gety()+1).getitembild())
            if self.d.getbegehbar(self.held.getx() ,self.held.gety()+1):
                self.canvas.move(self.heldid,0,64)
                self.held.sety(self.held.gety()+1)
            self.lightmap_aktualisieren()
            self.heldenstats_aktualisieren()
# wenn held.le > 0, dann held tot mit fenster
            if self.held.getle()<=0:
                self.spielfeld_fenster.destroy()
# Heldtotschirm aufrufen              
            if self.d.getlevelende():
                self.spielfeld_fenster.destroy()
                self.loadingScreen()
            if self.d.getspielende():
                self.spielfeld_fenster.destroy()
                self.endScreen()
# Spielendschirm aufrufen

# Spiel
spiel = Hauptprogramm()
