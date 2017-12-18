import threading
import tkinter.ttk
import shelve
from random import randint
from tkinter import *

from helden.batman import *  # Batman
from helden.flash import *  # Flash
from helden.GreenLantern import *  # Green Lantern
from helden.ironman import *  # Ironman
from helden.spiderman import *  # Spiderman
from helden.superman import *  # Superman
# noinspection PyUnresolvedReferences
from level.dungeonebene01 import *
# noinspection PyUnresolvedReferences
from level.dungeonebene02 import *
# noinspection PyUnresolvedReferences
from level.dungeonebene03 import *
# noinspection PyUnresolvedReferences
from level.dungeonebene04 import *
# noinspection PyUnresolvedReferences
from level.dungeonebene05 import *
# noinspection PyUnresolvedReferences
from level.dungeonebene06 import *

try:
    import winsound
except ImportError:
    winsound = None
try:
    import pygame
except ImportError:
    pygame = None
    exit("Please install pygame http://www.pygame.org/download.shtml")


# Threading

class GUIThread(threading.Thread):
    def __init__(self, fenster):
        self.fenster = fenster
        self._stop = False
        threading.Thread.__init__(self)

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
        if pygame:
            pygame.mixer.init()
            pygame.mixer.music.load("music/sound.wav")
            pygame.mixer.music.play()
            if self._stop:
                pygame.mixer.music.stop()
        while not self._stop:
            if winsound:
                winsound.PlaySound('music/sound.wav', winsound.SND_FILENAME)
            else:
                self.stop()


class LoadingBalken(threading.Thread):
    def __init__(self, progressbar, button):
        self.progressbar = progressbar
        self.button = button
        threading.Thread.__init__(self)

    def run(self):  # TODO auf 0.05 und auf 0.5 später zurück ändern
        for i in range(0, 90):
            self.progressbar.step()
            time.sleep(0.0005)

        for i in range(0, 9):
            self.progressbar.step()
            time.sleep(0.005)

        self.button.pack(side=BOTTOM, anchor=E, padx=30, pady=30)


# ###########################################GUI:Startbildschirm############################################

