# 1. Cari angka dalam list menggunakan Linear dan Binary Search.

# Linear
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

angka = [1, 2, 3, 4, 5]
print(linear_search(angka, 3))