class Siswa:
    # atribut
    nis = ""
    nama = ""
    
    # constructor
    def __init__(self, x, y):
        self.nis = x
        self.nama = y
    
    # method
    def printSiswa(self):
        print("NIS :", self.nis)
        print("Nama :", self.nama)

# membuat objek sis1 dari class siswa
sis1 = Siswa("1234", "Martin Edwards")

# memberi nilai kedua atribut dari objek
# sis1.nis = "1234"
# sis1.nama = "martin"

# memanggil method 
sis1.printSiswa()