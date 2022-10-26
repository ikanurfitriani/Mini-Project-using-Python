print('*'*41)
print("MENENTUKAN BILANGAN TERBESAR DAN TERKECIL")
print('*'*41)

n = int(input("\nMasukan Jumlah Bilangan = "))
bil = []
sum = 0
for x in range(n):
    m=x+1
    a = int(input("Bilangan ke %d = "%m))
    bil.append(a)
    sum += bil[x]
    rata2 = sum / n
print("\nBilangan Terkecil : %d" %min(bil))
print("Bilangan Terbesar : %d" %max(bil))
print("Nilai Rata-rata   : %0.2f" %rata2)