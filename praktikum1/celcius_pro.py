class Celcius:

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273
    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5

mycelcius = 45
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
mykelvin = Celcius.to_kelvin(mycelcius)
myreamur = Celcius.to_reamur(mycelcius)

print("konversi ",mycelcius, "derajat celcius adalah ",myfahrenheit, "derajat fahrenheit")
print("konversi ",mycelcius, "derajat celcius adalah ",mykelvin, "derajat kelvin")
print("konversi ",mycelcius, "derajat celcius adalah ",myreamur, "derajat reamur")
