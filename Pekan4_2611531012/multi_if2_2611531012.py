# Buat file dengan nama multi_if2_2611531012.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit NIM terakhir contoh: total_belanja_1012
# program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_1012 = float(input("Input Total Belanja Anda (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_1012 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member_1012 = input_member_1012 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_1012 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_1012 = input_promo_1012 in ["y", "ya"]

total_diskon_persen_1012 = 0

# Multi-IF terpisah: setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_1012 > 1000000:
    total_diskon_persen_1012 += 10 # Diskon belanja besar

if is_member_1012:
    total_diskon_persen_1012 += 5 # Diskon member

if kode_promo_valid_1012:
    total_diskon_persen_1012 += 15 # Diskon voucher

# menghitung nominal diskon dan total bayar
nominal_diskon_1012 = total_belanja_1012 * (total_diskon_persen_1012 / 100)
total_bayar_1012 = total_belanja_1012 - nominal_diskon_1012

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_1012}% (Rp {nominal_diskon_1012:,.0f})")
print(f"Total Bayar  : Rp {total_bayar_1012:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_1012}%")
# Output: Total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid