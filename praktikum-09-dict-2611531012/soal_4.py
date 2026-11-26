daftar_kelas = input("Daftar mahasiswa: ").split()
daftar_pengumpul = input("Mahasiswa yang mengumpulkan: ").split()
pengumpul = set(daftar_pengumpul)
belum_mengumpulkan = []
for nomor in daftar_kelas:
    if nomor not in pengumpul:
        belum_mengumpulkan.append(nomor)
print(f"Submitted: {len(pengumpul)} students")
print(f"Not submitted: {len(belum_mengumpulkan)} students")
for nomor in belum_mengumpulkan:
    print(nomor)