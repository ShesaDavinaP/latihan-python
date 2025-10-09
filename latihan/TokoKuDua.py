print("---Toko Sheesh Bercahaya Asek---")

def total(harga, jumlah):
    """Fungsi untuk menghitung Total bayar"""
    return harga * jumlah

def diskon(harga):
    """Fungsi menghitung diskon"""
    if harga <= 500000:
        potongan = harga * 0.1
    else:
        potongan = harga * 0.05 
    return potongan

def bayar(harga, potongan):
    """Fungsi menghitung total bayar setelah diskon"""
    return harga - potongan

# Input data
harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah baju yang dibeli: "))

Total = total(harga, jumlah)
Potongan = diskon(Total)
Bayar = bayar(Total, Potongan)

print("Total harga sebelum diskon = Rp.", Total)
print("Potongan harga = Rp.", Potongan)
print("Total yang harus dibayar=Rp.",Bayar)
