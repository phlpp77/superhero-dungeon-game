import queue
import sndhdr
import threading
from time import sleep
from random import randint
import shelve
from tkinter import *
import tkinter.ttk

from helden.held import Hero
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
            sleep(0.2)
            self.fenster.wm_attributes('-alpha', 0.25)
            sleep(0.2)
            # print("Flacker!" + str(threading.get_ident()))
            self.fenster.wm_attributes('-alpha', 1)


class Musik(GUIThread):
    def run(self):
        # queueing all music files in music folder
        all_music = []
        sound_queue = queue.Queue()
        for root, dirs, filenames in os.walk('./music'):
            for filename in filenames:
                # checking if the file is a soundfile
                sound_path = "music/" + filename
                if sndhdr.what(sound_path):
                    all_music.append(sound_path)
                    sound_queue.put(sound_path)

        # using pygame to play all music in the music folder
        if pygame:
            # playing music if there is music in the music folder
            if len(all_music) > 0:
                # initializing the music player
                pygame.mixer.init()
                pygame.mixer.music.load(all_music[0])
                pygame.mixer.music.play()
                # queueing the music
                for filename in all_music[0:]:
                    pygame.mixer.music.queue(filename)
            # stopping music
            if self._stop:
                pygame.mixer.music.stop()

        # using Windows to play music
        while not self._stop:
            # checking if winsound is available
            if winsound and not pygame:
                sound = sound_queue.get()
                winsound.PlaySound(sound, winsound.SND_FILENAME)
                sound_queue.put(sound)
            # if no soundplayer is available, the process is stopped
            else:
                self.stop()


class LoadingBalken(threading.Thread):
    def __init__(self, stop, progressbar, button, window):
        self.stop, self.progressbar, self.button, self.window = stop, progressbar, button, window
        threading.Thread.__init__(self)

    def run(self):  # TODO auf 0.05 und auf 0.5 später zurück ändern
        # showing the progressbar with 90 steps
        for i in range(0, 90):
            self.progressbar.step()
            sleep(0.005)

        for i in range(0, 9):
            self.progressbar.step()
            sleep(0.05)

        # after the progressbar has finished
        # binding the button and keys to termminate the loading screen
        self.button.pack(side=BOTTOM, anchor=E, padx=30, pady=30)
        self.window.bind('<Escape>', lambda event: self.stop(self.window))
        self.window.bind('<Return>', lambda event: self.stop(self.window))


# ###########################################GUI:Startbildschirm############################################

