class Angkot:

    def __init__(self, titiktemu, tujuan):
        self.titiktemu = titiktemu
        self.tujuan = tujuan

    def info(self):
        print(f"Titik Temu: {self.titiktemu}\nTujuan: {self.tujuan}")

angkotA = Angkot("Jalan Juanda", "Cirebon")
angkotA.info()