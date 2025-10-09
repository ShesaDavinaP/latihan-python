from typing import Final

PI: Final = 3.14
print("phi: %f" % (PI))

# tipe konstanta PI tidak ditentukan secara explisit,
# melainkan didapat dari tipe data nilai
PI: Final = 3.14
# tipe konstanta TOTAL_MONTH ditentukan secara explisit yaitu `int`
TOTAL_MONTH: Final[int] = 12
# buat namain konstanta tuh harus pake capslock dan snack case  