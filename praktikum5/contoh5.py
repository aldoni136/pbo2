list_angka = [7, 8, 9]
try:
    value = list_angka[3]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")