class Binatang:
    def bersuara(self):
        print("Suara binatang")

class Dog(Binatang):
    def bersuara(self):
        print("The dog barks")

class Cat(Binatang):
    def bersuara(self):
        print("The cat meows")

class Chihuahua(Dog):
    def bersuara(self):
        print("The chihuahua yaps")

class Siamese(Cat):
    def bersuara(self):
        print("The Siamese purrs")

def binatang_sound(binatang):
    binatang.bersuara()

# Instantiate objects of each class
binatang = Binatang()
dog = Dog()
cat = Cat()
chihuahua = Chihuahua()
siamese = Siamese()

# Call the binatang_sound function for each object
binatang_sound(binatang) # Output: Suara binatang
binatang_sound(dog) # Output: The dog barks
binatang_sound(cat) # Output: The cat meows
binatang_sound(chihuahua) # Output: The chihuahua yaps
binatang_sound(siamese) # Output: The Siamese purrs