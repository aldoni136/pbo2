class Peneliti:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Jurnal:
    def __init__(self, nama, peneliti):
        self.nama = nama
        self.peneliti = peneliti

    def daftar_peneliti(self):
        for peneliti in self.peneliti:
            print(peneliti.nama, peneliti.umur)

peneliti1 = Peneliti("Aldoni", 22)
peneliti2 = Peneliti("Santoso", 23)

jurnal = Jurnal("PBO", [peneliti1, peneliti2])
jurnal.daftar_peneliti()