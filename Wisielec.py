import random
import tkinter
import linecache
from tkinter import *
import runpy
from random import randint
import os
import sys

window = tkinter.Tk()
window.title("Wisielec Gra")
window.geometry("600x750")
window.configure(background="#303030")

tytulVar = tkinter.StringVar()
tytulVar.set("WISIELEC THE GAME")




tytul = tkinter.Label(window, textvariable=tytulVar, bg="#303030", fg="Blue", height=1, font='Arial 20')
tytul.pack()
tytul.place(x=160, y=5)


def close_window():
    window.destroy()

def przyslowia():
    przyslowiaWindow = tkinter.Tk()
    przyslowiaWindow.title("Przysłowia trening")
    przyslowiaWindow.geometry("300x250")
    przyslowiaWindow.configure(background="#303030")
    przyslowiaWindow.mainloop()

def zwierzeta():
    zwierzetaWindow = tkinter.Tk()
    zwierzetaWindow.title("Zwierzeta trening")
    zwierzetaWindow.geometry("300x250")
    zwierzetaWindow.configure(background="#303030")
    zwierzetaWindow.mainloop()
    przysZ = Canvas(zwierzetaWindow, bg="blue", width="300", height="250")
    przysZ.pack()
    przysZ.place(x=10, y=10)
    antylopa = PhotoImage(file="impala.gif")
    antylopa1 = przysZ.create_image(1, 1, image=antylopa)
    antylopa1 = przysZ.create_oval







menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Opcje",  menu=filemenu)
filemenu.add_command(label="O grze", command=close_window)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=close_window)
window.config(menu=menubar)

trainmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Trening",  menu=trainmenu)
trainmenu.add_command(label="Przysłowia", command=przyslowia)
trainmenu.add_command(label="Film", command=close_window)
trainmenu.add_command(label="Geografia", command=close_window)
trainmenu.add_command(label="Zwierzeta", command=close_window)
trainmenu.add_command(label="Informatyka", command=close_window)



haslaPrzyslowia = ["bez pracy nie ma kołaczy ", "biedny jak mysz koscielna ", "jak kuba bogu tak bóg kubie ",
                   "apetyt rośnie w miare jedzenia ",
                   "baba z wozu koniom lżej ", "czas to pieniądz ", "czuć się jak ryba w wodzie ",
                   "człowiek człowiekowi wilkiem ",
                   "do trzech razy sztuka "]

haslaFilm = ["Chłopaki nie płaczą", "Brunet wieczorową porą", "Kariera nikodema dyzmy", "Pittbul niebezpieczne kobiety",
             "Forrest gump"
    , "Zielona mila", "Skazani na shawshank", "Deadpool", "harry potter i komnata tajemnic", "poszukiwany poszukiwana", "avengers czas ultrona",
             "cezary pazura", "skazany na śmierć", "braking bad", "the walking dead", "house of cards", "leonardo di caprio", "piraci z karaibów"]

haslaGeografia = ["Wyspy owcze", "Wielka brytania", "Stany zjednoczone", "Warszawa", "Wybrzeże kości słoniowej",
                  "Republika południowej afryki", "wulkan kilimandżaro", "wyspy kanaryjskie"]

haslaZwierzeta = ["Antylopa" ]

haslaPolska = ["Kazimierz dolny" ]

haslaInformatyka = ["Programowanie"]


plik = open("przyslowia.txt", "w")
plik.write("***********************HASLA PRZYSLOWIA**************************")
plik.write('\n')
plik.write('\n'.join(haslaPrzyslowia))
plik.write('\n')
plik.write("************************HASLA FILM*******************************")
plik.write('\n')
plik.write('\n'.join(haslaFilm))




def losujHaslo(x):
    hasloLosowe = random.choice(x)
    return hasloLosowe

