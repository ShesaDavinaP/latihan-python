# TRIK 1

class Penjumlahan:
    # method hasil() dengan variasi parameter
    def hasil(self, *args):
        if (len(args) <= 4):
            sum = 0
            for num in args:
                sum += num
            print(sum)
        else:
            print("Maksimum 4 argumen")

coba = Penjumlahan()
coba.hasil(1, 2)
coba.hasil(1, 2, 3, 4)
coba.hasil(1, 2, 30, 4)
coba.hasil(1, 2, 3, 4, 5, 6)