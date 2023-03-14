class Baju:

    def __init__(self, ukuran, warna):
        self.ukuran = ukuran
        self.warna = warna

    def info(self):
        print(f"Baju {self.ukuran} berwarna {self.warna}")

BajuA = Baju("XL", "Hitam")
BajuA.info() # Output: Baju XL berwarna Hitam