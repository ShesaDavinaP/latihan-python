# Menghitung umur (dalam tahun, bulan, hari)
from datetime import datetime

tanggal_lahir = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")

tanggal_sekarang = datetime.now()
umur = tanggal_sekarang - tanggal_lahir

umur_tahun = umur.days // 365
sisa_hari = umur.days % 365
umur_bulan = sisa_hari // 30
sisa_hari = sisa_hari % 30
print("Umur anda; ", umur_tahun, "tahun, ", umur_bulan, "bulan, ", sisa_hari, "hari")

"""
Penjelasan:

Baris kedua mengimpor mmodul datetime dari library Python untuk menyediakan informasi tanggal dan waktu.
Pada baris keempat, input tanggal lahir diminta dari pengguna an disimpan sebagai objek datetime menggunakan datetime.strptime() dan
format "%Y-%m-%d".
Objek tanggal_sekarang dibuat untuk mewakili tanggal dan waktu saat ini.
Perhitungan umur dilakukan dengan mengurangkan tanggal lahir dari tanggal sekarang.
Pembagian umur.days // 365 menghasilkan umur dalam tahun.
Sisa hari dari pembagian sebelumnya kemudia dibagi lagi untuk mendapatkan umur dalam bulan dan sisa hari.
"""