# 2. Urutkan list nilai ujian menggunakan Bubble Sort.

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for u in range(0, n-i-1):
            if data[u] > data[u+1]:
                data[u], data[u+1] = data[u+1], data[u]
    return data

nilai_ujian = [93, 70, 88, 55, 60, 43, 100]
print(bubble_sort(nilai_ujian))