str_input = input('Tahun: ')
tahun = int(str_input)

if tahun % 4 == 0:
    print("tahun kabisat")
elif tahun % 400 == 0:
    print("tahun kabisat")
else:
    print("bukan tahun kabisat")

# if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#     print(tahun, "tahun kabisat")
# else:
#     print(tahun, "bukan tahun kabisat")