def dodajHaslo():
    wybierz = input(
        "Wybierz Kateogrie: ///////////      Przysłowia: p ,  Film: f :  , Geografia: g,   Test:  t ////////////")
    if wybierz == 'p':
        newHas = input("Podaj swoje hasło do kategorii przysłowia:  ")
        haslaPrzyslowia.append(newHas)
    elif wybierz == 'f':
        newHas = input("Podaj swoje hasło do kategorii przysłowia:  ")
        haslaFilm.append(newHas)
    elif wybierz == 'g':
        newHas = input("Podaj swoje hasło do kategorii przysłowia:  ")
        haslaGeografia.append(newHas)

def haslo(x):
    hasloZmiana = ""
    for letter in x:
        if letter == ' ':
            hasloZmiana = hasloZmiana + letter
        else:
            letter = '*'
            hasloZmiana = hasloZmiana + letter
    return hasloZmiana


def main():
    print(
        "Wybierz Kateogrie: ///////////      Przysłowia: p ,  Film: f :  , Geografia: g,   Test:  t     Dodaj swoje hasło:    d       ////////////")


szubienica = Canvas(window, bg="Grey", width="500", height="450")
szubienica.pack()
szubienica.place(x=50, y=120)

wstep = PhotoImage(file="wstep.gif")
szubienica0 = PhotoImage(file="s0.gif")
szubienica1 = PhotoImage(file="s1.gif")
szubienica2 = PhotoImage(file="s2.gif")
szubienica3 = PhotoImage(file="s3.gif")
szubienica4 = PhotoImage(file="s4.gif")
szubienica5 = PhotoImage(file="s5.gif")
szubienica6 = PhotoImage(file="s6.gif")
szubienica7 = PhotoImage(file="s7.gif")
szubienica8 = PhotoImage(file="s8.gif")
szubienica9 = PhotoImage(file="s9.gif")
szubienica10 = PhotoImage(file="gameover.gif")
szubienicaWin = PhotoImage(file="win.gif")

rys1 = szubienica.create_image(250, 230, image=wstep)
rys12 = szubienica.create_oval

hasloZmiana = ""
iter = 10

def start():
    rys1 = szubienica.create_image(250, 230, image=wstep)
    rys12 = szubienica.create_oval
    tytulVar.set("Wisielec(THE HANGMAN)")
    tytul.place(x=150, y=5)
    tytulPrz = tkinter.StringVar()
    tytulPrz.set("Wybierz Kategorie")
    tytulFilm = tkinter.StringVar()
    tytulFilm.set("Wybierz Kategorie")

def get_text(x):
    litera = x
    global iter
    global RollPrz
    global odpowiedz
    global hasloZmiana
    global odpowiedz1
    LiczbaSzans = tkinter.Label(window, text="Pozostało Ci: " + str(iter) + " szans", bg="#303030", fg="red", height=1,
                                font='Arial 8')
    LiczbaSzans.pack()
    LiczbaSzans.place(x=10, y=5)

    HasKon = RollPrz
    RollPrz = list(RollPrz)
    for i in range(len(odpowiedz)):
        if RollPrz[i] == litera:

            odpowiedz[i] = litera
            odpowiedz1 = ''
            odpowiedz1 = (odpowiedz1.join(odpowiedz))
            print(odpowiedz)
            print(odpowiedz1)
            labelHaslo = tkinter.Label(window, text="Twoje hasło to: " + str(odpowiedz1), bg="#303030", fg="red", height=1,
                                       font='Arial 16')
            labelHaslo.pack()
            labelHaslo.place(x=50, y=60)


        elif odpowiedz.count('*') < 1 :
            iter = 100
            rys75 = szubienica.create_image(250, 230, image=szubienicaWin)
            rys76 = szubienica.create_oval

    if litera not in RollPrz:
        iter = iter - 1
        if iter == 0:
            print("Przegrałeś ")
    if iter == 10:
        rys2 = szubienica.create_image(250, 230, image=szubienica0)
        rys22 = szubienica.create_oval
    elif iter == 9:
        rys3 = szubienica.create_image(250, 230, image=szubienica1)
        rys32 = szubienica.create_oval
    elif iter == 8:
        rys4 = szubienica.create_image(250, 230, image=szubienica2)
        rys42 = szubienica.create_oval
    elif iter == 7:
        rys4 = szubienica.create_image(250, 230, image=szubienica3)
        rys42 = szubienica.create_oval
    elif iter == 6:
        rys4 = szubienica.create_image(250, 230, image=szubienica4)
        rys42 = szubienica.create_oval
    elif iter == 5:
        rys4 = szubienica.create_image(250, 230, image=szubienica5)
        rys42 = szubienica.create_oval
    elif iter == 4:
        rys4 = szubienica.create_image(250, 230, image=szubienica6)
        rys42 = szubienica.create_oval
    elif iter == 3:
        rys4 = szubienica.create_image(250, 230, image=szubienica7)
        rys42 = szubienica.create_oval
    elif iter == 2:
        rys4 = szubienica.create_image(250, 230, image=szubienica8)
        rys42 = szubienica.create_oval
    elif iter == 1:
        rys4 = szubienica.create_image(250, 230, image=szubienica9)
        rys42 = szubienica.create_oval
    elif iter == 0:
        rys4 = szubienica.create_image(250, 230, image=szubienica10)
        rys42 = szubienica.create_oval

