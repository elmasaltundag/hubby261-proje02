import tkinter
from tkinter import *
import tkinter as tk

başlat = Tk()
başlat.title("Mini Örümcek Arayüz Denemesi")



Başlık = Label(başlat, text="MENÜ TERCİHİNİZ")
Buton1 = Button(başlat, text="URL Listele", fg="black", bg="white")
Buton2 = Button(başlat, text="URL Ekle",fg="black", bg="white")
Buton3 = Button(başlat, text="Örümcek Gönder",fg="black", bg="white")
Buton4 = Button(başlat, text="Sonuçları Listele",fg="black", bg="white")
Buton0 = Button(başlat, text="Çıkış", fg="black", bg="red", command=başlat.quit)


Başlık.grid(row=0, columnspan=2, padx=50, pady=25)
Başlık.config(font=("Times New Roman", 30))
Buton1.grid(row=1, column=0, padx=10, pady=20)
Buton2.grid(row=1, column=1, padx=10, pady=20)
Buton3.grid(row=2, column=0, padx=10, pady=20)
Buton4.grid(row=2, column=1, padx=10, pady=20)
Buton0.grid(row=4, columnspan=2, padx=5, pady=10)


başlat.mainloop()






