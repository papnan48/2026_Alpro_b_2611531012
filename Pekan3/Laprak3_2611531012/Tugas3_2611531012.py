# tugas3_2611531012.py
# Sistem Simulasi Transaksi dan Validasi Akses Toko

print("=== SISTEM TRANSAKSI TOKO ===\n")

# Input Data Pelanggan
nama_1012 = input("Masukkan Nama Pelanggan : ")
status_1012 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_1012 = int(input("Masukkan Total Belanja : "))
jumlah_barang_1012 = int(input("Masukkan Jumlah Barang : "))
kode_promo_input_1012 = input("Masukkan Kode Promo : ")

# Operator Keanggotaan
daftar_promo_1012 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
promo_tersedia_1012 = kode_promo_input_1012 in daftar_promo_1012
promo_tidak_valid_1012 = kode_promo_input_1012 not in daftar_promo_1012

# Operator Perbandingan & Logika
syarat_belanja_1012 = total_belanja_1012 >= 200000
syarat_barang_1012 = jumlah_barang_1012 >= 3
is_member_1012 = status_1012 == "member"

# Logika Penggabungan (and)
dapat_diskon_1012 = is_member_1012 and syarat_belanja_1012
dapat_promo_1012 = promo_tersedia_1012 and syarat_barang_1012

# Operator Identitas
promo_ref_1012 = daftar_promo_1012
promo_copy_1012 = daftar_promo_1012.copy()
# Membuktikan identitas objek
is_same_object_1012 = promo_ref_1012 is daftar_promo_1012
is_diff_object_1012 = promo_copy_1012 is not daftar_promo_1012

# Operator Aritmatika & Penugasan
besaran_diskon_1012 = 0
if dapat_diskon_1012:
    besaran_diskon_1012 = total_belanja_1012 * 10 // 100  # Diskon 10% (Aritmatika Perkalian & Pembagian Bulat)

# Assignment
total_pembayaran_1012 = total_belanja_1012
total_pembayaran_1012 -= besaran_diskon_1012  # Augmented assignment pengurangan

# Aritmatika lanjutan
rata_rata_harga_1012 = total_belanja_1012 // jumlah_barang_1012
sisa_bagi_1012 = total_belanja_1012 % jumlah_barang_1012

# 6. Operator Bitwise
# 0001 (1) = Member | 0010 (2) = Belanja >= 200k | 0100 (4) = Barang >= 3 | 1000 (8) = Promo
status_code_1012 = 0
if is_member_1012: status_code_1012 |= 1
if syarat_belanja_1012: status_code_1012 |= 2
if syarat_barang_1012: status_code_1012 |= 4
if promo_tersedia_1012: status_code_1012 |= 8

cek_member_bitwise_1012 = status_code_1012 & 1
cek_promo_bitwise_1012 = status_code_1012 & 8

# Perbandingan Status (XOR) dan Shift
kode_referensi_1012 = 11  # 1011 Biner
hasil_xor_1012 = status_code_1012 ^ kode_referensi_1012
shift_kiri_1012 = status_code_1012 << 1

# === OUTPUT PROGRAM ===
print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan       : {nama_1012}")
print(f"Status Pelanggan     : {status_1012}")
print(f"Total Belanja        : Rp{total_belanja_1012}")
print(f"Jumlah Barang        : {jumlah_barang_1012}")
print(f"Kode Promo           : {kode_promo_input_1012}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {syarat_belanja_1012}")
print(f"Jumlah Barang >= 3         : {syarat_barang_1012}")
print(f"Status Member              : {is_member_1012}")
print(f"Kode Promo Tersedia        : {promo_tersedia_1012}")
print(f"Mendapatkan Diskon         : {dapat_diskon_1012}")
print(f"Mendapatkan Promo          : {dapat_promo_1012}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                     : Rp{besaran_diskon_1012}")
print(f"Total Pembayaran           : Rp{total_pembayaran_1012}")
print(f"Rata-rata Harga Barang     : Rp{rata_rata_harga_1012}")
print(f"Sisa Bagi (Modulus)        : Rp{sisa_bagi_1012}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses             : {format(status_code_1012, '04b')}")
print(f"Member Access              : {bool(cek_member_bitwise_1012)}")
print(f"Promo Access               : {bool(cek_promo_bitwise_1012)}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print(f"Kode Biner   : {format(status_code_1012, '04b')}")
print(f"Kode Desimal : {status_code_1012}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(status_code_1012, '04b')} & 0001")
print(f"Hasil Biner   : {format(cek_member_bitwise_1012, '04b')}")
print(f"Hasil Desimal : {cek_member_bitwise_1012}")

print("\nCek Promo")
print(f"{format(status_code_1012, '04b')} & 1000")
print(f"Hasil Biner   : {format(cek_promo_bitwise_1012, '04b')}")
print(f"Hasil Desimal : {cek_promo_bitwise_1012}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {format(status_code_1012, '04b')}")
print(f"Kode Referensi : {format(kode_referensi_1012, '04b')}")
print(f"{format(status_code_1012, '04b')} ^ {format(kode_referensi_1012, '04b')}")
print(f"Hasil Biner   : {format(hasil_xor_1012, '04b')}")
print(f"Hasil Desimal : {hasil_xor_1012}")

print("\n=== Shift ===")
print(f"{format(status_code_1012, '04b')} << 1")
print(f"Hasil Biner   : {format(shift_kiri_1012, '05b')}")
print(f"Hasil Desimal : {shift_kiri_1012}")
print("\n=== SELESAI ===")