class Hauptprogramm:

    def __init__(self):
        global text_color
        text_color = '#c3e2e7'
        global bg_color
        bg_color = '#000000'
        # starting-window setup
        self.fenster = Tk()
        self.fenster.title('Dungeon Game')
        # opening the titlescreen and getting its dimensions
        background_image = PhotoImage(file="gfx/titlescreen1.gif")
        width, height = background_image.width(), background_image.height()
        # configuring the window to be of same size as titlescreen
        self.fenster.minsize(width, height)
        self.fenster.maxsize(width, height)
        # centering the window on screen
        ws = self.fenster.winfo_screenwidth()
        hs = self.fenster.winfo_screenheight()
        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)
        self.fenster.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # showing the background image
        background_label = Label(self.fenster, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # starting flickering of the screen
        self.parallel = Flackern(self.fenster)
        self.parallel.setDaemon(True)
        self.parallel.start()
        # starting music play
        self.music = Musik(self.fenster)
        self.music.setDaemon(True)
        self.music.start()
        # binding keys to game functions
        self.fenster.bind('<Return>', lambda event: self.einspieler())
        self.fenster.bind('<Escape>', lambda event: self.fenster.destroy())
        self.fenster.bind('<Motion>', lambda event: self.parallel.stop())
        self.fenster.wm_attributes('-alpha', 0.5)
        # initializing the buttons
        self.neuesspiel_button = Button(master=self.fenster, text='START',
                                        command=self.einspieler, fg=text_color, bg='RED')
        self.neuesspiel_button.place(anchor=E, y=496, x=835)
        self.beenden_button = Button(master=self.fenster, text="ENDE",
                                     command=self.fenster.destroy, fg="white", bg="grey")
        self.beenden_button.place(anchor=E, y=528, x=829)
        self.reset_button = Button(master=self.fenster, text="RESET",
                                   command=self.reset_score, fg="white", bg="grey")
        self.reset_button.place(anchor=E, y=height - height * 0.027, x=width * 0.043)

        # displaying the highscore on the starting screen
        self.score = 0
        self.scorelabel = Label(self.fenster, text=self.score, compound=CENTER, bg="black", fg="light yellow",
                                font="System 26 bold")
        self.scorelabel.place(anchor=E, y=320, x=587)
        # reading the highscore from score.txt
        highscore = shelve.open("score.txt")
        # on initial startup the score is set to 0
        if "Score" in highscore:
            highscore.close()
            self.refresh_score()
        else:
            highscore.close()
            self.reset_score()

        self.fenster.mainloop()

    # function to set the score to zero
    def reset_score(self):
        highscore = shelve.open("score.txt")
        highscore["Score"] = 0
        highscore.close()
        self.refresh_score()

    # function to refresh the highscore label
    def refresh_score(self):
        highscore = shelve.open("score.txt")
        self.score = highscore["Score"]
        self.scorelabel.config(text=self.score)
        highscore.close()

    # function to start the hero selection
    def einspieler(self):
        self.parallel.stop()
        Heldenwahl()


class Heldenwahl:

    def __init__(self):
        # initializing window
        w, h = 590, 280
        self.heldenwahl_fenster = Toplevel()
        self.heldenwahl_fenster.title('Dungeon Game')
        self.heldenwahl_fenster.minsize(w, h)
        self.heldenwahl_fenster.maxsize(w, h)
        # centering the window on screen
        ws = self.heldenwahl_fenster.winfo_screenwidth()
        hs = self.heldenwahl_fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.heldenwahl_fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.heldenwahl_fenster.config(bg=bg_color)
        self.heldenwahl_fenster.focus()

        self.label = Label(master=self.heldenwahl_fenster,
                           text='Heldenauswahl',
                           font=('Comic Sans MS', 14),
                           fg=text_color, bg=bg_color)
        # initializing radiobuttons
        self.radiogroup = Frame(master=self.heldenwahl_fenster,
                                bd=2, bg=bg_color)
        self.auswahl = StringVar()
        self.auswahl.set(0)
        self.radiobuttons = []
        self.radio_names = ["Batman", "Superman", "Spiderman", "Ironman", "GreenLantern", "Flash"]
        for i in self.radio_names:
            self.radiobuttons.append(Radiobutton(master=self.radiogroup, text=i, font=('Comic Sans MS', 10),
                                                 bg=bg_color, fg=text_color, value=i, variable=self.auswahl,
                                                 command=self.refresh))
        self.radiobuttons[0].select()
        self.radio_pos = 0
        # initializing buttons
        self.weiter_button = Button(master=self.radiogroup, text='weiter',
                                    command=self.heldenwahl_beenden, bg=bg_color, fg=text_color)
        self.beschreibung = Text(master=self.heldenwahl_fenster, width=50,
                                 height=11, wrap=WORD, font=('Comic Sans MS', 10), bg=bg_color, fg=text_color)

        # initializaing hero preview
        self.hero_image = PhotoImage(file=self.get_hero().get_anzeige_bild())
        self.hero_label = Label(self.heldenwahl_fenster, image=self.hero_image, bg=bg_color)
        self.hero_label.pack(side=RIGHT, padx=5, pady=5)
        self.refresh()

        # packing all elements
        self.label.place(x=w / 2, y=h * 0.07, anchor='center')
        self.radiogroup.pack(side=LEFT, padx=5, pady=5)
        for i in self.radiobuttons:
            i.pack(anchor=W)

        self.weiter_button.pack(anchor=S, padx=5, pady=5, fill=X)
        self.beschreibung.pack(side=LEFT, padx=5, pady=0)
        # binding keys to game functions
        self.heldenwahl_fenster.bind('<Return>', lambda event: self.heldenwahl_beenden())
        self.heldenwahl_fenster.bind('<Escape>', lambda event: self.heldenwahl_fenster.destroy())
        self.heldenwahl_fenster.bind('<KeyPress-Down>', lambda event: self.scroll(0))
        self.heldenwahl_fenster.bind('<KeyPress-Up>', lambda event: self.scroll(1))

        self.heldenwahl_fenster.mainloop()

    # function to scroll up and down the radiobutton list
    def scroll(self, direction):
        # if the direction is upwards
        if direction:
            if self.radio_pos > 0:
                self.radio_pos -= 1
                self.radiobuttons[self.radio_pos].select()
        # direction downwards
        else:
            if self.radio_pos < len(self.radiobuttons) - 1:
                self.radio_pos += 1
                self.radiobuttons[self.radio_pos].select()
        self.refresh()

    # function to refresh the seleced hero's data
    def refresh(self):
        # updating the text
        self.beschreibung.delete(1.0, END)
        dateiname = os.path.join("helden", self.auswahl.get() + '.txt')
        daten = open(dateiname, "r", encoding="iso-8859-15")
        textdaten = daten.read()
        daten.close()
        self.beschreibung.insert(1.0, textdaten)
        # updating the image
        self.hero_image = PhotoImage(file=self.get_hero().get_anzeige_bild())
        self.hero_label.configure(image=self.hero_image)

    # function to get the selected hero
    def get_hero(self):
        return Hero.factory(self.auswahl.get())

    # function to set the selected hero and terminate the hero selection
    def heldenwahl_beenden(self):
        global held
        held = self.get_hero()
        self.heldenwahl_fenster.destroy()
        HeldBenennen()


class HeldBenennen:

    def __init__(self):
        # initializing window
        w = h = 220
        self.heldbenennen_fenster = Toplevel()
        self.heldbenennen_fenster.title('Dungeon Game')
        self.heldbenennen_fenster.minsize(w, h)
        self.heldbenennen_fenster.maxsize(w, h)
        # centering the window on screen
        ws = self.heldbenennen_fenster.winfo_screenwidth()
        hs = self.heldbenennen_fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.heldbenennen_fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.heldbenennen_fenster.config(bg=bg_color)
        self.heldbenennen_fenster.focus()
        # binding keys to game functions
        self.heldbenennen_fenster.bind('<Return>', lambda event: self.heldbenennen_beenden())
        self.heldbenennen_fenster.bind('<Escape>', lambda event: self.heldenwahl_neustart())
        # initializing name input
        self.label = Label(master=self.heldbenennen_fenster,
                           text='Held benennen',
                           padx=30, pady=10,
                           font=('Comic Sans MS', 14),
                           fg=text_color, bg=bg_color)
        self.eingabefeld = Entry(self.heldbenennen_fenster, bg=bg_color, fg=text_color)
        self.eingabefeld.insert(END, held.gettypname())
        # automatically selecting text of name field
        self.eingabefeld.focus()
        self.eingabefeld.select_range(0, 'end')
        # gender selection
        self.auswahlgeschlecht = StringVar()
        self.maennlich = Radiobutton(master=self.heldbenennen_fenster,
                                     text='maennlich',
                                     font=('Comic Sans MS', 10),
                                     bg=bg_color,
                                     fg=text_color,
                                     value='0',
                                     variable=self.auswahlgeschlecht)
        self.weiblich = Radiobutton(master=self.heldbenennen_fenster,
                                    text='weiblich',
                                    font=('Comic Sans MS', 10),
                                    bg=bg_color,
                                    fg=text_color,
                                    value='1',
                                    variable=self.auswahlgeschlecht)
        self.maennlich.select()
        self.weiter_button = Button(master=self.heldbenennen_fenster, text='weiter',
                                    command=self.heldbenennen_beenden, bg=bg_color, fg=text_color)
        self.zurueck_button = Button(master=self.heldbenennen_fenster, text='zurück',
                                     command=self.heldenwahl_neustart, bg=bg_color, fg=text_color)

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
        if self.eingabefeld.get() == held.gettypname():
            held.setheldenname("Namenloser")
        else:
            held.setheldenname(self.eingabefeld.get())
        held.setgeschlecht(self.auswahlgeschlecht.get())
        self.heldbenennen_fenster.destroy()
        Spielfeldanzeigen(1)


# ###########################################GUI:Spielfeld############################################
# noinspection PyAttributeOutsideInit
class Spielfeldanzeigen:

    def __init__(self, levelnr):
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
        self.spielfeld_fenster.config(bg=bg_color)

        self.canvas = Canvas(master=self.spielfeld_fenster, width=1088,
                             height=576, bg=bg_color)
        self.canvas.pack(padx=0, pady=0)

        self.statsframe = Frame(master=self.spielfeld_fenster, bd=3, bg=bg_color)

        self.statsframe1 = Frame(master=self.statsframe, relief=FLAT,
                                 bd=2, bg=bg_color)
        self.statsframe2 = Frame(master=self.statsframe, relief=FLAT,
                                 bd=2, bg=bg_color)

        self.labelheldenname = Label(master=self.statsframe1, text=held.getheldenname(),
                                     bg=bg_color, fg=text_color, width=20, pady=2, font=('Comic Sans MS', 15))

        self.labeltypname = Label(master=self.statsframe2, text=held.gettypname(),
                                  bg=bg_color, fg=text_color, width=20, pady=2, font=('Comic Sans MS', 15))

        # amount_characteristics describes the number of labels that are characteristics (the rest are combat values)
        self.amount_characteristics, self.amount_combat_values = 8, 2
        self.label, self.labeltext = [], ["MU: ", "KL: ", "CH: ", "IN: ", "FF: ", "GE: ", "KO: ", "KK: ", "AT: ",
                                          "PA: ", "LE: ", "RS: "]
        # initialize characteristics readout
        for i in range(self.amount_characteristics):
            tmp_label = Label(master=self.statsframe1, text=self.labeltext[i] + str(held.geteigenschaften()[i]),
                              bg=bg_color, fg=text_color, width=6, pady=2, font=('Comic Sans MS', 13))
            self.label.append(tmp_label)

        # initialize combat values readout
        for i in range(self.amount_characteristics, self.amount_characteristics + self.amount_combat_values):
            tmp_label = Label(master=self.statsframe2,
                              text=self.labeltext[i] + str(
                                  held.getkampfwerte()[i - self.amount_characteristics] + held.getwaffe().getmod()[
                                      i - self.amount_characteristics]), bg=bg_color,
                              fg=text_color, width=6, pady=2, font=('Comic Sans MS', 13))
            self.label.append(tmp_label)

        # initialize life value readout
        self.label.append(Label(master=self.statsframe2,
                                text=self.labeltext[len(self.labeltext) - 2] + str(held.getkampfwerte()[2]) + '/' + str(
                                    held.getmaxle()),
                                bg=bg_color, fg=text_color, width=12, pady=2, font=('Comic Sans MS', 13)))
        # initialize armor readout
        self.label.append(Label(master=self.statsframe2,
                                text=self.labeltext[len(self.labeltext) - 1] + str(held.getruestung().getrs()),
                                bg=bg_color, fg=text_color, width=6, pady=2, font=('Comic Sans MS', 13)))

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

        # binding keys to game events
        self.spielfeld_fenster.bind('<Escape>', lambda event: self.spielfeld_fenster.destroy())
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
        # updating characteristics readout
        for i in range(self.amount_characteristics):
            self.label[i].config(text=self.labeltext[i] + str(held.geteigenschaften()[i]))

        # updating combat value readout
        for i in range(self.amount_characteristics, self.amount_characteristics + self.amount_combat_values):
            self.label[i].config(text=self.labeltext[i] + str(
                held.getkampfwerte()[i - self.amount_characteristics] + held.getwaffe().getmod()[
                    i - self.amount_characteristics]))

        # updating health and armor readout
        self.label[len(self.label) - 2].config(
            text=self.labeltext[len(self.labeltext) - 2] + str(held.getkampfwerte()[2]) + '/' + str(held.getmaxle()))
        self.label[len(self.label) - 1].config(
            text=self.labeltext[len(self.labeltext) - 1] + str(held.getruestung().getrs()))

    @staticmethod
    def bildrichtung_aktualisieren(direction):
        switcher = {1: 'W', 2: 'D', 3: 'A', 4: ''}
        held.setbild(os.path.join("gfxhelden", held.gettypname() + switcher.get(direction) + ".gif"))
        heldenbild.config(file=held.getbild())

    def bewegung(self, direction):  # direction: 1:up, 2:right, 3:left, 4:down
        # the required amount of movement of the hero per field
        block_dimension = 64
        # slowing the hero down according to it's type
        sleep(held.get_timeout())
        # refreshing the shown image of the hero according to it's direction
        self.bildrichtung_aktualisieren(direction)
        # getting the current coordinates of the hero
        x, y = held.getx(), held.gety()
        # getting the direction vector
        dir_vector = {1: (0, -1), 2: (1, 0), 3: (-1, 0), 4: (0, 1)}
        vec_x, vec_y = dir_vector.get(direction)
        # calculating the new coordinates of the hero
        new_x, new_y = x + vec_x, y + vec_y

        # checking if the wanted movement is a legal operation
        if 0 <= new_x < d.getmaxx() and 0 <= new_y < d.getmaxy():
            # triggering the switch at the current coordinates
            self.d = d.getschalter(new_x, new_y).ausloesen(d)
            # showing non-invisible switches
            if self.d.getschalter(new_x, new_y).getschaltertyp() != 0:
                self.canvas_aktualisieren(new_x, new_y)
            # hero enters the field at the new coordinates
            self.d.getfeld(new_x, new_y).betreten(held)
            # refreshing the shown item
            self.itembild[new_x][new_y].config(file=self.d.getfeld(new_x, new_y).getitembild())
            if self.d.getbegehbar(new_x, new_y):
                self.canvas.move(heldid, block_dimension * vec_x, block_dimension * vec_y)
                held.setx(new_x)
                held.sety(new_y)

        # showing the changes made
        self.lightmap_aktualisieren()
        self.heldenstats_aktualisieren()

        # if the hero has no lifes left the deathscreen is shown
        if held.getle() <= 0:
            # terminating the current level window
            self.spielfeld_fenster.destroy()
            DeathScreen()

        # if the level is finished the highscore gets refreshed and the loading screen is shown
        if d.getlevelende():
            # writing the new highscore
            self.highscore = shelve.open("score.txt")
            if self.highscore["Score"] < d.getlevelnr() + 1:
                self.highscore["Score"] = d.getlevelnr() + 1
            self.highscore.close()
            # terminating the current level window
            self.spielfeld_fenster.destroy()
            # opening the loading screen
            LoadingScreen()

        # if the game is finished the end screen is shown
        if d.getspielende():
            # terminating the current level window
            self.spielfeld_fenster.destroy()
            # opening the end screen
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
        self.death_fenster.config(bg=bg_color)
        bg = PhotoImage(file="gfx/deathScreen.gif")
        bl = Label(self.death_fenster, image=bg)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        self.death_fenster.mainloop()


class EndScreen:

    def __init__(self):
        bg = PhotoImage(file="gfx/endScreen.gif")
        width, height = bg.width(), bg.height()
        self.end_fenster = Toplevel()
        self.end_fenster.focus_force()
        self.end_fenster.title('Dungeon Game - Vollversion kaufen!')
        self.end_fenster.minsize(width, height)
        self.end_fenster.maxsize(width, height)
        ws = self.end_fenster.winfo_screenwidth()
        hs = self.end_fenster.winfo_screenheight()
        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)
        self.end_fenster.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.end_fenster.config(bg=bg_color)
        bl = Label(self.end_fenster, image=bg)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        self.end_fenster.mainloop()


