# Buat file dengan nama logika_2611531012.py
# Nama variabel ditambah 4 digit NIM terakhir contoh: a1_1012
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_1012 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_1012 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_1012)
print("A2 =", a2_1012)

# Konjungsi: bernilai True jika keduanya True
hasil_1012 = a1_1012 and a2_1012
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_1012)

# Disjungsi: bernilai True jika salah satunya True
hasil_1012 = a1_1012 or a2_1012
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_1012)

# Negasi A1: membalik nilai A1
hasil_1012 = not a1_1012
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_1012)

# Negasi A2: membalik nilai A2
hasil_1012 = not a2_1012
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_1012)

# XOR: bernilai True jika kedua nilai berbeda
hasil_1012 = a1_1012 != a2_1012
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_1012)