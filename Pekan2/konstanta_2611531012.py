# Buat file dengan nama konstanta_2611531012.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran.
# Nama variabel ditambah 4 digit nim terakhir contoh: jari_1012

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_1012 = float(input("Masukkan nilai jari-jari: "))
luas_1012 = PI * jari_1012 * jari_1012
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1012, luas_1012))