print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK ===")
n_1012 = int(input("Masukkan ukuran skala jam pasir (N): "))

# 1. Bingkai Pembatas Horizontal (Border Atas)
print("#", end="")
for i_1012 in range(4 * n_1012 + 5):
    print("=", end="")
print("#", end="")
print() # Pindah baris

# 2. Fase 1: Jam Pasir Atas (Reduksi Angka Menurun: Baris N turun s.d. 1)
for baris_1012 in range(n_1012, 0, -1):
    print("| ", end="") 
    
    # Spasi penyeimbang kiri
    for spasi_1012 in range(2 * (n_1012 - baris_1012)):
        print(" ", end="")
        
    # Deret angka mundur
    for angka_1012 in range(baris_1012, 0, -1):
        print(angka_1012, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju
    for angka_1012 in range(1, baris_1012 + 1):
        print(" ", end="")
        print(angka_1012, end="")
        
    # Spasi penyeimbang kanan
    for spasi_1012 in range(2 * (n_1012 - baris_1012)):
        print(" ", end="")
        
    print(" |", end="")
    print() # Pindah baris

# 3. Fase 2: Poros Titik Pusat Jam Pasir (Singularity)
print("|", end="")
for spasi_1012 in range(2 * n_1012 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_1012 in range(2 * n_1012 + 1):
    print(" ", end="")
print("|", end="")
print() # Pindah baris

# 4. Fase 3: Jam Pasir Bawah (Ekspansi Angka Menaik: Baris 1 naik s.d. N)
for baris_1012 in range(1, n_1012 + 1):
    print("| ", end="")
    
    # Spasi penyeimbang kiri
    for spasi_1012 in range(2 * (n_1012 - baris_1012)):
        print(" ", end="")
        
    # Deret angka mundur
    for angka_1012 in range(baris_1012, 0, -1):
        print(angka_1012, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju
    for angka_1012 in range(1, baris_1012 + 1):
        print(" ", end="")
        print(angka_1012, end="")
        
    # Spasi penyeimbang kanan
    for spasi_1012 in range(2 * (n_1012 - baris_1012)):
        print(" ", end="")
        
    print(" |", end="")
    print() # Pindah baris

# 5. Bingkai Pembatas Horizontal (Border Bawah)
print("#", end="")
for i_1012 in range(4 * n_1012 + 5):
    print("=", end="")
print("#", end="")
print() # Pindah baris