print('*'*30)
print("KONVERSI SATUAN LUSIN DAN KODI")
print('*'*30)

jumlah_barang = int(input('Masukan jumlah barang: '))

satuan_lusin = round(jumlah_barang / 12, 2)
satuan_kodi = round(jumlah_barang / 20, 2)

# konversi x.0 menjadi x
if satuan_lusin % 1 == 0:
  satuan_lusin = int(satuan_lusin)

if satuan_kodi % 1 == 0:
  satuan_kodi = int(satuan_kodi)

print(f'\n{jumlah_barang} = {satuan_lusin} lusin')
print(f'{jumlah_barang} = {satuan_kodi} kodi')