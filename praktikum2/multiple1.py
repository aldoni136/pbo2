class Penduduk:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def ngoding(self):
        print(self.nama, "sedang ngoding")

class Alamat:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    def kuliah(self):
        print(self.nama, "sedang kuliah")

class PendudukA(Penduduk, Alamat):
    def __init__(self, nama, usia, alamat):
        Penduduk.__init__(self, nama, usia)
        Alamat.__init__(self, nama, alamat)

    def liburan(self):
        print(self.nama, "sedang liburan")

penduduk_A = PendudukA("Aldoni", "22", "Indramayu")
penduduk_A.ngoding() # output: Aldoni sedang ngoding
penduduk_A.kuliah() # output: Aldoni sedang kuliah
penduduk_A.liburan() # output: Aldoni sedang liburan