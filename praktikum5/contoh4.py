dictionary = {"empat": 4, "lima": 5, "enam": 6}
try:
    value = dictionary["sepuluh"]
except KeyError:
    print("Key yang diminta tidak ditemukan pada dictionary!")