# Buat file dengan nama jumlah_genap_2611531012.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1012
# program ini menggunakan fungsi input()

ulang_1012 = int(input("Masukkan nilai batas: "))

jumlah_1012 = 0
for i_1012 in range(1, ulang_1012 + 1):
    if i_1012 % 2 == 0:
        print(i_1012, end=" ")
        jumlah_1012 = jumlah_1012 + i_1012

        if i_1012 < ulang_1012:
            print(" + ", end=" ")
        else:
            print(" = ", jumlah_1012, end=" ")
print()
print("Jumlah =", jumlah_1012)