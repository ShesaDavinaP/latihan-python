# tipe data numerik
number_1 = 100009   # ini int
number_2 = 100.56   # ini float
number_3 = 120+3j   # ini complex

# tipe data string
# string sebaris pakai ""
string_1 = "hello python"

# string multi-baris
string_2 = """Selamat
Belajar
Python"""

# string sebaris pakai ''
string_3 = 'for the horde!'

# string multi-baris
string_4 = '''
Sesuk
Preiiii
'''

# kalo mau ada baris baru di awal penulisan """ atau ''', kalo mau  meng-exclude-nya bisa pakai '''\ atau """\


# tipe data boolean
bool_1 = True
bool_2 = False

# tipe data none -> null atau nil di bahasa lain
data = "hello"
print(data)

data = None
print(data)


# tipe data list
# list int
list_1 = [2, 4, 8, 16]

# list str
list_2 = ["shesa", "lino", "mingi", "mark lee"]

# list variasi
list_3 = [25, True, "step out!"]

print(list_3[2])

# tipe data tuple -> nilai data tidak bisa diubah
# perbedaannya: tuple memakai ()
tuple_1 = (3, False, "being myself")
print(tuple_1[0])

# tipe data dictionary
profile_1 = {
    "name": "minho",
    "hobbies": ["dancing", "coding"]
}

print("name: %s" % (profile_1["name"]))
print("hobbies: %s" % (profile_1["hobbies"]))

# tipe data set
# Tidak bisa menyimpan informasi urutan data
# Elemen data yang sudah dideklarasikan tidak bisa diubah nilainya (tapi bisa dihapus)
# Tidak bisa diakses menggunakan index (tetapi bisa menggunakan perulangan)

set_1 = {"pineapple", "spaghetti"}
print(set_1)