class LoadingScreen:

    def __init__(self):
        bg = PhotoImage(file="gfx/loadingScreen.gif")
        w, h = bg.width(), bg.height()
        self.loading_fenster = Toplevel()
        self.loading_fenster.focus_force()
        self.loading_fenster.title('Dungeon Game - loading...')
        self.loading_fenster.minsize(w, h)
        self.loading_fenster.maxsize(w, h)
        ws = self.loading_fenster.winfo_screenwidth()
        hs = self.loading_fenster.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.loading_fenster.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.loading_fenster.config(bg=bg_color)

        bl = Label(self.loading_fenster, image=bg)
        bl.place(x=0, y=0, relwidth=1, relheight=1)

        progressbar = tkinter.ttk.Progressbar(master=self.loading_fenster, orient=HORIZONTAL, length=200,
                                              mode='determinate')
        progressbar.pack(side="bottom")

        w_button = Button(master=self.loading_fenster, text='weiter',
                          command=lambda: self.loading_beenden(self.loading_fenster), bg=text_color)

        balken = LoadingBalken(self.loading_beenden, progressbar, w_button, self.loading_fenster)
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
                      fg='black', bg=text_color)
        tipps.pack()

        self.loading_fenster.mainloop()

    @staticmethod
    def loading_beenden(loading_fenster):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        loading_fenster.destroy()
        Spielfeldanzeigen(d.getlevelnr() + 1)


# Spiel
spiel = Hauptprogramm()
