print('*'*41)
print("MENGURUTKAN BILANGAN TERKECIL KE TERBESAR")
print("-----  DENGAN METODE INSERTION SORT -----")
print('*'*41)

bil = []
n = int(input("\nMasukan Jumlah Bilangan = "))

for x in range(n):
    m=x+1
    a = int(input("Bilangan ke %d = "%m))
    bil.append(a)
print("\nList Bilangan yang Anda Masukan = ", bil)

for i in range(len(bil)):  
    for j in range(0, i):  
        if (bil[i] < bil[j]):  
            temp = bil[i]  
            bil[i] = bil[j]  
            bil[j] = temp

print("\nHasil Pengurutan = ", bil)