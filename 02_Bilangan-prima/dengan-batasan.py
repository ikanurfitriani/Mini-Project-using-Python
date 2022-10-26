print('*'*29)
print("BILANGAN PRIMA DENGAN BATASAN")
print('*'*29)

awal = int(input('Masukan bilangan awal: '))
akhir = int(input('Masukan bilangan akhir: '))
 
list_batas = [i for i in range(awal, akhir +1 )]
 
bilangan_prima = [i for i in list_batas if (i==2 or i==3 or i==5 or i==7) or (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0)]

print("\nBerikut bilangan prima dari range bilangan yang Anda input:")
print(bilangan_prima)
print('')