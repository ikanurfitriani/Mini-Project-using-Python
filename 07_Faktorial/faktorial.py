print('*'*20)
print("MENGHITUNG FAKTORIAL")
print('*'*20)

n = int(input('Masukan nilai n = '))

def hitung_faktorial (n):
  if n > 2:
    return n * hitung_faktorial(n - 1)

  return 2

faktorial = hitung_faktorial(n)
print(f'\n{n}! = {faktorial}')