def przyslowiaKat():
    global iter
    global odpowiedz
    global RollPrz
    RollPrz = ""
    iter = 10
    rys1 = szubienica.create_image(250, 230, image=szubienica0)
    rys12 = szubienica.create_oval
    tytulVar.set("PRZYSŁOWIA")
    tytul.place(x=190, y=5)

    RollPrz = losujHaslo(haslaPrzyslowia)
    odpowiedz = list(haslo(RollPrz))
    # losowanie hasla z listy przyslowia
    print(hasloZmiana)
    tytulPrz = tkinter.StringVar()
    tytulPrz.set("Twoje hasło to: " + str(haslo(RollPrz)))
    labelHaslo = tkinter.Label(window, textvariable=tytulPrz,  bg="#303030", fg="red", height=1,
                               font='Arial 16')
    labelHaslo.pack()
    labelHaslo.place(x=50, y=60)

def filmKat():
    global iter
    global odpowiedz
    global RollPrz
    RollPrz = ""
    iter = 10
    rys1 = szubienica.create_image(250, 230, image=szubienica0)
    rys12 = szubienica.create_oval
    tytulVar.set("FILM")
    tytul.place(x=190, y=5)

    RollPrz = losujHaslo(haslaFilm)
    odpowiedz = list(haslo(RollPrz))
    # losowanie hasla z listy Film
    print(hasloZmiana)

    tytulFilm = tkinter.StringVar()
    tytulFilm.set("Twoje hasło to:  "+str(haslo(RollPrz)))

    labelHaslo = tkinter.Label(window, textvariable=tytulFilm,  bg="#303030", fg="red", height=1,
                               font='Arial 16')
    labelHaslo.pack()
    labelHaslo.place(x=90, y=60)

def geografiaKat():
    global iter
    global odpowiedz
    global RollPrz
    RollPrz = ""
    iter = 10
    rys1 = szubienica.create_image(250, 230, image=szubienica0)
    rys12 = szubienica.create_oval
    tytulVar.set("GEOGRAFIA")
    tytul.place(x=190, y=5)

    RollPrz = losujHaslo(haslaGeografia)
    odpowiedz = list(haslo(RollPrz))
    # losowanie hasla z listy Geografia
    print(hasloZmiana)
    tytulPrz = tkinter.StringVar()
    tytulPrz.set("Twoje hasło to: " + str(haslo(RollPrz)))
    labelHaslo = tkinter.Label(window, textvariable=tytulPrz,  bg="#303030", fg="red", height=1,
                               font='Arial 16')
    labelHaslo.pack()
    labelHaslo.place(x=50, y=60)

def zwierzKat():
    global iter
    global odpowiedz
    global RollPrz
    RollPrz = ""
    iter = 10
    rys1 = szubienica.create_image(250, 230, image=szubienica0)
    rys12 = szubienica.create_oval
    tytulVar.set("Zwierzęta")
    tytul.place(x=190, y=5)

    RollPrz = losujHaslo(haslaZwierzeta)
    odpowiedz = list(haslo(RollPrz))
    # losowanie hasla z listy Film
    print(hasloZmiana)

    tytulFilm = tkinter.StringVar()
    tytulFilm.set("Twoje hasło to:  "+str(haslo(RollPrz)))

    labelHaslo = tkinter.Label(window, textvariable=tytulFilm,  bg="#303030", fg="red", height=1,
                               font='Arial 16')
    labelHaslo.pack()
    labelHaslo.place(x=90, y=60)

