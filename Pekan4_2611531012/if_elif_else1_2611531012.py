# Buat file dengan nama if_elif_else1_2611531012.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit NIM terakhir contoh: ipk_1012
# program ini menggunakan fungsi input()

umur_1012 = int(input("Input Umur Anda: "))
sim_1012 = input("Apakah Anda sudah memiliki SIM C? (y/t): ")[0]

if umur_1012 >= 17 and sim_1012 == "y":
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_1012 >= 17 and sim_1012 != "y":
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_1012 < 17 and sim_1012 == "y":
    print("Anda belum cukup umur punya SIM")
else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program Selesai")