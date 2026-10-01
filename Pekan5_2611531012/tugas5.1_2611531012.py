# Soal: Buatlah proghgram untuk menampilkan output dibawah menggunakan perulangan for
# Ex: Masukkan tinggi segitiga: 5
# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

tinggi_1012 = int(input("Masukkan tinggi segitiga: "))

for i_1012 in range(1, tinggi_1012 + 1):
    for j_1012 in range(tinggi_1012 - i_1012):
        print(" ", end="")
    for k_1012 in range(i_1012):
        print("* ", end="")
    print()
