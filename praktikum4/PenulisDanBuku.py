class Penulis:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Buku:
    def __init__(self, nama, penulis):
        self.nama = nama
        self.penulis = penulis

    def daftar_penulis(self):
        for penulis in self.penulis:
            print(penulis.nama, penulis.umur)

penulis1 = Penulis("Andi", 25)
penulis2 = Penulis("Budi", 30)

buku = Buku("ABC", [penulis1, penulis2])
buku.daftar_penulis()