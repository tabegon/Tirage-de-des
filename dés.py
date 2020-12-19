from tkinter import *
import random
F = Tk()

DD = chr(0x2662)
DD5 = DD+DD+DD+DD+DD
D1 = chr(0x2680)
D2 = chr(0x2681)
D3 = chr(0x2682)
D4 = chr(0x2683)
D5 = chr(0x2684)
D6 = chr(0x2685)
LD = [" ", D1, D2, D3, D4, D5, D6]

def Tirage():
    t = ' '
    total = 0
    for i in range(d.get()):
        des = random.randint(1,6)
        total += des
        t += LD[des]
    Resultat.config(text = t)
    L.config(text = total)

# Le bouton pour lancer le tirage
B = Button(F, text = "Lancez les dés !", command=Tirage, fg="white", bg="black", activebackground="black", activeforeground="white")
B.grid(column=0,row=0,rowspan = 3, sticky="ewns")
B.config( font = "Arial 30")

# Choix du nombre de dés
d = IntVar()
d.set(1)

b1=Radiobutton(F, variable=d,text="1 Dés        ",bg="light green", value=1)
b1.grid(column=1,row=0)
b1.config( font = "Arial 25")

b2=Radiobutton(F, variable=d,text="3 Dés        ",bg="light green", value=3)
b2.grid(column=1,row=1)
b2.config( font = "Arial 25")

b3=Radiobutton(F, variable=d,text="5 Dés        ",bg="light green", value=5)
b3.grid(column=1,row=2)
b3.config( font = "Arial 25")

# L'affichage du score
L = Label(F,text ="XX",bg="blue", width=3)
L.grid(column=2,row=0,rowspan = 3, sticky="ewns")
L.config( font = "Arial 80")

# Zone de dessin des dés
Resultat = Label(F, text=DD5, width=7)
Resultat.config( font = "Arial 80")
Resultat.grid(column=0,row=3,columnspan = 3, sticky="ewns")

F.title("Tirage de dés")
F.mainloop()