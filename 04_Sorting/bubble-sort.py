print('*'*41)
print("MENGURUTKAN BILANGAN TERKECIL KE TERBESAR")
print("------- DENGAN METODE BUBBLE SORT -------")
print('*'*41)

bil = []
n = int(input("\nMasukan Jumlah Bilangan = "))

for x in range(n):
    m=x+1
    a = int(input("Bilangan ke %d = "%m))
    bil.append(a)
print("\nList Bilangan yang Anda Masukan = ", bil)

for i in range (len(bil)):  
    for j in range (0, (len(bil)-1)-i):  
        if (bil[j] > bil[j+1]):  
            temp = bil[j]  
            bil[j] = bil[j+1]  
            bil[j+1] = temp

print("\nHasil Pengurutan = ", bil)