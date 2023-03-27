# Single Inheritance
class Variabel:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Single Inheritance
class Bergambar:
    def draw(self):
        print("isi : ", self.x, self.y)

# Single Inheritance
class Bergerak:
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Multiple Inheritance
class Player(Variabel, Bergambar, Bergerak):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self):
        self.move(1, 1)
        self.draw()