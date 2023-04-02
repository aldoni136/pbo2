class Menghitung:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=0):
        return a + b + c

mat = Menghitung()
B = mat.add(4, 7, 9)
print(B)

mut = Menghitung()
C = mut.add(9,7)
print(C)