class Karyawan:

    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    def info(self):
        print(f"Nama: {self.nama}\nAlamat: {self.alamat}")

KaryawanB = Karyawan("Aldoni", "Cirebon")
KaryawanB.info()