# 3. Buat function sendiri untuk mencari nilai tertinggi dari sebuah list.

def nilai_maksimal(data):
    nilai_tertinggi = data[0]
    for nilai in data:
        if nilai > nilai_tertinggi:
            nilai_tertinggi = nilai
    return nilai_tertinggi

a = [30, 70, 100, 55, 50]
print(a)
print('Nilai terbesar:', nilai_maksimal(a))