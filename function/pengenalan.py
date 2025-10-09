# def say_hello():
#     print("helloooww")
    
# say_hello()

# def print_something():
#     print("hello")
    
#     today = "wednesday"
#     print(f"happy {today}")
    
#     for i in range(5):
#         print(f"i: {i}")
        
# print_something()


# A. Pengenalan Fungsi
# Function atau fungsi adalah kode program yang terisolasi dalam satu blok kode, yang bisa dipanggil sewaktu-waktu. Fungsi memiliki beberapa    atribut seperti nama fungsi, isi fungsi, parameter/argument, dan nilai balik.
# pembuatan fungsi dilakukan dengan keyword def diikuti dengan nama fungsi, lalu dibawahnya ditulis body/isi fungsi.

# sebagai contoh pada kode berikut fungsi say_hello() dideklarasikan dengan isi adalah sebuah statement yang menampilkan text hello.

# def say_hello():
#     print("hello")
    
# setelah dideklarasikan, fungsi bisa dipanggil berkali-kali. misalnya pada contoh berikut

# say_hello()
# say_hello()
# say_hello()

# suatu fungsi hanya bisa diakses atau dipanggil setelah fungsi tersebut dideklarasikan (statement pemanggilan fungsi harus dibawah statement deklarasi fungsi). jika fungsi dipaksa digunakan sebelum dideklarasikan hasilnya error.

# contoh
# say_hello()
# def say_hello():
#     print("hello")
    
# fungsi dengan banyak statement

def print_something():
    print("helllo")
    
    today = "Sunday"
    print(f"happy {today}")
    
    for i in range(5):
        print(f"i: {i}")
print_something()

# isi statement posisinya tidak boleh sejajar dengan blok deklarasi fungsi (secara vertikal). isi fungsi harus lebih menjorok ke kanan.

# parameter dan argument fungsi

# fungsi bisa memiliki parameter. dengan adanya parameter, suatu nilai bisa disisipkan ke dalam fungsi secara otomatis

# parameter sendiri merupakan istilah untuk variable yang menempel pada fungsi, yang mengharuskan kita untuk menyisipkan nilai pada parameter tersebut saat pemanggilan fungsi.

# contoh

def calculate_circle_area(r):
    area = 3.14 * (r ** 2)
    print("area of circle:", area)

calculate_circle_area(788)
# output -> area of circle: 1949764.160000001

# penjelasan
# - fungsi calculate_circle_area() dideklarasikan memiliki parameter bernama r
# - notasi penulisan parameter fungsi ada diantara penulisan kurung () milik blok deklarasi fungsi
# - tugas fungsi calculate_circle_area() adalah menghitung luas lingkaran dengan nilai jari-jari didapat dari parameter r. Nilai luas lingkaran kemudian di-print
# setelah blok deklarasi fungsi, ada statement pemanggilan fungsi calculate_circle_area(). Nilai numerik 788 digunakan sebagai argument parameter r pemanggilan fungsi tersebut.

# parameter by default bisa menerima segala jenis tipe data. untuk memaks suatu parameter agar hanya bisa menerima data tertentu, maka tulis tipe data yang diinginkan dengan notasi penulisan sama seperti deklarasi variabel

# perhatikan contoh berikut agar lebih jelas
# fungsi calculate_circle_area() di atas di-refactor menjadi fungsi dengan 2 parameter yaitu message bertipe string dan r bertipe int

def calculate_circle_area(message: str, r: int):
    area = 3.14 * (r ** 2)
    print(message, area)
    
calculate_circle_area("area of circle:", 788)

# nama fungsi dianjurkan untuk ditulis menggunakan snake_case
# penulisan nama parameter/argument adalah sama seperti nama variable, yaitu menggunakan snake_case juga.