kata = input("Masukkan kata-kata yang akan diurutkan (pisahkan dengan spasi): ")
daftar_kata = kata.split()
daftar_kata.sort()
kata_urut = ' '.join(daftar_kata)
print("Kata-kata setelah diurutkan: ", kata_urut)

"""
Penjelasan:

Baris kedua mengambil input dari pengguna dalam bentuk kata-kata yang dipisahkan oleh spasi dan
menyimpannya dalam variabel kata. Pada baris ketiga, kata-kata tersebut dipisahkan menggunakan method split().
Selanjutnya, daftar kata diurutkan sesuai urutan abjad menggunakan method sort() pada baris keempat.
Baris kelima menggabungkan kata-kata yang sudah diurutkan kembali menggunakan method join(),
dipisahkan dengan tanda spasi (' ').
"""
