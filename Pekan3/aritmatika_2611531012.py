# Buat file dengan nama aritmatika_2611531012.py
# Buat program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit NIM terakhir contoh: angka1_1012
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_1012 = int(input("Input angka-1: "))
angka2_1012 = int(input("Input angka-2: "))

# Penjumlahan
hasil_1012 = angka1_1012 + angka2_1012
print("\nOperator Penjumlahan")
print("Hasil =", hasil_1012)

# Pengurangan
hasil_1012 = angka1_1012 - angka2_1012
print("\nOperator Pengurangan")
print("Hasil =", hasil_1012)

# Perkalian
hasil_1012 = angka1_1012 * angka2_1012
print ("\nOperator Perkalian")
print("Hasil =", hasil_1012)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_1012 !=0:
    hasil_1012 = angka1_1012 / angka2_1012
    print("\nOperator Pembagian")
    print("Hasil =", hasil_1012)

    hasil_1012 = angka1_1012 // angka2_1012
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_1012)

    hasil_1012 = angka1_1012 % angka2_1012
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_1012)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_1012 = angka1_1012 ** angka2_1012
print("\nOperator Pangkat")
print("Hasil =", hasil_1012)