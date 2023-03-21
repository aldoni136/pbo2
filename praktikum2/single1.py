class HandPhone:
    def __init__(self, merk, tipe):
        self.merk = merk
        self.tipe = tipe

    def fastcharging(self):
        print(self.merk, "fastcharging")

class Samsung(HandPhone):
    def __init__(self, merk, tipe, warna):
        super().__init__(merk, tipe)
        self.warna = warna

    def kamera(self):
        print("Kamera aktif!")

handphoneA = Samsung("Samsung Galaxy", 15, "Black")
handphoneA.fastcharging() # output: Samsung Galaxy fastcharging
handphoneA.kamera() # output: Kamera aktif!
