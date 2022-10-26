print('*'*36)
print("BILANGAN GANJIL GENAP DENGAN BATASAN")
print('*'*36)

# Input batas
print('Masukan batasan!')
awal = int(input('Bilangan awal: '))
akhir = int(input('Bilangan akhir: '))

print("""\nTampilkan bilangan
 1. Ganjil
 2. Genap""")
print('')

# Input pilihan
pilihan = int(input('Pilihan: '))

# Periksa pilihan 1, 2 atau bukan keduanya
if pilihan not in [1, 2]:
  print('[WARNING] Pilihan salah!')
else:
  for x in range(awal, akhir + 1):
    if pilihan == 1 and x % 2 == 1:
      print(x, end=' ')
    elif pilihan == 2 and x % 2 == 0:
      print(x, end=' ')
  else:
    print('\n')