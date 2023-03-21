class Laptop:
    def __init__(self, merk, tipe):
        self.merk = merk
        self.tipe = tipe

    def gaming(self):
        print(f"{self.merk} kuat bermain game berat.")

class Fitur(Laptop):
    def __init__(self, merk, tipe, plus):
        super().__init__(merk, tipe)
        self.plus = plus

    def kelebihan(self):
        print(f"{self.merk} dengan Fitur {self.plus} teknologinya canggih.")

FiturA = Fitur("ASUS", 312, "ROG")
FiturA.gaming() # Output: ASUS kuat bermain game berat
FiturA.kelebihan() # Output: ASUS dengan Fitur ROG teknologinya canggih