def total(harga, jumlah):
    """ fungsi untuk menghitung total bayar """
    return harga*jumlah

def diskon(harga):
    """ fungsi menghitung diskon """
    if (harga <= 500000):
        potongan = harga * 0.1
    else:
        potongan = harga * 0.05
    return potongan

def bayar(harga, potongan):
    """ fungsi menghitung total bayar """
    return harga - potongan