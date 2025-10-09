# Menghitung rata-rata
jumlah_angka = int(input("Masukkan jumlah angka: "))
total = 0
for i in range(jumlah_angka):
    angka = float(input("Masukkan angka ke-{}:".format(i + 1)))
    total += angka
rata_rata = total / jumlah_angka
print("Rata-rata dari angka-angka tersebut adalah ", rata_rata)

"""
Penjelasan:

Baris kedua mengambil input dari pengguna dengan tipe data int yang akan dihitung rata-ratanya,
lalu menyimpannya dalam variabel jumlah_angka.
Baris ketiga membuat variabel total untuk menghitung jumlah total dari angka-angka yang diinputkan.
Pengulangan for digunakan pada baris keempat untuk menghitung jumlah_angka,
setiap kali pengguna diminta untuk menginput angka.
Semua angka yang diinputkan ditambahkan ke total.
Pada baris ketujuh, rata-rata dihitung dengan membagi total dengan jumlah_angka
"""