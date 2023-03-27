class Rumah:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

class Kosan(Rumah):
    def __init__(self, name, color, price):
        super().__init__(name, color)
        self.price = price

    def get_price(self):
        return self.price

class Kontrakan(Rumah):
    def __init__(self, name, color, room):
        super().__init__(name, color)
        self.room = room

    def get_room(self):
        return self.room

# Hierarchical Inheritance
class Sewa(Kosan):
    def __init__(self, name, color, price, scale):
        super().__init__(name, color, price)
        self.scale = scale

    def get_scale(self):
        return self.scale