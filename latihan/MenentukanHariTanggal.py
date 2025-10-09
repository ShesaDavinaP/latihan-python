# Menentukan hari dan tanggal
import datetime

tahun = int(input("Masukkan tahun: "))
bulan = int(input("Masukkan bulan: "))
tanggal = int(input("Masukkan tanggal: "))

tanggal_input = datetime.date(tahun, bulan, tanggal)
nama_hari = tanggal_input.strftime("%A")
tanggal_format = tanggal_input.strftime("%d %B %Y")

print("Tanggal", tanggal_format, "adalah hari ", nama_hari)

"""
Penjelasan:

Baris kedua mengimpor modul datetime untuk mengambil informasi tanggal dan waktu.
Variabel tahun, bulan, dan tanggal digunakan untuk menyimpan input dari pengguna.
Pada baris kelima, kami membuat objek tanggal_input menggunakan data yang diinputkan oleh pengguna.
Objek tanggal_input kemudian digunakan untuk mendapatkan nama hari dengan menggunakan method .strftime("%A").
Selanjutnya, tanggal_input diformat untuk mencetak tanggal dalam format "tanggal bulan tahun" dengan method .strftime("%d %B %Y")
"""