class Hauptprogramm:

    def __init__(self):
        self.fenster = Tk()
        self.fenster.title('Dungeon Game')
        self.fenster.minsize(1088, 567)
        self.fenster.maxsize(1088, 567)
        w = 1088
        h = 567
        ws = self.fenster.winfo_screenwidth()
        hs = self.fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))  # Fenster mittig anordnen
        background_image = PhotoImage(file="gfx/titlescreen.gif")
        background_label = Label(self.fenster, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.parallel = Flackern(self.fenster)
        self.parallel.setDaemon(True)
        self.parallel.start()

        self.fenster.wm_attributes('-alpha', 0.5)
        self.neuesspiel_button = Button(master=self.fenster, text='START',
                                        command=self.einspieler, fg='white', bg='RED')
        self.neuesspiel_button.place(anchor=E, y=496, x=835)
        self.beenden_button = Button(master=self.fenster, text="ENDE",
                                     command=self.fenster.destroy, fg="white", bg="grey")
        self.beenden_button.place(anchor=E, y=528, x=829)
        self.fenster.mainloop()

    def einspieler(self):
        self.parallel.stop()
        Heldenwahl()


class Heldenwahl:

    def __init__(self):
        self.heldenwahl_fenster = Toplevel()
        self.heldenwahl_fenster.title('Dungeon Game')
        self.heldenwahl_fenster.minsize(600, 320)
        self.heldenwahl_fenster.maxsize(600, 320)
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
                           font=('Comic Sans MS', 14),
                           fg='white', bg='darkgray')
        self.radiogroup = Frame(master=self.heldenwahl_fenster, relief=RIDGE,
                                bd=2, bg='darkgray')
        self.auswahl = StringVar()
        self.auswahl.set(0)
        self.batman_radiobutton = Radiobutton(master=self.radiogroup,
                                              text='Batman',
                                              font=('Comic Sans MS', 10),
                                              bg='darkgray',
                                              value='Batman', variable=self.auswahl,
                                              command=self.aktualisiere_beschreibung)
        self.batman_radiobutton.select()
        self.superman_radiobutton = Radiobutton(master=self.radiogroup,
                                                text='Superman',
                                                font=('Comic Sans MS', 10),
                                                bg='darkgray',
                                                value='Superman', variable=self.auswahl,
                                                command=self.aktualisiere_beschreibung)
        self.spiderman_radiobutton = Radiobutton(master=self.radiogroup,
                                                 text='Spiderman',
                                                 font=('Comic Sans MS', 10),
                                                 bg='darkgray',
                                                 value='Spiderman', variable=self.auswahl,
                                                 command=self.aktualisiere_beschreibung)
        self.ironman_radiobutton = Radiobutton(master=self.radiogroup,
                                               text='Ironman',
                                               font=('Comic Sans MS', 10),
                                               bg='darkgray',
                                               value='Ironman', variable=self.auswahl,
                                               command=self.aktualisiere_beschreibung)
        self.GreenLantern_radiobutton = Radiobutton(master=self.radiogroup,
                                                    text='Green Lantern',
                                                    font=('Comic Sans MS', 10),
                                                    bg='darkgray',
                                                    value='GreenLantern', variable=self.auswahl,
                                                    command=self.aktualisiere_beschreibung)
        self.flash_radiobutton = Radiobutton(master=self.radiogroup,
                                             text='Flash',
                                             font=('Comic Sans MS', 10),
                                             bg='darkgray',
                                             value='Flash', variable=self.auswahl,
                                             command=self.aktualisiere_beschreibung)

        self.weiter_button = Button(master=self.radiogroup, text='weiter',
                                    command=self.heldenwahl_beenden, bg='darkgray')
        self.beschreibung = Text(master=self.heldenwahl_fenster, width=50,
                                 height=8, wrap=WORD, font=('Comic Sans MS', 10))

        self.aktualisiere_beschreibung()

        self.label.pack()
        self.radiogroup.pack(side=LEFT, padx=5, pady=5)
        self.batman_radiobutton.pack(anchor=W)
        self.superman_radiobutton.pack(anchor=W)
        self.spiderman_radiobutton.pack(anchor=W)
        self.ironman_radiobutton.pack(anchor=W)
        self.GreenLantern_radiobutton.pack(anchor=W)
        self.flash_radiobutton.pack(anchor=W)

        self.weiter_button.pack(anchor=S, padx=5, pady=5, fill=X)
        self.beschreibung.pack(side=RIGHT, padx=5, pady=5)
        self.heldenwahl_fenster.mainloop()

    def aktualisiere_beschreibung(self):
        self.beschreibung.delete(1.0, END)
        dateiname = os.path.join("helden", self.auswahl.get() + '.txt')
        daten = open(dateiname, "r", encoding="iso-8859-15")
        textdaten = daten.read()
        daten.close()
        self.beschreibung.insert(1.0, textdaten)

    def heldenwahl_beenden(self):
        global held
        text = "Bitten Name eingeben"
        switcher = {
            "Batman": Batman(text),
            "Superman": Superman(text),
            "Spiderman": Spiderman(text),
            "Ironman": Ironman(text),
            "GreenLantern": GreenLantern(text),
            "Flash": Flash(text)
        }
        held = switcher.get(self.auswahl.get())
        self.heldenwahl_fenster.destroy()
        HeldBenennen()


