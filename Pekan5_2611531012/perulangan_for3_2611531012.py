# Buat file dengan nama perulangan_for3_2611531012.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1012
# program ini menggunakan fungsi input()

ulang_1012 = int(input("Masukkan jumlah perulangan: "))

jumlah_1012 = 0
for i_1012 in range(1, ulang_1012 + 1):
    print(i_1012, end=" ")
    jumlah_1012 = jumlah_1012 + i_1012

    if i_1012 < ulang_1012:
        print(" + ", end=" ")
    else:
        print(" = ", jumlah_1012, end=" ")

print()
print("Jumlah =", jumlah_1012)