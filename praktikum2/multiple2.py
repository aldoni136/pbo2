class Buku:
    def __init__(self, judul, id):
        self.judul = judul
        self.id = id

    def display_info(self):
        print(f"Judul Buku: {self.judul}")
        print(f"ID Buku: {self.id}")

class Penerbit:
    def __init__(self, penerbit, harga):
        self.penerbit = penerbit
        self.harga = harga

    def display_info(self):
        print(f"Penerbit: {self.penerbit}")
        print(f"Harga: {self.harga}")

class Penulis:
    def __init__(self, buku, genre):
        self.buku = buku
        self.genre = genre

    def display_info(self):
        print(f"Buku: {self.buku}")
        print(f"Genre: {self.genre}")

class PenulisPenerbit(Buku, Penerbit, Penulis):
    def __init__(self, judul, id, penerbit, harga, buku, genre):
        Buku.__init__(self, judul, id)
        Penerbit.__init__(self, penerbit, harga)
        Penulis.__init__(self, buku, genre)
        
    def display_info(self):
        super().display_info()
        print(f"penerbit: {self.penerbit}")
        print(f"harga: {self.harga}")
        print(f"Buku: {self.buku}")
        print(f"Genre: {self.genre}")

# contoh penggunaan
penulis_penerbitC = PenulisPenerbit("PBO2", 879621, "Penulis", "$100", "Pemrograman Berorientasi Objek", "Pemrograman")
penulis_penerbitC.display_info()
