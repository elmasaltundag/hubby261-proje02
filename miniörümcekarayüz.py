from random import choice
from tkinter import *


miniörümcekgününsözü = ["Minimini Örümceğe hoşş geldiniz", "tekrar tekrar basmayınız"]

başlat = Tk()

def metingöster():
    gününseçilensözü = choice(miniörümcekgününsözü)
    gününsözü = Label(başlat, text=gününseçilensözü)
    gününsözü.pack()
    gününsözü.after(2000, gününsözü.destroy)

gününsözübaslık = Label(başlat, text="Günün Sözünü Görmek İçin Tıklayınız")
başlatbuton = Button(başlat, text="Tıklayınız!!", command=metingöster)
başlatKapat = Button(başlat, text="Kapat", command=quit)
gününsözübaslık.pack()
başlatbuton.pack()
başlatKapat.pack()

başlat.mainloop()



