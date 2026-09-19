# Buat file dengan nama assignment_2611531012.py
# Nama variabel ditambah 4 digit NIM terakhir contoh: angka1_1012
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam python

angka1_1012 = int(input("Input angka-1: "))
angka2_1012 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_1012)
print("\nNilai angka2 =", angka2_1012)

# Assignmant biasa
hasil_1012 = angka1_1012
print("\nAssignment biasa (=)")
print("Hasil =", hasil_1012)

# Assignment penambahan
hasil_1012 = angka1_1012
hasil_1012 += angka2_1012
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_1012)

# Assignment pengurangan
hasil_1012 = angka1_1012
hasil_1012 -= angka2_1012
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_1012)

# Assignment perkalian
hasil_1012 = angka1_1012
hasil_1012 *= angka2_1012
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_1012)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_1012 !=0:
    hasil_1012 = angka1_1012
    hasil_1012 /= angka2_1012
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_1012)
    # Operator tambahan
    hasil_1012 = angka1_1012
    hasil_1012 //= angka2_1012
    print("\nAssignment pembagian bulat(//=)")
    print("Hasil =", hasil_1012)
    hasil_1012 = angka1_1012
    hasil_1012 %= angka2_1012
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_1012)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_1012 = angka1_1012
hasil_1012 **= angka2_1012
print("\nAssignment perpangkatan (**=)")
<<<<<<< HEAD
print("Hasil =", hasil_1012)
=======
print("Hasil =", hasil_1012)
>>>>>>> 21223a7e2c6f80970163afb5fd14f6e5d558ec33
