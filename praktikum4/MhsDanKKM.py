class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Kelompok_KKM:
    def __init__(self, nama, mahasiswa):
        self.nama = nama
        self.mahasiswa = mahasiswa

    def daftar_mahasiswa(self):
        for mahasiswa in self.mahasiswa:
            print(mahasiswa.nama, mahasiswa.umur)

mahasiswa1 = Mahasiswa("Aldoni", 22)
mahasiswa2 = Mahasiswa("Santoso", 23)
mahasiswa3 = Mahasiswa("Budi", 21)
mahasiswa4 = Mahasiswa("Siti", 25)
mahasiswa5 = Mahasiswa("Mawar", 22)

kelompok_KKM = Kelompok_KKM("KKM1", [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4, mahasiswa5])
kelompok_KKM.daftar_mahasiswa()