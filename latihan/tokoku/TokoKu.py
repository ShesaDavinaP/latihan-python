from Diskon import total, diskon, bayar

print(" TokoKu ")

# input data
harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang yang dibeli: "))
Total = total(harga, jumlah)
potongan = diskon(Total)
tagihan = bayar(Total, potongan)

print("Total harga = ", "Rp. ", Total)
print("Diskon = ", "Rp. ", potongan)

Bayar = int(input("Jumlah nominal uang = "))
Kembalian = int(Bayar-tagihan)
print("Uang kembalian = ", "Rp. ", Kembalian)