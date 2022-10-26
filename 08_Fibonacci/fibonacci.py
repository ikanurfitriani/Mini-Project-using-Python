print('*'*27)
print("MENAMPILKAN DERET FIBONACCI")
print('*'*27)

def fibo(n):
  if n < 1:
    return [n]

  listSebelumN = fibo(n - 1)
  angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
  angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

  return listSebelumN + [angka1 + angka2]

panjang = int(input('Masukan panjang deret = '))

print('\n', fibo(panjang - 1))