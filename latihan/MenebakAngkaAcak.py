import random
# Menebak angka acak
angka_acak = random.randint(1, 100)
tebakan = 0
while True:
    tebakan = int(input("Tebak angka (1-100): "))
    if tebakan < angka_acak:
        print("Angka terlalu kecil, coba lagi!")
    elif tebakan > angka_acak:
        print("Angka terlalu besar, coba lagi!")
    else:
        print("Selamat, tebakan anda benar!")
        break

"""
Penjelasan:

Baris pertama digunakan untuk mengimpor modul random yang memungkinkan komputer menghasilkan angka acak.
Pada baris ketiga, sebuah angka acak antara 1 hingga 100 akan dihasilkan dan disimpan dalam variabel angka_acak.
Variabel tebakan digunakan untuk menghitung jumlah tebakan yang dilakukan oleh pengguna.
Pengulangan while True: digunakan untuk mengulang proses menebak angka sampai tebakan benar.
Setiap kali pengguna diminta untuk memasukkan tebakan, perbandingan dilakukan dengan angka_acak.
Jika tebakan terlalu kecil, pesan "Angka terlalu kecilm coba lagi!" akan ditampilkan, 
Sebaliknya, jika tebakan terlalu besar, pesan "Angka terlalu besar, coba lagi!" akan muncul di layar.
Apabila tebakan benar, pesan "Selamat, tebakan anda benar!" akan ditampilkan, dan pengulangan dihentikan dengan break.
"""