class HeldBenennen:

    def __init__(self):
        self.heldbenennen_fenster = Toplevel()
        self.heldbenennen_fenster.title('Dungeon Game')
        self.heldbenennen_fenster.minsize(220, 220)
        self.heldbenennen_fenster.maxsize(220, 220)
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
                           font=('Comic Sans MS', 14),
                           fg='white', bg='darkgray')
        self.eingabefeld = Entry(self.heldbenennen_fenster)
        self.eingabefeld.insert(END, held.getheldenname())
        self.auswahlgeschlecht = StringVar()
        self.maennlich = Radiobutton(master=self.heldbenennen_fenster,
                                     text='maennlich',
                                     font=('Comic Sans MS', 10),
                                     bg='darkgray',
                                     value='0',
                                     variable=self.auswahlgeschlecht)
        self.weiblich = Radiobutton(master=self.heldbenennen_fenster,
                                    text='weiblich',
                                    font=('Comic Sans MS', 10),
                                    bg='darkgray',
                                    value='1',
                                    variable=self.auswahlgeschlecht)
        self.maennlich.select()
        self.weiter_button = Button(master=self.heldbenennen_fenster, text='weiter',
                                    command=self.heldbenennen_beenden, bg='darkgray')
        self.zurueck_button = Button(master=self.heldbenennen_fenster, text='zurück',
                                     command=self.heldenwahl_neustart, bg='darkgray')

        self.label.pack()
        self.eingabefeld.pack(padx=30, fill=X)
        self.maennlich.pack(anchor=W, padx=30, pady=5)
        self.weiblich.pack(anchor=W, padx=30, pady=5)
        self.weiter_button.pack(side=BOTTOM, padx=30, pady=5, fill=X)
        self.zurueck_button.pack(side=BOTTOM, padx=30, pady=5, fill=X)
        self.heldbenennen_fenster.mainloop()

    def heldenwahl_neustart(self):
        self.heldbenennen_fenster.destroy()
        Heldenwahl()

    def heldbenennen_beenden(self):
        if self.eingabefeld.get() == "Bitte Name eingeben":
            held.setheldenname("Namenloser")
        else:
            held.setheldenname(self.eingabefeld.get())
        held.setgeschlecht(self.auswahlgeschlecht.get())
        self.heldbenennen_fenster.destroy()
        Heldenzeigen()