def PolKat():
    global iter
    global odpowiedz
    global RollPrz
    RollPrz = ""
    iter = 10
    rys1 = szubienica.create_image(250, 230, image=szubienica0)
    rys12 = szubienica.create_oval
    tytulVar.set("Informatyka")
    tytul.place(x=190, y=5)

    RollPrz = losujHaslo(haslaInformatyka)
    odpowiedz = list(haslo(RollPrz))
    # losowanie hasla z listy Film
    print(hasloZmiana)

    tytulFilm = tkinter.StringVar()
    tytulFilm.set("Twoje hasło to:  "+str(haslo(RollPrz)))

    labelHaslo = tkinter.Label(window, textvariable=tytulFilm,  bg="#303030", fg="red", height=1,
                               font='Arial 16')
    labelHaslo.pack()
    labelHaslo.place(x=90, y=60)

def infKat():
    global iter
    global odpowiedz
    global RollPrz
    RollPrz = ""
    iter = 10
    rys1 = szubienica.create_image(250, 230, image=szubienica0)
    rys12 = szubienica.create_oval
    tytulVar.set("Informatyka")
    tytul.place(x=190, y=5)

    RollPrz = losujHaslo(haslaInformatyka)
    odpowiedz = list(haslo(RollPrz))
    # losowanie hasla z listy Film
    print(hasloZmiana)

    tytulFilm = tkinter.StringVar()
    tytulFilm.set("Twoje hasło to:  "+str(haslo(RollPrz)))

    labelHaslo = tkinter.Label(window, textvariable=tytulFilm,  bg="#303030", fg="red", height=1,
                               font='Arial 16')
    labelHaslo.pack()
    labelHaslo.place(x=90, y=60)

A = tkinter.Button(window, text="A", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("a"))
A.pack(side='left')
A.place(x=30, y=590, width=35, height=35)

Ą = tkinter.Button(window, text="Ą", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("ą"))
Ą.pack(side='left')
Ą.place(x=70, y=590, width=35, height=35)

B = tkinter.Button(window, text="B", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("b"))
B.pack(side='left')
B.place(x=110, y=590, width=35, height=35)

C = tkinter.Button(window, text="C", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("c"))
C.pack(side='left')
C.place(x=150, y=590, width=35, height=35)

Ć = tkinter.Button(window, text="Ć", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("ć"))
Ć.pack(side='left')
Ć.place(x=190, y=590, width=35, height=35)

D = tkinter.Button(window, text="D", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("d"))
D.pack(side='left')
D.place(x=230, y=590, width=35, height=35)

E = tkinter.Button(window, text="E", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("e"))
E.pack(side='left')
E.place(x=270, y=590, width=35, height=35)

Ę = tkinter.Button(window, text="Ę", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("ę"))
Ę.pack(side='left')
Ę.place(x=310, y=590, width=35, height=35)

F = tkinter.Button(window, text="F", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("f"))
F.pack(side='left')
F.place(x=350, y=590, width=35, height=35)

G = tkinter.Button(window, text="G", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("g"))
G.pack(side='left')
G.place(x=390, y=590, width=35, height=35)

H = tkinter.Button(window, text="H", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("h"))
H.pack(side='left')
H.place(x=430, y=590, width=35, height=35)

I = tkinter.Button(window, text="I", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("i"))
I.pack(side='left')
I.place(x=470, y=590, width=35, height=35)

J = tkinter.Button(window, text="J", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("j"))
J.pack(side='left')
J.place(x=510, y=590, width=35, height=35)

K = tkinter.Button(window, text="K", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("k"))
K.pack(side='left')
K.place(x=30, y=630, width=35, height=35)

