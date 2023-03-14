class Persegi:

    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def luas(self):
        return self.panjang * self.lebar
    
PersegiA = Persegi(10, 5)
print(f"Luas persegi: {PersegiA.luas()}")