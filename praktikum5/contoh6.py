class Handphone:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
manusia = Handphone("Samsung", "black")
try:
    print(Handphone.harga)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")