L = tkinter.Button(window, text="L", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("l"))
L.pack(side='left')
L.place(x=70, y=630, width=35, height=35)

Ł = tkinter.Button(window, text="Ł", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("ł"))
Ł.pack(side='left')
Ł.place(x=110, y=630, width=35, height=35)

M = tkinter.Button(window, text="M", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("m"))
M.pack(side='left')
M.place(x=150, y=630, width=35, height=35)

N = tkinter.Button(window, text="N", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("n"))
N.pack(side='left')
N.place(x=190, y=630, width=35, height=35)

Ń = tkinter.Button(window, text="Ń", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("ń"))
Ń.pack(side='left')
Ń.place(x=230, y=630, width=35, height=35)

O = tkinter.Button(window, text="O", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("o"))
O.pack(side='left')
O.place(x=270, y=630, width=35, height=35)

Ó = tkinter.Button(window, text="Ó", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("ó"))
Ó.pack(side='left')
Ó.place(x=310, y=630, width=35, height=35)

P = tkinter.Button(window, text="P", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("p"))
P.pack(side='left')
P.place(x=350, y=630, width=35, height=35)

Q = tkinter.Button(window, text="Q", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("q"))
Q.pack(side='left')
Q.place(x=390, y=630, width=35, height=35)

R = tkinter.Button(window, text="R", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("r"))
R.pack(side='left')
R.place(x=430, y=630, width=35, height=35)

S = tkinter.Button(window, text="S", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("s"))
S.pack(side='left')
S.place(x=470, y=630, width=35, height=35)

Ś = tkinter.Button(window, text="Ś", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("ś"))
Ś.pack(side='left')
Ś.place(x=510, y=630, width=35, height=35)

T = tkinter.Button(window, text="T", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("t"))
T.pack(side='left')
T.place(x=110, y=670, width=35, height=35)

U = tkinter.Button(window, text="U", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("u"))
U.pack(side='left')
U.place(x=150, y=670, width=35, height=35)

V = tkinter.Button(window, text="V", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("v"))
V.pack(side='left')
V.place(x=190, y=670, width=35, height=35)

W = tkinter.Button(window, text="W", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("w"))
W.pack(side='left')
W.place(x=230, y=670, width=35, height=35)

X = tkinter.Button(window, text="X", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("x"))
X.pack(side='left')
X.place(x=270, y=670, width=35, height=35)

Y = tkinter.Button(window, text="Y", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("y"))
Y.pack(side='left')
Y.place(x=310, y=670, width=35, height=35)

Z = tkinter.Button(window, text="Z", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("z"))
Z.pack(side='left')
Z.place(x=350, y=670, width=35, height=35)

Ź = tkinter.Button(window, text="Ź", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("ź"))
Ź.pack(side='left')
Ź.place(x=390, y=670, width=35, height=35)

Ż = tkinter.Button(window, text="Ż", font=("Courier", 16, "bold"), background="blue", bd=7,
                   command=lambda: get_text("ż"))
Ż.pack(side='left')
Ż.place(x=430, y=670, width=35, height=35)

START = tkinter.Button(window, text="START", font=("Courier", 16, "bold"), background="green", bd=7,
                       command=start)
START.pack(side='left')
START.place(x=470, y=670, width=78, height=35)

EXIT = tkinter.Button(window, text="EXIT", font=("Courier", 16, "bold"), background="red", bd=7, command=close_window)
EXIT.pack(side='left')
EXIT.place(x=30, y=670, width=78, height=35)

Pr = tkinter.Button(window, text="P", font=("Courier", 16, "bold"), background="#99FFCC", command=przyslowiaKat)
Pr.pack(side='left')
Pr.place(x=560, y=590, width=35, height=35)

Fi = tkinter.Button(window, text="F", font=("Courier", 16, "bold"), background="#00FF99", command=filmKat)
Fi.pack(side='left')
Fi.place(x=560, y=630, width=35, height=35)

Ge = tkinter.Button(window, text="G", font=("Courier", 16, "bold"), background="#339966", command=geografiaKat)
Ge.pack(side='left')
Ge.place(x=560, y=670, width=35, height=35)

window.mainloop()
