# Buat file dengan nama lainnya_2611531012.py
# Nama variabel ditambah 4 digit terakhir contoh: angka1_1012
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("=================================")
print("1, OPERATOR KEANGGOTAAN")
print("=================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1012 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_1012 = [int(angka.strip()) for angka in input_data_1012.split(",")]

nilai_dicari_1012 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_1012 = nilai_dicari_1012 in data_1012
print ("\nOperator keanggotaan IN")
print(nilai_dicari_1012, "in", data_1012, "=", hasil_1012)

# Operator not in
hasil_1012 = nilai_dicari_1012 not in data_1012
print ("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1012, "not in", data_1012, "=", hasil_1012)


print("\n============================")
print("2. OPERATOR IDENTITAS")
print("============================")

# objek1 menggunakan list dari input pengguna
objek1_1012 = data_1012

# objek2 merujuk pada objek yang sama dengan objek 1
objek2_1012 = objek1_1012

# objek2 memiliki isi sama, tetapi merupakan objek baru
objek3_1012 = data_1012.copy()

print("objek1 =", objek1_1012)
print("objek2 =", objek2_1012)
print("objek3 =", objek3_1012)

# Operator is
hasil_1012 = objek1_1012 is objek2_1012
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_1012)

# Operator is not
hasil_1012 = objek1_1012 is not objek3_1012
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_1012)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek 3 =", objek1_1012 is objek3_1012)
print("objek1 == objek3 =", objek1_1012 == objek3_1012)