nama_depan = "shesa"
nama_belakang = "davina"

print(nama_depan + " " + nama_belakang)

sample_list = [2,3,4]
is_3_exists = 3 in sample_list
print(is_3_exists)

sample_tuple = ("hello", "py")
is_hello_exists = "hello" in sample_tuple
print(is_hello_exists)

sample_dict = {"nama" : "lino", "age": 27}
is_key_nama_exists = "lino" in sample_dict # in bakal ngecheck key, bukan valuenya
print(is_key_nama_exists)

sample_set = {"sesuk", "preiiii"}
is_prei = "preii" in sample_set
print(is_prei)

text = 'Hello world'
is_substring_exists = 'orl' in text
print(is_substring_exists)