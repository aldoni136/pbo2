import pygame
from tkinter import *

#init
window = Tk()
window.geometry("500x300")
window.title("MP3 Player")

#variabel dan fungsi
def suaraAyam():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/ALXSTAR/OneDrive/Documents/CODING/PBO2/tugas/tugas3/ayam.mp3')
    pygame.mixer.music.play()

def suaraAnjing():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/ALXSTAR/OneDrive/Documents/CODING/PBO2/tugas/tugas3/anjing.mp3')
    pygame.mixer.music.play()

def suaraBebek():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/ALXSTAR/OneDrive/Documents/CODING/PBO2/tugas/tugas3/bebek.mp3')
    pygame.mixer.music.play()

def suaraBurung():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/ALXSTAR/OneDrive/Documents/CODING/PBO2/tugas/tugas3/burung.mp3')
    pygame.mixer.music.play()

def suaraGajah():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/ALXSTAR/OneDrive/Documents/CODING/PBO2/tugas/tugas3/gajah.mp3')
    pygame.mixer.music.play()

def suaraKambing():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/ALXSTAR/OneDrive/Documents/CODING/PBO2/tugas/tugas3/kambing.mp3')
    pygame.mixer.music.play()

def suaraKera():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/ALXSTAR/OneDrive/Documents/CODING/PBO2/tugas/tugas3/kera.mp3')
    pygame.mixer.music.play()

def suaraKucing():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/ALXSTAR/OneDrive/Documents/CODING/PBO2/tugas/tugas3/kucing.mp3')
    pygame.mixer.music.play()

def suaraKuda():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/ALXSTAR/OneDrive/Documents/CODING/PBO2/tugas/tugas3/kuda.mp3')
    pygame.mixer.music.play()

def suaraSapi():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/ALXSTAR/OneDrive/Documents/CODING/PBO2/tugas/tugas3/sapi.mp3')
    pygame.mixer.music.play()
    
#komponen
    #label
ayam_label = Label(window, text="Suara Ayam\t")
ayam_label.grid(column=0, row=0)
anjing_label = Label(window, text="Suara Anjing\t")
anjing_label.grid(column=0, row=1)
bebek_label = Label(window, text="Suara Bebek\t")
bebek_label.grid(column=0, row=2)
burung_label = Label(window, text="Suara Burung\t")
burung_label.grid(column=0, row=3)
gajah_label = Label(window, text="Suara Gajah\t")
gajah_label.grid(column=0, row=4)
kambing_label = Label(window, text="Suara Kambing\t")
kambing_label.grid(column=0, row=5)
kera_label = Label(window, text="Suara Kera\t")
kera_label.grid(column=0, row=6)
kucing_label = Label(window, text="Suara Kucing\t")
kucing_label.grid(column=0, row=7)
kuda_label = Label(window, text="Suara Kuda\t")
kuda_label.grid(column=0, row=8)
sapi_label = Label(window, text="Suara Sapi\t")
sapi_label.grid(column=0, row=9)

    #tombol
ayam_tombol = Button(window, text="Play", command=suaraAyam)
ayam_tombol.grid(column=1, row=0)
anjing_tombol = Button(window, text="Play", command=suaraAnjing)
anjing_tombol.grid(column=1, row=1)
bebek_tombol = Button(window, text="Play", command=suaraBebek)
bebek_tombol.grid(column=1, row=2)
burung_tombol = Button(window, text="Play", command=suaraBurung)
burung_tombol.grid(column=1, row=3)
gajah_tombol = Button(window, text="Play", command=suaraGajah)
gajah_tombol.grid(column=1, row=4)
kambing_tombol = Button(window, text="Play", command=suaraKambing)
kambing_tombol.grid(column=1, row=5)
kera_tombol = Button(window, text="Play", command=suaraKera)
kera_tombol.grid(column=1, row=6)
kucing_tombol = Button(window, text="Play", command=suaraKucing)
kucing_tombol.grid(column=1, row=7)
kuda_tombol = Button(window, text="Play", command=suaraKuda)
kuda_tombol.grid(column=1, row=8)
sapi_tombol = Button(window, text="Play", command=suaraSapi)
sapi_tombol.grid(column=1, row=9)

#main loop
window.mainloop()