# Buat file dengan nama nested_for4_2611531012.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1012
# Program ini menggunakan fungsi input()

tinggi_1012 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1012 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1012 = tinggi_1012
    c_1012 = a_1012
    lebar_1012 = (2 * tinggi_1012) - 2

    for i_1012 in range(1, tinggi_1012 + 1):
        b_1012 = c_1012 + 1

        for j_1012 in range(1, lebar_1012 + 1):

            # Baris atas dan bawah
            if i_1012 == 1 or i_1012 == tinggi_1012:
                if j_1012 == 1 or j_1012 == lebar_1012:
                    print("#", end="")
                else:
                    print("=", end="")
                    
            # Baris isi
            else:
                if j_1012 == 1 or j_1012 == lebar_1012:
                    print("|", end="")
                else:
                    if j_1012 == c_1012:
                        print("<", end="")
                    elif j_1012 == b_1012:
                        print(">", end="")
                    elif j_1012 == (lebar_1012 - c_1012):
                        print("<", end="")
                    elif j_1012 == (lebar_1012 - c_1012 + 1):
                        print(">", end="")
                    elif j_1012 > b_1012 and j_1012 < (lebar_1012 - c_1012):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        # Logika asli Java
        a_1012 -= 2

        if a_1012 <= 0:
            c_1012 = (-a_1012) + 2
        else:
            c_1012 = a_1012