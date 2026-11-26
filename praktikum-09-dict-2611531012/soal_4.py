daftar_kelas = input("Ketikkan nomor absen: ").split()
daftar_pengumpul = input("Ketikkan nomor absen yang mengumpulkan: ").split()

pengumpul = set(daftar_pengumpul)
belum_mengumpulkan = set(daftar_kelas) - pengumpul

print(f"Submitted: {len(pengumpul)} students")
print(f"Not submitted: {len(belum_mengumpulkan)} students")

for nomor in daftar_kelas:
    if nomor not in pengumpul:
        print(nomor)