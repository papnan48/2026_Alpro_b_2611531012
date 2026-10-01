# Buat file dengan nama nested_for1_2611531012.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1012
# program ini menggunakan fungsi input()

batas_1012 = int(input("Masukkan nilai batas: "))
for line_1012 in range(1, batas_1012 + 1):
    for j_1012 in range(1, (-1 * line_1012 + batas_1012) + 1):
        print(".", end=" ")
    print(line_1012)