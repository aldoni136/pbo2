class Data:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Perusahaan:
    def __init__(self, nama, data):
        self.nama = nama
        self.data = data

    def daftar_data(self):
        for data in self.data:
            print(data.nama, data.umur)

data1 = Data("Andi", 25)
data2 = Data("Budi", 30)
data3 = Data("Siti", 20)
data4 = Data("Edo", 22)
data5 = Data("Wanto", 26)

perusahaan = Perusahaan("ABC", [data1, data2, data3, data4, data5])
perusahaan.daftar_data()