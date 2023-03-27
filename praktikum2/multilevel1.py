class Handphone:
    def __init__(self, name):
        self.name = name

    def speaker(self):
        print("The Handphone speaker is powerfull")

class Samsung(Handphone):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speaker(self):
        print("The Handphone speaker is powerfull")

class Galaxy(Samsung):
    def __init__(self, name, color, price):
        super().__init__(name, color)
        self.price = price

    def speaker(self):
        print("The Handphone speaker is powerfull")