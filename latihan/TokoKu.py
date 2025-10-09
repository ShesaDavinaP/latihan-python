print("---Toko Sheesh Bercahaya Asek---")
def total(harga, jumlah):
    """fungsi untuk menghitung total bayar"""
    return harga*jumlah
# input data
harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah baju yang dibeli: "))
Total = total(harga, jumlah)
# diskon 5% tiap pembelian di atas Rp 100.000
if Total > 100000:
    Total = Total - 0.05  * Total
print("Total harga = ", "Rp.", Total)
Bayar = int(input("Jumlah nominal uang = " ))
Kembalian = (Bayar-Total)
print("Uang kembalian = ", "Rp.", Kembalian)

"""
Penjelasan:

Baris kedua sampai keempat menunjukan fungsi perhitungan total yang harus dibayarkan.
Kata kunci yang menyatakan sebuah fungsi adalah def dilanjutkan dengan tab sebagai indikator
bahwa statement tersebut adalah fungsi. Pada baris ke 10 dan ke 11 diperkenalkan cara
menggunakan if untuk pengecekan kondisi tertentu, misalnya apa perlu diberi diskon atau tida.
"""