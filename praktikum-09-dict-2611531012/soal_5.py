n = int(input("Masukkan jumlah setoran: "))
kas = {}
for i in range(n):
    nama, nominal = input().split()
    nominal = int(nominal)

    if nama not in kas:
        kas[nama] = 0

    kas[nama] += nominal
for nama in kas:
    print(f"{nama}: {kas[nama]}")
total_kas = sum(kas.values())
print(f"Total cash: {total_kas}")
top_nama = max(kas, key=kas.get)
print(f"Top contributor: {top_nama} ({kas[top_nama]})")