print('*'*23)
print("MENGHITUNG PERPANGKATAN")
print('*'*23)

bil = int(input('Masukkan bilangan : '))
pangkat = int(input('Masukkan pangkat : '))

def hitung_pangkat(bil, pangkat):
  if pangkat > 1:
    return bil * hitung_pangkat(bil, pangkat - 1)

  return bil

hasil = hitung_pangkat(bil, pangkat)
print(f'\nHasil = {hasil}')