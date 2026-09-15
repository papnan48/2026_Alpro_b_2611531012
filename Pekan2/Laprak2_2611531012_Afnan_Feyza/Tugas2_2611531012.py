# Kode program tugas "tugas2_1012.py"

from typing import Final

# Konstanta batas kelulusan
BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_1012 = input("Masukkan Nama Mahasiswa\t\t: ")
jenis_kelamin_1012 = input("Masukkan Jenis Kelamin (L/P)\t: ")
umur_1012 = int(input("Masukkan Umur\t\t\t: "))
skor_tes_1012 = float(input("Masukkan Skor Tes Awal\t\t: "))

# Deklarasi alamat secara multiline
alamat_1012 = """Jl. Kakak Tua No 2, 
Kecamatan Padang Utara, Kelurahan Air Tawar Barat,
Kota Padang"""

# Token identifikasi menggunakan bilangan kompleks
token_1012 = 100+3j

# Evaluasi status kelulusan
status_lulus_1012 = skor_tes_1012 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa\t:", nama_1012, "| Tipe:", type(nama_1012))
print("Jenis Kelamin\t:", jenis_kelamin_1012, "| Tipe:", type(jenis_kelamin_1012))
print("Alamat Domisili\t:\n" + alamat_1012, "\n| Tipe:", type(alamat_1012))
print("Umur\t\t:", umur_1012, "tahun | Tipe:", type(umur_1012))
print("Skor Tes Awal\t:", skor_tes_1012, "| Tipe:", type(skor_tes_1012))
print("ID Token Sinyal\t:", token_1012, "| Tipe:", type(token_1012))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", status_lulus_1012, "| Tipe:", type(status_lulus_1012))