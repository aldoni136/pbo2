class Lagu:

    def __init__(self, judul, penyanyi):
        self.judul = judul
        self.penyanyi = penyanyi

    def info(self):
        print(f"Judul: {self.judul}\nPenyanyi: {self.penyanyi}")

laguA = Lagu("Pujaan Hati", "Kangen Band")
laguA.info()