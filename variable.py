nama = "Shesa"
hobi = 'ngerajut'
umur = 16
cewe = True

print("----- biodata -----")
print("nama: %s" % (nama))
print("hobi: %s, umur: %d, cewe: %r" % (hobi, umur, cewe))
# %s => string, %d => integer, %r => boolean, %f => float

# tipe datanya bisa ditentukan secara eksplisit
nama: str = "Shesa"
hobi: str = 'ngerajut'
umur: int = 16
cewe: bool = True
pesan: str = 'halo, selamat pagi'
nilai_ujian: float = 98.8   # dianjurkan pake snake case

# bisa deklarasi variabel langsung banyak
nilai1, nilai2, nilai3, nilai4 = 88, 99, 77, 66
nilai_rata_rata = (nilai1 + nilai2 + nilai3 + nilai4) / 4

print("nilai rata rata: %f" % (nilai_rata_rata))