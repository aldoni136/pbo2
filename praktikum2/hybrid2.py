class Seseorang:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    def get_info(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)
        print("Alamat:", self.alamat)
# Single Inheritance
class Mahasiswa(Seseorang):
    def __init__(self, nama, umur, alamat, student_id):
        super().__init__(nama, umur, alamat)
        self.student_id = student_id
    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)
# Single Inheritance
class Karyawan(Seseorang):
    def __init__(self, nama, umur, alamat, karyawan_id, salary):
        super().__init__(nama, umur, alamat)
        self.karyawan_id = karyawan_id
        self.salary = salary
    def get_info(self):
        super().get_info()
        print("Karyawan ID:", self.karyawan_id)
        print("Salary:", self.salary)
# Multiple Inheritance
class Penulis(Karyawan, Mahasiswa):
    def __init__(self, nama, umur, alamat, karyawan_id, salary, student_id, published_books):
        karyawan.__init__(self, nama, umur, alamat, karyawan_id, salary)
        Mahasiswa.__init__(self, nama, umur, alamat, student_id)
        self.published_books = published_books
    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)
        print("Published Books:", self.published_books)