class Heldenzeigen:

    def __init__(self):
        self.held_fenster = Toplevel()
        self.held_fenster.title('Dungeon Game')
        self.held_fenster.minsize(220, 220)
        self.held_fenster.maxsize(220, 220)
        w = 220
        h = 220
        ws = self.held_fenster.winfo_screenwidth()
        hs = self.held_fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.held_fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.held_fenster.config(bg='darkgray')
        bg_image = PhotoImage(file=held.getanzeigeBild())
        bg_label = Label(self.held_fenster, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.weiter_button = Button(master=self.held_fenster, text='weiter',
                                    command=self.heldenzeigen_beenden, bg='darkgray')
        self.zurueck_button = Button(master=self.held_fenster, text='zurück',
                                     command=self.wahl_neustart, bg='darkgray')
        self.weiter_button.pack(side=BOTTOM, padx=30, pady=5, fill=X)
        self.zurueck_button.pack(side=BOTTOM, padx=30, pady=5, fill=X)
        self.held_fenster.mainloop()

    def wahl_neustart(self):
        self.held_fenster.destroy()
        Heldenwahl()

    def heldenzeigen_beenden(self):
        self.held_fenster.destroy()
        Spielfeldanzeigen(1, held)


# ###########################################GUI:Spielfeld############################################
# noinspection PyAttributeOutsideInit
class Spielfeldanzeigen:

    def __init__(self, levelnr, heldget):
        self.spielfeld_fenster = Toplevel()
        self.spielfeld_fenster.focus_force()
        self.spielfeld_fenster.title('Dungeon Game - Level ' + str(levelnr))
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

        self.music = Musik(self.spielfeld_fenster)
        self.music.setDaemon(True)
        self.music.start()

        self.canvas = Canvas(master=self.spielfeld_fenster, width=1088,
                             height=576)
        self.canvas.pack(padx=0, pady=0)

        global held
        held = heldget

        self.statsframe = Frame(master=self.spielfeld_fenster, relief=GROOVE, bd=3, bg="darkgrey")

        self.statsframe1 = Frame(master=self.statsframe, relief=FLAT,
                                 bd=2, bg='darkgray')
        self.statsframe2 = Frame(master=self.statsframe, relief=FLAT,
                                 bd=2, bg='darkgray')

        self.labelheldenname = Label(master=self.statsframe1, text=held.getheldenname(),
                                     bg='darkgray', fg='white', width=20, pady=2, font=('Comic Sans MS', 15))

        self.labeltypname = Label(master=self.statsframe2, text=held.gettypname(),
                                  bg='darkgray', fg='white', width=20, pady=2, font=('Comic Sans MS', 15))
        # Heldenstats initialisieren
        """self.labelmu = Label(master=self.statsframe1, text='MU: ' + str(held.geteigenschaften()[0]),
                             bg='darkgray', fg='white', width=6, pady=2, font=('Comic Sans MS', 13))
        self.labelkl = Label(master=self.statsframe1, text='KL: ' + str(held.geteigenschaften()[1]),
                             bg='darkgray', fg='white', width=6, pady=2, font=('Comic Sans MS', 13))
        self.labelch = Label(master=self.statsframe1, text='CH: ' + str(held.geteigenschaften()[2]),
                             bg='darkgray', fg='white', width=6, pady=2, font=('Comic Sans MS', 13))
        self.labelin = Label(master=self.statsframe1, text='IN: ' + str(held.geteigenschaften()[3]),
                             bg='darkgray', fg='white', width=6, pady=2, font=('Comic Sans MS', 13))
        self.labelff = Label(master=self.statsframe1, text='FF: ' + str(held.geteigenschaften()[4]),
                             bg='darkgray', fg='white', width=6, pady=2, font=('Comic Sans MS', 13))
        self.labelge = Label(master=self.statsframe1, text='GE: ' + str(held.geteigenschaften()[5]),
                             bg='darkgray', fg='white', width=6, pady=2, font=('Comic Sans MS', 13))
        self.labelko = Label(master=self.statsframe1, text='KO: ' + str(held.geteigenschaften()[6]),
                             bg='darkgray', fg='white', width=6, pady=2, font=('Comic Sans MS', 13))
        self.labelkk = Label(master=self.statsframe1, text='KK: ' + str(held.geteigenschaften()[7]),
                             bg='darkgray', fg='white', width=6, pady=2, font=('Comic Sans MS', 13))"""
        # amount_characteristics describes the number of labels that are characteristics (the rest are combat values)
        self.amount_characteristics, self.amount_combat_values = 8, 2
        self.label, self.labeltext = [], ["MU: ", "KL: ", "CH: ", "IN: ", "FF: ", "GE: ", "KO: ", "KK: ", "AT: ",
                                          "PA: ", "LE: ", "RS: "]
        # initialize characteristics
        for i in range(self.amount_characteristics):
            tmp_label = Label(master=self.statsframe1, text=self.labeltext[i] + str(held.geteigenschaften()[i]),
                              bg='darkgray', fg='white', width=6, pady=2, font=('Comic Sans MS', 13))
            self.label.append(tmp_label)

        # initialize combat values
        for i in range(self.amount_characteristics, self.amount_characteristics + self.amount_combat_values):
            tmp_label = Label(master=self.statsframe2,
                              text=self.labeltext[i] + str(
                                  held.getkampfwerte()[i - self.amount_characteristics] + held.getwaffe().getmod()[
                                      i - self.amount_characteristics]), bg='darkgray',
                              fg='white', width=6, pady=2, font=('Comic Sans MS', 13))
            self.label.append(tmp_label)

        # initialize life value
        self.label.append(Label(master=self.statsframe2,
                                text=self.labeltext[len(self.labeltext) - 2] + str(held.getkampfwerte()[2]) + '/' + str(
                                    held.getmaxle()),
                                bg='darkgray', fg='white', width=12, pady=2, font=('Comic Sans MS', 13)))
        # initialize armor
        self.label.append(Label(master=self.statsframe2,
                                text=self.labeltext[len(self.labeltext) - 1] + str(held.getruestung().getrs()),
                                bg='darkgray', fg='white', width=6, pady=2, font=('Comic Sans MS', 13)))

        functionsname = "Dungeonebene0" + str(levelnr) + "(levelnr, held)"  # Level Aufrufen
        global d
        d = eval(functionsname)

        self.feldbild = list(range(
            d.getmaxx()))  # Anlegen eines Feldes, in dem alle Bilder des Dungeons (Wand, Boden) gespeichert sind
        for i in range(d.getmaxx()):
            self.feldbild[i] = list(range(d.getmaxy()))
        self.overlaybild = list(
            range(d.getmaxx()))  # Anlegen eines Feldes, in dem alle Bilder der Overlays gespeichert sind
        for i in range(d.getmaxx()):
            self.overlaybild[i] = list(range(d.getmaxy()))
        self.itembild = list(
            range(d.getmaxx()))  # Anlegen eines Feldes, in dem alle Bilder der Items gespeichert sind
        for i in range(d.getmaxx()):
            self.itembild[i] = list(range(d.getmaxy()))
        self.fogbild = list(range(
            d.getmaxx()))  # Anlegen eines Feldes, in dem alle Bilder des Fogs gespeichert sind:
        # alle Bilder sind schwarz, werden dann beim Beleuchten per Held oder Schalter gelöscht
        for i in range(d.getmaxx()):
            self.fogbild[i] = list(range(d.getmaxy()))

        self.canvas_zeichnen()
        self.lightmap_aktualisieren()
        self.heldenstats_zeichnen()

        self.spielfeld_fenster.bind('<KeyPress-Left>', lambda event, a=3: self.bewegung(a))
        self.spielfeld_fenster.bind('<KeyPress-Right>', lambda event, a=2: self.bewegung(a))
        self.spielfeld_fenster.bind('<KeyPress-Up>', lambda event, a=1: self.bewegung(a))
        self.spielfeld_fenster.bind('<KeyPress-Down>', lambda event, a=4: self.bewegung(a))
        self.spielfeld_fenster.bind('<KeyPress-a>', lambda event, a=3: self.bewegung(a))
        self.spielfeld_fenster.bind('<KeyPress-d>', lambda event, a=2: self.bewegung(a))
        self.spielfeld_fenster.bind('<KeyPress-w>', lambda event, a=1: self.bewegung(a))
        self.spielfeld_fenster.bind('<KeyPress-s>', lambda event, a=4: self.bewegung(a))
        self.spielfeld_fenster.focus_set()
        self.spielfeld_fenster.mainloop()

    def canvas_zeichnen(self):
        for x in range(d.getmaxx()):
            for y in range(d.getmaxy()):
                self.feldbild[x][y] = PhotoImage(file=d.getbild(x, y), gamma=d.getlightmap(x, y))
                self.canvas.create_image(64 * x + 2, 64 * y + 2, anchor=NW,
                                         image=self.feldbild[x][y])
                self.overlaybild[x][y] = PhotoImage(file=d.getoverlaybild(x, y), gamma=d.getlightmap(x, y))
                self.canvas.create_image(64 * x + 2, 64 * y + 2, anchor=NW,
                                         image=self.overlaybild[x][y])
                self.itembild[x][y] = PhotoImage(file=d.getitembild(x, y), gamma=d.getlightmap(x, y))
                self.canvas.create_image(64 * x + 2, 64 * y + 2, anchor=NW,
                                         image=self.itembild[x][y])
                self.fogbild[x][y] = PhotoImage(file='gfx/fog.gif', gamma=d.getlightmap(x, y))
                self.canvas.create_image(64 * x + 2, 64 * y + 2, anchor=NW,
                                         image=self.fogbild[x][y])
        global heldenbild
        heldenbild = PhotoImage(file=held.getbild())  # Held zeichnen
        global heldid
        heldid = self.canvas.create_image(64 * held.getx() + 2, 64 * held.gety() + 2, anchor=NW,
                                          image=heldenbild)

    def canvas_aktualisieren(self, x, y):
        for i in d.getschalter(x, y).getfelderliste():
            self.feldbild[i[0]][i[1]].config(file=d.getbild(i[0], i[1]))
            self.overlaybild[i[0]][i[1]].config(file=d.getoverlaybild(i[0], i[1]))
            self.itembild[i[0]][i[1]].config(file=d.getitembild(i[0], i[1]))
            if d.getfog(i[0], i[1]):
                self.fogbild[i[0]][i[1]].config(file='gfx/fog.gif')
            else:
                self.fogbild[i[0]][i[1]].config(file='gfx/blank.gif')
        heldenbild.config(file=held.getbild())  # Held zeichnen

    def lightmap_aktualisieren(self):
        # alle bekannten Felder werden verdunkelt: gamma=0.3
        for i in range(d.getmaxx()):
            for j in range(d.getmaxy()):
                if self.feldbild[i][j].cget('gamma') == '1.0':
                    self.feldbild[i][j].config(gamma=0.3)
                    self.overlaybild[i][j].config(gamma=0.3)
                    self.itembild[i][j].config(gamma=0.3)
                # alle Felder, die durch einen Schalter auf einen Lichtwert von 0.999 gesetzt wurden,
                # werden vom Schatten befreit
                if d.getlightmap(i, j) == 0.999:
                    self.fogbild[i][j].config(file='gfx/blank.gif')
                    d.setfog(i, j, False)
                    self.feldbild[i][j].config(gamma=0.999)
                    self.overlaybild[i][j].config(gamma=0.999)
                    self.itembild[i][j].config(gamma=0.999)
                    # alle Felder im Lichtschein des Helden werden normal=ausgeleuchtet dargestellt: Gamma=1
        for i in held.ausleuchten():
            if (i[0] >= 0) and (i[0] < d.getmaxx()) and (i[1] >= 0) and (i[1] < d.getmaxy()):
                self.fogbild[i[0]][i[1]].config(file='gfx/blank.gif')
                d.setfog(i[0], i[1], False)
                self.feldbild[i[0]][i[1]].config(gamma=1.0)
                self.overlaybild[i[0]][i[1]].config(gamma=1.0)
                self.itembild[i[0]][i[1]].config(gamma=1.0)
                if 20100 < d.getitem(i[0], i[1]).gettyp() < 20200:
                    # wenn das Item des ausgeleuchteten Feldes eine Falle ist, wird deren entdeckt()-Methode aufgerufen
                    d.getitem(i[0], i[1]).entdecken(held)
                    self.itembild[i[0]][i[1]].config(file=d.getitembild(i[0], i[1]))

    def heldenstats_zeichnen(self):
        self.statsframe.pack(anchor=NW, pady=10, padx=2)
        self.statsframe1.pack(anchor=NW, pady=2)
        self.statsframe2.pack(anchor=NW, pady=2)
        self.labelheldenname.pack(anchor=NW, side=LEFT)
        self.labeltypname.pack(anchor=NW, side=LEFT)
        # packing characteristics and combat values
        for i in self.label:
            i.pack(anchor=NW, side=LEFT)

    def heldenstats_aktualisieren(self):
        # updating characteristics
        for i in range(self.amount_characteristics):
            self.label[i].config(text=self.labeltext[i] + str(held.geteigenschaften()[i]))

        # updating combat values
        for i in range(self.amount_characteristics, self.amount_characteristics + self.amount_combat_values):
            self.label[i].config(text=self.labeltext[i] + str(
                held.getkampfwerte()[i - self.amount_characteristics] + held.getwaffe().getmod()[
                    i - self.amount_characteristics]))

        # updating health and armor
        self.label[len(self.label) - 2].config(
            text=self.labeltext[len(self.labeltext) - 2] + str(held.getkampfwerte()[2]) + '/' + str(held.getmaxle()))
        self.label[len(self.label) - 1].config(
            text=self.labeltext[len(self.labeltext) - 1] + str(held.getruestung().getrs()))

    @staticmethod
    def bildrichtung_aktualisieren(direction):
        if direction == 1:
            held.setbild(os.path.join("gfxhelden", held.gettypname() + "W.gif"))
        elif direction == 2:
            held.setbild(os.path.join("gfxhelden", held.gettypname() + "D.gif"))
        elif direction == 3:
            held.setbild(os.path.join("gfxhelden", held.gettypname() + "A.gif"))
        elif direction == 4:
            held.setbild(os.path.join("gfxhelden", held.gettypname() + ".gif"))
        heldenbild.config(file=held.getbild())

    def bewegung(self, richtung):  # Richtung: 4=runter, 1=hoch, 2=rechts, 3=links
        # print(richtung)
        held.rennen(held.getheldentyp())
        self.bildrichtung_aktualisieren(richtung)

        if richtung == 4:
            if held.gety() < d.getmaxy():
                self.d = d.getschalter(held.getx(), held.gety() + 1).ausloesen(d)
                if self.d.getschalter(held.getx(), held.gety() + 1).getschaltertyp() != 0:
                    self.canvas_aktualisieren(held.getx(), held.gety() + 1)
                self.held = self.d.getfeld(held.getx(), held.gety() + 1).betreten(held)
                self.itembild[held.getx()][held.gety() + 1].config(
                    file=self.d.getfeld(held.getx(), held.gety() + 1).getitembild())
                if self.d.getbegehbar(held.getx(), held.gety() + 1):
                    self.canvas.move(heldid, 0, 64)
                    held.sety(held.gety() + 1)
        elif richtung == 3:
            if held.getx() > 0:
                self.d = d.getschalter(held.getx() - 1, held.gety()).ausloesen(d)
                if self.d.getschalter(held.getx() - 1, held.gety()).getschaltertyp() != 0:
                    self.canvas_aktualisieren(held.getx() - 1, held.gety())
                self.held = self.d.getfeld(held.getx() - 1, held.gety()).betreten(held)
                self.itembild[held.getx() - 1][held.gety()].config(
                    file=self.d.getfeld(held.getx() - 1, held.gety()).getitembild())
                if self.d.getbegehbar(held.getx() - 1, held.gety()):
                    self.canvas.move(heldid, -64, 0)
                    held.setx(held.getx() - 1)
        elif richtung == 2:
            if held.getx() < d.getmaxx():
                self.d = d.getschalter(held.getx() + 1, held.gety()).ausloesen(d)
                if self.d.getschalter(held.getx() + 1, held.gety()).getschaltertyp() != 0:
                    self.canvas_aktualisieren(held.getx() + 1, held.gety())
                self.held = self.d.getfeld(held.getx() + 1, held.gety()).betreten(held)
                self.itembild[held.getx() + 1][held.gety()].config(
                    file=self.d.getfeld(held.getx() + 1, held.gety()).getitembild())
                if self.d.getbegehbar(held.getx() + 1, held.gety()):
                    self.canvas.move(heldid, 64, 0)
                    held.setx(held.getx() + 1)
        else:
            if held.gety() > 0:
                self.d = d.getschalter(held.getx(), held.gety() - 1).ausloesen(d)
                if self.d.getschalter(held.getx(), held.gety() - 1).getschaltertyp() != 0:
                    self.canvas_aktualisieren(held.getx(), held.gety() - 1)
                self.held = self.d.getfeld(held.getx(), held.gety() - 1).betreten(held)
                self.itembild[held.getx()][held.gety() - 1].config(
                    file=self.d.getfeld(held.getx(), held.gety() - 1).getitembild())
                if self.d.getbegehbar(held.getx(), held.gety() - 1):
                    self.canvas.move(heldid, 0, -64)
                    held.sety(held.gety() - 1)

        self.lightmap_aktualisieren()
        self.heldenstats_aktualisieren()

        # wenn held.le > 0, dann held tot mit fenster
        if held.getle() <= 0:
            self.spielfeld_fenster.destroy()
            DeathScreen()

        # Heldtotschirm aufrufen
        if d.getlevelende():
            self.spielfeld_fenster.destroy()
            LoadingScreen()

        # Spielende Bildschirm aufrufen
        if d.getspielende():
            self.spielfeld_fenster.destroy()
            EndScreen()


class DeathScreen:

    def __init__(self):
        self.death_fenster = Toplevel()
        self.death_fenster.focus_force()
        self.death_fenster.title('Dungeon Game - Du bist gestorben!')
        self.death_fenster.minsize(1088, 567)
        self.death_fenster.maxsize(1088, 567)
        w = 1088
        h = 567
        ws = self.death_fenster.winfo_screenwidth()
        hs = self.death_fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.death_fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.death_fenster.config(bg='darkgray')
        bg = PhotoImage(file="gfx/deathScreen.gif")
        bl = Label(self.death_fenster, image=bg)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        self.death_fenster.mainloop()


class EndScreen:

    def __init__(self):
        self.end_fenster = Toplevel()
        self.end_fenster.focus_force()
        self.end_fenster.title('Dungeon Game - Vollversion kaufen!')
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


class LoadingScreen:

    def __init__(self):
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

        progressbar = tkinter.ttk.Progressbar(master=self.loading_fenster, orient=HORIZONTAL, length=200,
                                              mode='determinate')
        progressbar.pack(side="bottom")

        w_button = Button(master=self.loading_fenster, text='weiter',
                          command=lambda: self.loading_beenden(self.loading_fenster), bg='white')

        balken = LoadingBalken(progressbar, w_button)
        balken.setDaemon(True)
        balken.start()

        tippslist = []
        tippstxt = open("tipps/tipps.txt", "r", encoding="iso-8859-15")
        for line in tippstxt:
            tippslist.append(line)
        tippstxt.close()
        tipps = Label(master=self.loading_fenster, text=tippslist[randint(0, len(tippslist) - 1)],
                      padx=30, pady=10,
                      font=('Comic Sans MS', 14),
                      fg='black', bg='white')
        tipps.pack()

        self.loading_fenster.mainloop()

    @staticmethod
    def loading_beenden(loading_fenster):
        loading_fenster.destroy()
        Spielfeldanzeigen(d.getlevelnr() + 1, held)


# Spiel


spiel = Hauptprogramm()
