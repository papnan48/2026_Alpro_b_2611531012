print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_1012 = input("Masukkan Nama Pengunjung        : ")
umur_1012 = int(input("Input umur anda                 : "))

# Mengambil huruf pertama dari input SIM untuk validasi
sim_input_1012 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
sim_1012 = sim_input_1012[0] if len(sim_input_1012) > 0 else 't'

print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_1012 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_1012 = int(input("Masukkan jumlah tiket           : "))
member_1012 = input("Apakah Anda member? (y/t)       : ").strip().lower()
promo_1012 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# Variabel flag untuk menghentikan eksekusi tanpa exit() atau nested-if
validasi_1012 = True

# If Tunggal untuk validasi kelogisan tiket
if jumlah_tiket_1012 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")
    validasi_1012 = False

harga_satuan_1012 = 0
nama_wahana_1012 = ""

# Match - Case beserta Case _
match paket_1012:
    case 1:
        nama_wahana_1012 = "Safari Rimba"
        harga_satuan_1012 = 50000
    case 2:
        nama_wahana_1012 = "Arung Jeram"
        harga_satuan_1012 = 75000
    case 3:
        nama_wahana_1012 = "Motor ATV Ekstrim"
        harga_satuan_1012 = 120000
    case 4:
        nama_wahana_1012 = "Roller Coaster Kilat"
        harga_satuan_1012 = 100000
    case 5:
        nama_wahana_1012 = "All-Access VIP"
        harga_satuan_1012 = 220000
    case _:
        print("Paket wahana tidak valid!")
        validasi_1012 = False

# Jika validasi_1012 bernilai False (tiket <= 0 atau paket tidak valid), 
# maka program akan melewati seluruh evaluasi di bawah ini secara otomatis.

if validasi_1012:
    print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

# If - Elif - Else terstruktur tanpa Nested If (if di dalam if)
if validasi_1012 and paket_1012 == 3 and umur_1012 >= 17 and sim_1012 == 'y':
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif validasi_1012 and paket_1012 == 3 and umur_1012 >= 17 and sim_1012 != 'y':
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
elif validasi_1012 and paket_1012 == 3 and umur_1012 < 17 and sim_1012 == 'y':
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif validasi_1012 and paket_1012 == 3:
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
elif validasi_1012 and umur_1012 >= 10:
    print(f"Status Akses: Umur Anda mencukupi untuk wahana {nama_wahana_1012}.")
elif validasi_1012:
    print(f"Status Akses: Anda belum cukup umur untuk wahana {nama_wahana_1012} (wajib didampingi orang tua).")

# Multi-IF terpisah untuk diskon akumulatif
subtotal_1012 = harga_satuan_1012 * jumlah_tiket_1012
total_diskon_persen_1012 = 0

if validasi_1012 and subtotal_1012 >= 200000:
    total_diskon_persen_1012 += 10
if validasi_1012 and member_1012 in ['y', 'ya']:
    total_diskon_persen_1012 += 5
if validasi_1012 and promo_1012 in ['y', 'ya']:
    total_diskon_persen_1012 += 15
if validasi_1012 and jumlah_tiket_1012 >= 5:
    total_diskon_persen_1012 += 5

# Kalkulasi Nominal Diskon dan Evaluasi Akhir
if validasi_1012:
    nominal_diskon_1012 = subtotal_1012 * (total_diskon_persen_1012 / 100)
    total_bayar_1012 = subtotal_1012 - nominal_diskon_1012

    print("\n--- Rincian Pembayaran ---")
    print(f"Subtotal Belanja : Rp {subtotal_1012:,.0f}")
    print(f"Total Diskon     : {total_diskon_persen_1012}% (Rp {nominal_diskon_1012:,.0f})")
    print(f"Total Bayar      : Rp {total_bayar_1012:,.0f}")

# Evaluasi if - else penutup audit
if validasi_1012 and total_bayar_1012 > 300000:
    print("Catatan Layanan  : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
elif validasi_1012:
    print("Catatan Layanan  : Terima kasih telah berkunjung.")