print('*'*25)
print("MENENTUKAN BILANGAN PRIMA")
print('*'*25)

# Input bilangan
bil = int(input("Masukan bilangan: "))

# Pengecekkan bilangan prima
if bil > 1:
   # mengecek faktor pembagi dengan operasi modulus
   for i in range(2, bil):
       if (bil % i) == 0:
           print(bil,"bukan bilangan Prima")
           print("Karena",bil,"dapat dihasilkan dari",i,"dikalikan",bil//i)
           break
   else:
       print(bil,"merupakan bilangan Prima")
else:
   print("[WARNING] Salah masukan bilangan!")