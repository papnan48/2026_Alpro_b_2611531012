# Buat file dengan nama bitwise_2611531012.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1012
# Program ini menggunakan fungsi input()

print("\n=============================")
print("3. OPERATOR BITWISE")
print("=============================")

angka1_1012 = int(input("Masukkan angka bitwise-1: "))
angka2_1012 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_1012, "| biner =", bin(angka1_1012))
print("angka2 =", angka2_1012, "| biner =", bin(angka2_1012))

# Bitwise AND
hasil_1012 = angka1_1012 & angka2_1012
print("\nBitwise AND (&)")
print(angka1_1012, "&", angka2_1012, "=", hasil_1012)
print("Biner hasil =", bin(hasil_1012))
print("Biner hasil (8 bit) =", format(hasil_1012, "08b"))

# Bitwise OR
hasil_1012 = angka1_1012 | angka2_1012
print("\nBitwise OR (|)")
print(angka1_1012, "|", angka2_1012, "=", hasil_1012)
print("Biner hasil =", bin(hasil_1012))
print("Biner hasil (8 bit) =", format(hasil_1012, "08b"))

# Bitwise XOR
hasil_1012 = angka1_1012 ^ angka2_1012
print("\nBitwise XOR (^)")
print(angka1_1012, "^", angka2_1012, "=", hasil_1012)
print("Biner hasil =", bin(hasil_1012))
print("Biner hasil (8 bit) =", format(hasil_1012, "08b"))

# Bitwise NOT
hasil_1012 = ~angka1_1012
print("\nBitwise NOT (~)")
print("~", angka1_1012, "=", hasil_1012)
print("Biner hasil =", bin(hasil_1012))
print("Biner hasil (8 bit) =", format(hasil_1012, "08b"))

# Bitwise geser kiri
jumlah_geser_1012 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_1012 = angka1_1012 << jumlah_geser_1012
print("\nBitwise geser kiri (<<)")
print(angka1_1012, "<<", jumlah_geser_1012, "=", hasil_1012)
print("Biner hasil =", bin(hasil_1012))
print("Biner hasil (8 bit) =", format(hasil_1012, "08b"))

# Bitwise geser kanan
hasil_1012 = angka1_1012 >> jumlah_geser_1012
print("\nBitwise geser kanan (>>)")
print(angka1_1012, ">>", jumlah_geser_1012, "=", hasil_1012)
print("Biner hasil =", bin(hasil_1012))
print("Biner hasil (8 bit) =", format(hasil_1012, "08b"))