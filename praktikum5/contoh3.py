try:
    with open("file_kosong.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File yang diakses atau dicari tidak ditemukan!")